#!/usr/bin/env python3
"""Generator boxów aero FS (2027 z wyciągu + 2026 v1.1 do porównania) → STEP + podgląd PNG.

Użycie:  python3 gen_boxes.py [params.toml]
Wymaga:  cadquery (pip install cadquery), matplotlib.

Każda strefa to osobna, nazwana bryła w złożeniu STEP:
  OK_*   – przestrzeń, w której aero może być (po odjęciu keep-outów)
  KO_*   – strefy zakazane dla każdej części auta (T 2.1.3 / T 2.1.4)
  REF_*  – opony i płaszczyzny odniesienia
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
    wf: float
    wr: float
    tf: float
    tr: float
    x_hr: float
    gc: float
    ko_lat: float
    ko_h: float
    f_out: float

    # charakterystyczne współrzędne
    @property
    def yin_f(self):  # most inboard point przedniej opony
        return self.tf / 2 - self.wf / 2

    @property
    def yout_f(self):
        return self.tf / 2 + self.wf / 2

    @property
    def yin_r(self):
        return self.tr / 2 - self.wr / 2

    @property
    def yout_r(self):
        return self.tr / 2 + self.wr / 2

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
        """T 8.2.2 b1: pionowa płaszczyzna styczna do most outboard przód i tył."""
        return self.yout_f + (self.yout_r - self.yout_f) * (x / self.wb)


def load(path):
    p = tomllib.loads(Path(path).read_text())
    c, m = p["car"], p["model"]
    return Car(
        wb=c["wheelbase"], rf=c["tire_radius_front"], rr=c["tire_radius_rear"],
        wf=c["tire_width_front"], wr=c["tire_width_rear"],
        tf=c["track_front"], tr=c["track_rear"], x_hr=c["x_head_restraint"],
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
    """Pryzmat ograniczony płaszczyzną T 8.2.2 b1 (może być zbieżny, gdy rozstaw przód ≠ tył)."""
    x0: float
    x1: float
    z0: float
    z1: float


@dataclass
class Tire:
    x: float
    r: float
    w: float
    track: float


def solid_of(car, g):
    if isinstance(g, Box):
        def one(y0, y1):
            return cq.Solid.makeBox(g.x1 - g.x0, y1 - y0, g.z1 - g.z0,
                                    cq.Vector(g.x0, y0, g.z0))
        if g.ylo == 0:
            return one(-g.yhi, g.yhi)
        return one(g.ylo, g.yhi).fuse(one(-g.yhi, -g.ylo))
    if isinstance(g, W1Prism):
        pts = [(g.x0, -car.y_w1(g.x0)), (g.x1, -car.y_w1(g.x1)),
               (g.x1, car.y_w1(g.x1)), (g.x0, car.y_w1(g.x0))]
        wp = cq.Workplane("XY", origin=(0, 0, g.z0)).polyline(pts).close()
        return wp.extrude(g.z1 - g.z0).val()
    if isinstance(g, Tire):
        parts = []
        for side in (1, -1):
            yc = side * g.track / 2
            cyl = cq.Solid.makeCylinder(g.r, g.w, cq.Vector(g.x, yc - g.w / 2, g.r),
                                        cq.Vector(0, 1, 0))
            parts.append(cyl)
        return parts[0].fuse(parts[1])
    raise TypeError(g)


# ---------------------------------------------------------------- strefy
def zones_2027(c: Car):
    xa, xhr, xf, xr = c.x_a, c.x_hr, c.x_front_lim, c.x_rear_lim
    top_mid = min(c.top_f, c.top_r)  # C2: projektujemy pod niższą górę opon
    ko_front = Box(-c.rf - 75, c.rf + 75, c.yin_f, c.yout_f + c.ko_lat, 0, c.ko_h)
    ko_rear = Box(c.wb - c.rr - 75, c.wb + c.rr + 75, c.yin_r, c.yout_r + c.ko_lat, 0, 700)
    ko_rear_add = Box(c.wb - c.rr - 75, c.wb + c.rr + 75, c.yin_r - 150, c.yin_r, c.top_r, 700)
    keepouts = [ko_front, ko_rear, ko_rear_add]
    z = [
        # (nazwa, kategoria, geometria, reguła, odjąć keep-outy?)
        ("OK_2027_przod_ponizej_350", "OK",
         Box(xf, xa, 0, c.yout_f, c.gc, 350), "T 8.2.1 b1 + T 8.2.3", True),
        ("SZARA_2027_przod_outboard_bez_limitu_szer_T822", "GREY",
         Box(xf, xa, c.yout_f, c.yout_f + c.f_out, c.gc, 350), "T 8.2.2 milczy (loophole B3)", True),
        ("OK_2027_srodek_ponizej_gory_opon", "OK",
         W1Prism(xa, xhr, c.gc, top_mid), "T 8.2.1 b3 + T 8.2.2 b1", True),
        ("OK_2027_tyl_nisko_pelna_szer", "OK",
         W1Prism(xhr, xr, c.gc, c.top_r), "T 8.2.1 b2 + T 8.2.2 b1", True),
        ("OK_2027_tyl_pas_gora_opony-700_inboard150", "OK",
         Box(xhr, xr, 0, c.yin_r - 150, c.top_r, 700), "T 8.2.2 b2", True),
        ("OK_2027_tyl_700-1100_do_zewn_opony", "OK",
         Box(xhr, xr, 0, c.yout_r, 700, 1100), "T 8.2.2 b3", True),
        ("KO_2027_T213_kolo_przod", "KO", ko_front, "T 2.1.3 b2 (outboard bez końca, bez limitu wys.)", False),
        ("KO_2027_T213_kolo_tyl_do_700", "KO", ko_rear, "T 2.1.3 b2 (do 700 mm)", False),
        ("KO_2027_T213_tyl_dodatkowy_150", "KO", ko_rear_add, "T 2.1.3 b3", False),
        # T 2.1.4 — nie odejmujemy od OK: zależy od interpretacji (loophole B4)
        ("Q_2027_T214_wariantA_obszar_75wys", "Q",
         Box(xf, xa, 0, c.yout_f, 0, 75), "T 2.1.4 — jeśli 75 mm wys. i Tech ustawia dowolnie", False),
        ("Q_2027_T214_wariantB_obszar_250wys", "Q",
         Box(xf, xa, 0, c.yout_f, 0, 250), "T 2.1.4 — jeśli 250 mm wys. i Tech ustawia dowolnie", False),
    ]
    return z, keepouts


def zones_2026(c: Car):
    xhr, xf, xr = c.x_hr, c.x_front_lim, c.x_rear_lim
    ko_front = Box(-c.rf - 75, c.rf + 75, c.yin_f, c.yout_f, 0, c.ko_h)
    ko_rear = Box(c.wb - c.rr - 75, c.wb + c.rr + 75, c.yin_r, c.yout_r, 0, c.ko_h)
    keepouts = [ko_front, ko_rear]
    z = [
        ("OK_2026_przod_srodek_ponizej_500", "OK",
         Box(xf, 0, 0, c.yin_f, c.gc, 500), "T 8.2.1 b1", True),
        ("OK_2026_przod_outboard_ponizej_250", "OK",
         Box(xf, 0, c.yin_f, c.yout_f, c.gc, 250), "T 8.2.1 b2", True),
        ("OK_2026_srodek_ponizej_500", "OK",
         W1Prism(0, xhr, c.gc, 500), "T 8.2.1 b1 + T 8.2.2 b1", True),
        ("OK_2026_tyl_ponizej_500", "OK",
         W1Prism(xhr, xr, c.gc, 500), "T 8.2.2 b1", True),
        ("OK_2026_tyl_500-1100_inboard_opony", "OK",
         Box(xhr, xr, 0, c.yin_r, 500, 1100), "T 8.2.1 b3 + T 8.2.2 b2", True),
        ("KO_2026_T213_kolo_przod", "KO", ko_front, "T 2.1.3", False),
        ("KO_2026_T213_kolo_tyl", "KO", ko_rear, "T 2.1.3", False),
    ]
    return z, keepouts


def refs(c: Car):
    t = 1.0
    return [
        ("REF_opony_przod", "REF", Tire(0, c.rf, c.wf, c.tf), "", False),
        ("REF_opony_tyl", "REF", Tire(c.wb, c.rr, c.wr, c.tr), "", False),
        ("REF_plaszczyzna_A_LE_przednich_opon", "REF",
         Box(c.x_a - t, c.x_a, 0, c.yout_f + c.ko_lat, 0, 1100), "", False),
        ("REF_plaszczyzna_HR", "REF",
         Box(c.x_hr - t, c.x_hr, 0, c.yout_r + c.ko_lat, 0, 1100), "", False),
    ]


# ---------------------------------------------------------------- budowa i eksport
HALF = None


def half_space(c):
    big = 10000.0
    return cq.Solid.makeBox(2 * big, big, 2 * big, cq.Vector(-big, -big, -big))  # y ≤ 0


def build(c, zones, keepouts):
    ko = [solid_of(c, k) for k in keepouts]
    out = []
    for name, cat, g, rule, cut in zones:
        s = solid_of(c, g)
        if cut:
            for k in ko:
                s = s.cut(k)
        out.append((name, cat, s, rule))
    return out


def export(bodies, path, half=False, c=None):
    assy = cq.Assembly(name=path.stem)
    hs = half_space(c) if half else None
    for name, cat, s, _ in bodies:
        shp = s.intersect(hs) if half else s
        if shp.Volume() <= 1e-6:
            continue
        assy.add(cq.Workplane().add(shp), name=name, color=cq.Color(*COLORS[cat]))
    assy.export(str(path))


def limits_table(c):
    rows = [
        ("Płaszczyzna A (LE przednich opon) — x", c.x_a),
        ("Limit do przodu (700 mm przed oponami) — x", c.x_front_lim),
        ("Limit do tyłu (250 mm za tylnymi oponami) — x", c.x_rear_lim),
        ("Płaszczyzna HR — x  [PLACEHOLDER]", c.x_hr),
        ("Góra przedniej opony — z", c.top_f),
        ("Góra tylnej opony — z", c.top_r),
        ("Wewn. krawędź przedniej opony — |y|", c.yin_f),
        ("Zewn. krawędź przedniej opony — |y|", c.yout_f),
        ("Wewn. krawędź tylnej opony — |y|", c.yin_r),
        ("Zewn. krawędź tylnej opony — |y|", c.yout_r),
        ("2027 pas góra opony–700: max |y| (wewn. − 150)", c.yin_r - 150),
        ("2027 700–1100: max |y| (zewn. tylnej opony)", c.yout_r),
        ("2026 >500: max |y| (wewn. tylnej opony)", c.yin_r),
        ("2027 rozpiętość RW 700–1100 (pełna)", 2 * c.yout_r),
        ("2026 rozpiętość RW >500 (pełna)", 2 * c.yin_r),
        ("2027 keep-out tylnej opony — x od", c.wb - c.rr - 75),
        ("2027 keep-out tylnej opony — x do", c.wb + c.rr + 75),
        ("Okno na mocowania endplate'u (loophole A2) — długość", c.x_rear_lim - (c.wb + c.rr + 75)),
    ]
    lines = ["| Wielkość | mm |", "|---|---:|"]
    lines += [f"| {k} | {v:.1f} |" for k, v in rows]
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
                    ax_r.add_patch(Rectangle((side * g.track / 2 - g.w / 2, 0), g.w, 2 * g.r,
                                             fill=False, lw=1.2, color="k"))
                continue
            if cat == "REF":
                ax_s.axvline(g.x1, color="k", ls="--", lw=0.8)
                continue
            if isinstance(g, W1Prism):
                x0, x1, z0, z1 = g.x0, g.x1, g.z0, g.z1
                ylo, yhi = 0, max(c.y_w1(g.x0), c.y_w1(g.x1))
            else:
                x0, x1, z0, z1, ylo, yhi = g.x0, g.x1, g.z0, g.z1, g.ylo, g.yhi
            kw = dict(alpha=0.28 if cat != "KO" else 0.35, color=col, lw=0)
            if cat in ("KO", "Q"):
                kw.update(hatch="///" if cat == "KO" else "..", fill=False, ec=col, lw=0.8, alpha=0.9)
                kw.pop("color")
            ax_s.add_patch(Rectangle((x0, z0), x1 - x0, z1 - z0, **kw))
            # widok z tyłu: tylko strefy za HR + keep-outy tylne (czytelność)
            if x0 >= c.x_hr - 1 or ("tyl" in name and cat == "KO"):
                if ylo == 0:
                    ax_r.add_patch(Rectangle((-yhi, z0), 2 * yhi, z1 - z0, **kw))
                else:
                    ax_r.add_patch(Rectangle((ylo, z0), yhi - ylo, z1 - z0, **kw))
                    ax_r.add_patch(Rectangle((-yhi, z0), yhi - ylo, z1 - z0, **kw))
        ax_s.set_xlim(c.x_front_lim - 100, c.x_rear_lim + 100)
        ax_s.set_ylim(0, 1200)
        ax_s.set_aspect("equal")
        ax_s.set_title(f"{title} — widok z boku (x do tyłu, z w górę) [mm]")
        ax_s.grid(alpha=0.3)
        lim = c.yout_r + 250
        ax_r.set_xlim(-lim, lim)
        ax_r.set_ylim(0, 1200)
        ax_r.set_aspect("equal")
        ax_r.set_title(f"{title} — widok z tyłu, strefy za HR [mm]")
        ax_r.grid(alpha=0.3)
    fig.text(0.01, 0.005, "zielone = aero dozwolone, żółte = szara strefa, czerwone /// = keep-out, "
             "fioletowe ... = T 2.1.4 (interpretacja); rozstaw, szer. opon i x_HR = PLACEHOLDER (params.toml)",
             fontsize=9)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(path, dpi=110)


def main():
    c = load(sys.argv[1] if len(sys.argv) > 1 else HERE / "params.toml")
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    z27, k27 = zones_2027(c)
    z26, k26 = zones_2026(c)
    r = refs(c)
    b27 = build(c, z27 + r, k27)
    b26 = build(c, z26 + r, k26)
    export(b27, out / "fs2027_aero_boxes_full.step", c=c)
    export(b27, out / "fs2027_aero_boxes_half_yneg.step", half=True, c=c)
    export(b26, out / "fs2026_aero_boxes_full.step", c=c)
    (out / "limits.md").write_text(
        "# Wymiary boxów (auto z params.toml)\n\n"
        "Układ jak w CFD: x do tyłu od osi przedniej, |y| od symetrii, z od gruntu.\n\n"
        + limits_table(c) + "\n\n## Bryły\n\n| Bryła | Reguła | Objętość [dm³] |\n|---|---|---:|\n"
        + "\n".join(f"| {n} | {rule} | {s.Volume() / 1e6:.1f} |"
                    for n, cat, s, rule in b27 + b26 if not n.startswith("REF")) + "\n")
    preview(c, [("FS 2027 (wyciąg)", z27 + r), ("FS 2026 v1.1", z26 + r)], out / "preview.png")
    for p in sorted(out.iterdir()):
        print(f"{p.name:40s} {p.stat().st_size / 1024:8.1f} kB")


if __name__ == "__main__":
    main()
