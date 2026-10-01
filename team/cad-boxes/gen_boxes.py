#!/usr/bin/env python3
"""Generator boxów aero FS (2027 z wyciągu + 2026 v1.1 do porównania) → STEP + podgląd PNG.

Użycie:  python3 gen_boxes.py [params.toml]
Wymaga:  cadquery (pip install cadquery), matplotlib.

Pliki wyjściowe (out/):
  fsYYYY_dozwolone*.step – TYLKO przestrzeń, w której aero może być (keep-outy już odjęte)
  fs2027_zakazane.step   – keep-outy T 2.1.3 + warianty T 2.1.4 (osobno, żeby nie mylić z dozwolonymi)
  ref_opony.step         – opony (do dopasowania w złożeniu)
Reguły i cytaty: sources/fs-rules-2027-t8.md, sources/rules-2027-aero-loopholes.md.
"""
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

import cadquery as cq

HERE = Path(__file__).resolve().parent

COLORS = {
    "OK": (0.20, 0.65, 0.30, 0.35),
    "GREY": (0.95, 0.70, 0.10, 0.35),
    "KO": (0.85, 0.15, 0.15, 0.45),
    "Q": (0.60, 0.20, 0.80, 0.30),
    "REF": (0.25, 0.25, 0.25, 1.0),
}


@dataclass
class Car:
    wb: float
    rf: float
    rr: float
    yin_f: float   # |y| most inboard point przedniej opony
    yout_f: float  # |y| most outboard point przedniej opony
    yin_r: float
    yout_r: float
    x_hr: float
    m: float       # zapas bezpieczeństwa (zmniejsza strefy dozwolone, powiększa keep-outy)
    w1_mode: str   # "taper" | "parallel" — interpretacja płaszczyzny T 8.2.2 b1
    gc: float
    ko_lat: float
    ko_h: float
    f_out: float

    @property
    def x_a(self):  # płaszczyzna przez leading edge przednich opon
        return -self.rf

    @property
    def x_front_lim(self):  # T 8.2.3: 700 mm przed przednimi oponami
        return -self.rf - 700.0

    @property
    def x_rear_lim(self):  # T 8.2.3: 250 mm za tylnymi oponami
        return self.wb + self.rr + 250.0

    @property
    def top_f(self):
        return 2 * self.rf

    @property
    def top_r(self):
        return 2 * self.rr

    def y_w1(self, x):
        """T 8.2.2 b1: pionowa płaszczyzna przez most outboard point przód i tył (bez zapasu).

        taper    – jedna płaszczyzna styczna do obu opon (zbieżna, gdy krawędzie przód ≠ tył)
        parallel – płaszczyzna równoległa do osi auta przez bardziej zewnętrzną z opon
        """
        if self.w1_mode == "parallel":
            return max(self.yout_f, self.yout_r)
        return self.yout_f + (self.yout_r - self.yout_f) * (x / self.wb)


def load(path):
    p = tomllib.loads(Path(path).read_text())
    c, m = p["car"], p["model"]
    return Car(
        wb=c["wheelbase"], rf=c["tire_radius_front"], rr=c["tire_radius_rear"],
        yin_f=c["y_inner_front"], yout_f=c["y_outer_front"],
        yin_r=c["y_inner_rear"], yout_r=c["y_outer_rear"], x_hr=c["x_head_restraint"],
        m=m["margin"], w1_mode=m["width_plane_mode"],
        gc=m["ground_clearance"], ko_lat=m["keepout_lateral_extra"],
        ko_h=m["keepout_height_cap"], f_out=m["front_outboard_extra"],
    )


# ---------------------------------------------------------------- prymitywy
@dataclass
class Box:
    """Prostopadłościan; y: |y| w [ylo, yhi] po obu stronach (ylo == 0 → jedna bryła przez środek)."""
    x0: float
    x1: float
    ylo: float
    yhi: float
    z0: float
    z1: float


@dataclass
class W1Prism:
    """Pryzmat ograniczony płaszczyzną T 8.2.2 b1 pomniejszoną o zapas."""
    x0: float
    x1: float
    z0: float
    z1: float


@dataclass
class Tire:
    x: float
    r: float
    yin: float
    yout: float


def solid_of(car, g):
    if isinstance(g, Box):
        def one(y0, y1):
            return cq.Solid.makeBox(g.x1 - g.x0, y1 - y0, g.z1 - g.z0,
                                    cq.Vector(g.x0, y0, g.z0))
        if g.ylo == 0:
            return one(-g.yhi, g.yhi)
        return one(g.ylo, g.yhi).fuse(one(-g.yhi, -g.ylo))
    if isinstance(g, W1Prism):
        y0, y1 = car.y_w1(g.x0) - car.m, car.y_w1(g.x1) - car.m
        pts = [(g.x0, -y0), (g.x1, -y1), (g.x1, y1), (g.x0, y0)]
        wp = cq.Workplane("XY", origin=(0, 0, g.z0)).polyline(pts).close()
        return wp.extrude(g.z1 - g.z0).val()
    if isinstance(g, Tire):
        w = g.yout - g.yin
        parts = [cq.Solid.makeCylinder(g.r, w, cq.Vector(g.x, side * (g.yin + g.yout) / 2 - w / 2, g.r),
                                       cq.Vector(0, 1, 0)) for side in (1, -1)]
        return parts[0].fuse(parts[1])
    raise TypeError(g)


# ---------------------------------------------------------------- strefy
# Zapas m: granice stref dozwolonych przesunięte o m do środka; na granicy dwóch stref dozwolonych
# wygrywa ostrzejsza (np. wąski pas zaczyna się m PONIŻEJ góry opony). Prześwit 30 mm bez zapasu.

def keepouts_2027(c: Car):
    m = c.m
    ko_front = Box(-c.rf - 75 - m, c.rf + 75 + m, c.yin_f - m, c.yout_f + c.ko_lat, 0, c.ko_h)
    ko_rear = Box(c.wb - c.rr - 75 - m, c.wb + c.rr + 75 + m, c.yin_r - m, c.yout_r + c.ko_lat, 0, 700 + m)
    ko_rear_add = Box(c.wb - c.rr - 75 - m, c.wb + c.rr + 75 + m, c.yin_r - 150 - m, c.yin_r - m,
                      c.top_r - m, 700 + m)
    return [
        ("KO_2027_T213_kolo_przod", "KO", ko_front, "T 2.1.3 b2 (outboard bez końca, bez limitu wys.)", False),
        ("KO_2027_T213_kolo_tyl_do_700", "KO", ko_rear, "T 2.1.3 b2 (do 700 mm)", False),
        ("KO_2027_T213_tyl_dodatkowy_150", "KO", ko_rear_add, "T 2.1.3 b3", False),
    ]


def zones_2027(c: Car):
    m = c.m
    xa, xhr, xf, xr = c.x_a + m, c.x_hr + m, c.x_front_lim + m, c.x_rear_lim - m
    top_mid = min(c.top_f, c.top_r) - m  # C2: projektujemy pod niższą górę opon
    return [
        # (nazwa, kategoria, geometria, reguła, odjąć keep-outy?)
        ("OK_2027_przod_ponizej_350", "OK",
         Box(xf, xa, 0, c.yout_f - m, c.gc, 350 - m), "T 8.2.1 b1 + T 8.2.3", True),
        ("SZARA_2027_przod_outboard_bez_limitu_szer_T822", "GREY",
         Box(xf, xa, c.yout_f - m, c.yout_f + c.f_out, c.gc, 350 - m), "T 8.2.2 milczy (loophole B3)", True),
        ("OK_2027_srodek_ponizej_gory_opon", "OK",
         W1Prism(xa, xhr, c.gc, top_mid), "T 8.2.1 b3 + T 8.2.2 b1", True),
        ("OK_2027_tyl_nisko_pelna_szer", "OK",
         W1Prism(xhr, xr, c.gc, c.top_r - m), "T 8.2.1 b2 + T 8.2.2 b1", True),
        ("OK_2027_tyl_pas_gora_opony-700_inboard150", "OK",
         Box(xhr, xr, 0, c.yin_r - 150 - m, c.top_r - m, 700 + m), "T 8.2.2 b2", True),
        ("OK_2027_tyl_700-1100_do_zewn_opony", "OK",
         Box(xhr, xr, 0, c.yout_r - m, 700 + m, 1100 - m), "T 8.2.2 b3", True),
    ]


def questions_2027(c: Car):
    xf, xa = c.x_front_lim, c.x_a
    return [  # T 2.1.4 — nie odejmujemy od OK: zależy od interpretacji (loophole B4)
        ("Q_2027_T214_wariantA_obszar_75wys", "Q",
         Box(xf, xa, 0, c.yout_f, 0, 75), "T 2.1.4 — jeśli 75 mm wys. i Tech ustawia dowolnie", False),
        ("Q_2027_T214_wariantB_obszar_250wys", "Q",
         Box(xf, xa, 0, c.yout_f, 0, 250), "T 2.1.4 — jeśli 250 mm wys. i Tech ustawia dowolnie", False),
    ]


def keepouts_2026(c: Car):
    m = c.m
    return [
        ("KO_2026_T213_kolo_przod", "KO",
         Box(-c.rf - 75 - m, c.rf + 75 + m, c.yin_f - m, c.yout_f + m, 0, c.ko_h), "T 2.1.3", False),
        ("KO_2026_T213_kolo_tyl", "KO",
         Box(c.wb - c.rr - 75 - m, c.wb + c.rr + 75 + m, c.yin_r - m, c.yout_r + m, 0, c.ko_h), "T 2.1.3", False),
    ]


def zones_2026(c: Car):
    m = c.m
    xhr, xf, xr = c.x_hr + m, c.x_front_lim + m, c.x_rear_lim - m
    return [
        ("OK_2026_przod_srodek_ponizej_500", "OK",
         Box(xf, m, 0, c.yin_f - m, c.gc, 500 - m), "T 8.2.1 b1", True),
        ("OK_2026_przod_outboard_ponizej_250", "OK",
         Box(xf, m, c.yin_f - m, c.yout_f - m, c.gc, 250 - m), "T 8.2.1 b2", True),
        ("OK_2026_srodek_ponizej_500", "OK",
         W1Prism(m, xhr, c.gc, 500 - m), "T 8.2.1 b1 + T 8.2.2 b1", True),
        ("OK_2026_tyl_ponizej_500", "OK",
         W1Prism(xhr, xr, c.gc, 500 - m), "T 8.2.2 b1", True),
        ("OK_2026_tyl_500-1100_inboard_opony", "OK",
         Box(xhr, xr, 0, c.yin_r - m, 500 - m, 1100 - m), "T 8.2.1 b3 + T 8.2.2 b2", True),
    ]


def refs(c: Car):
    return [
        ("REF_opony_przod", "REF", Tire(0, c.rf, c.yin_f, c.yout_f), "", False),
        ("REF_opony_tyl", "REF", Tire(c.wb, c.rr, c.yin_r, c.yout_r), "", False),
    ]


# ---------------------------------------------------------------- budowa i eksport
def half_space():
    big = 10000.0
    return cq.Solid.makeBox(2 * big, big, 2 * big, cq.Vector(-big, -big, -big))  # y ≤ 0


def build(c, zones, keepouts):
    ko = [solid_of(c, g) for _, _, g, _, _ in keepouts]
    out = []
    for name, cat, g, rule, cut in zones:
        s = solid_of(c, g)
        if cut:
            for k in ko:
                s = s.cut(k)
        out.append((name, cat, s, rule))
    return out


def export(bodies, path, half=False):
    assy = cq.Assembly(name=path.stem)
    hs = half_space() if half else None
    for name, cat, s, _ in bodies:
        shp = s.intersect(hs) if half else s
        if shp.Volume() <= 1e-6:
            continue
        assy.add(cq.Workplane().add(shp), name=name, color=cq.Color(*COLORS[cat]))
    assy.export(str(path))


def limits_table(c):
    m = c.m
    rows = [
        ("Zapas bezpieczeństwa m (już odjęty od stref dozwolonych)", m),
        ("Płaszczyzna A (LE przednich opon) — x", c.x_a),
        ("Limit do przodu (700 mm przed oponami) — x", c.x_front_lim),
        ("Limit do tyłu (250 mm za tylnymi oponami) — x", c.x_rear_lim),
        ("Płaszczyzna HR — x", c.x_hr),
        ("Góra przedniej opony — z", c.top_f),
        ("Góra tylnej opony — z", c.top_r),
        ("Wewn. / zewn. krawędź przedniej opony — |y|", f"{c.yin_f:.1f} / {c.yout_f:.1f}"),
        ("Wewn. / zewn. krawędź tylnej opony — |y|", f"{c.yin_r:.1f} / {c.yout_r:.1f}"),
        ("2027 pas góra opony–700: max |y| (wewn. tylnej − 150 − m)", c.yin_r - 150 - m),
        ("2027 700–1100: max |y| (zewn. tylnej − m)", c.yout_r - m),
        ("2027 rozpiętość RW 700–1100 (pełna, z zapasem)", 2 * (c.yout_r - m)),
        ("2026 rozpiętość RW >500 (pełna, z zapasem)", 2 * (c.yin_r - m)),
        (f"Szerokość nisko (T 8.2.2 b1, tryb {c.w1_mode}) przy x = 0 / x = limit tył",
         f"{c.y_w1(0) - m:.1f} / {c.y_w1(c.x_rear_lim) - m:.1f}"),
        ("Okno na mocowania endplate'u (loophole A2) — długość", c.x_rear_lim - (c.wb + c.rr + 75) - 2 * m),
    ]
    lines = ["| Wielkość | mm |", "|---|---:|"]
    lines += [f"| {k} | {v if isinstance(v, str) else f'{v:.1f}'} |" for k, v in rows]
    return "\n".join(lines)


def preview(c, sets, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Circle

    fig, axes = plt.subplots(len(sets), 2, figsize=(16, 5.2 * len(sets)),
                             gridspec_kw={"width_ratios": [2.3, 1]})
    for row, (title, zones) in enumerate(sets):
        ax_s, ax_r = axes[row]
        for name, cat, g, _, _ in zones:
            col = COLORS[cat][:3]
            if isinstance(g, Tire):
                ax_s.add_patch(Circle((g.x, g.r), g.r, fill=False, lw=1.5, color="k"))
                for side in (1, -1):
                    a, b = sorted((side * g.yin, side * g.yout))
                    ax_r.add_patch(Rectangle((a, 0), b - a, 2 * g.r, fill=False, lw=1.2, color="k"))
                continue
            if isinstance(g, W1Prism):
                x0, x1, z0, z1 = g.x0, g.x1, g.z0, g.z1
                ylo, yhi = 0, max(c.y_w1(g.x0), c.y_w1(g.x1)) - c.m
            else:
                x0, x1, z0, z1, ylo, yhi = g.x0, g.x1, g.z0, g.z1, g.ylo, g.yhi
            kw = dict(alpha=0.28, color=col, lw=0)
            if cat in ("KO", "Q"):
                kw = dict(hatch="///" if cat == "KO" else "..", fill=False, ec=col, lw=0.8, alpha=0.9)
            ax_s.add_patch(Rectangle((x0, z0), x1 - x0, z1 - z0, **kw))
            if x0 >= c.x_hr - 1 or ("tyl" in name and cat == "KO"):  # widok z tyłu: strefy za HR
                if ylo == 0:
                    ax_r.add_patch(Rectangle((-yhi, z0), 2 * yhi, z1 - z0, **kw))
                else:
                    ax_r.add_patch(Rectangle((ylo, z0), yhi - ylo, z1 - z0, **kw))
                    ax_r.add_patch(Rectangle((-yhi, z0), yhi - ylo, z1 - z0, **kw))
        for x in (c.x_a, c.x_hr):
            ax_s.axvline(x, color="k", ls="--", lw=0.8)
        ax_s.set_xlim(c.x_front_lim - 100, c.x_rear_lim + 100)
        ax_s.set_ylim(0, 1200)
        ax_s.set_aspect("equal")
        ax_s.set_title(f"{title} — widok z boku (x do tyłu, z w górę) [mm]")
        ax_s.grid(alpha=0.3)
        lim = max(c.yout_f, c.yout_r) + 250
        ax_r.set_xlim(-lim, lim)
        ax_r.set_ylim(0, 1200)
        ax_r.set_aspect("equal")
        ax_r.set_title(f"{title} — widok z tyłu, strefy za HR [mm]")
        ax_r.grid(alpha=0.3)
    fig.text(0.01, 0.005, f"zielone = aero dozwolone (zapas {c.m:g} mm), żółte = szara strefa, "
             "czerwone /// = keep-out, fioletowe ... = T 2.1.4 (interpretacja); przerywane = płaszczyzny A i HR",
             fontsize=9)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(path, dpi=110)


def main():
    c = load(sys.argv[1] if len(sys.argv) > 1 else HERE / "params.toml")
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    for old in out.glob("*.step"):
        old.unlink()
    k27, q27, k26, r = keepouts_2027(c), questions_2027(c), keepouts_2026(c), refs(c)
    ok27 = build(c, zones_2027(c), k27)
    ok26 = build(c, zones_2026(c), k26)
    forbidden = build(c, k27 + q27, [])
    export(ok27, out / "fs2027_dozwolone_full.step")
    export(ok27, out / "fs2027_dozwolone_half_yneg.step", half=True)
    export(ok26, out / "fs2026_dozwolone_full.step")
    export(forbidden, out / "fs2027_zakazane.step")
    export(build(c, r, []), out / "ref_opony.step")
    (out / "limits.md").write_text(
        "# Wymiary boxów (auto z params.toml)\n\n"
        "Układ jak w CFD: x do tyłu od osi przedniej, |y| od symetrii, z od gruntu.\n\n"
        + limits_table(c) + "\n\n## Bryły\n\n| Plik | Bryła | Reguła | Objętość [dm³] |\n|---|---|---|---:|\n"
        + "\n".join(f"| {f} | {n} | {rule} | {s.Volume() / 1e6:.1f} |"
                    for f, bodies in (("fs2027_dozwolone", ok27), ("fs2027_zakazane", forbidden),
                                      ("fs2026_dozwolone", ok26))
                    for n, cat, s, rule in bodies) + "\n")
    preview(c, [("FS 2027 (wyciąg)", zones_2027(c) + k27 + q27 + r),
                ("FS 2026 v1.1", zones_2026(c) + k26 + r)], out / "preview.png")
    for p in sorted(out.iterdir()):
        print(f"{p.name:40s} {p.stat().st_size / 1024:8.1f} kB")


if __name__ == "__main__":
    main()
