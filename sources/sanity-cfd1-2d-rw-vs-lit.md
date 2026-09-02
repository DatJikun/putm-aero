# Sanity-check: CFD#1 2D RW (H1) vs Staniszewski / Jackson / McBeath

**Data:** 2026-09-02 (Europe/Warsaw)  
**Cel:** czy baseline 2D OpenFOAM CFD#1 jest w sensownym rzędzie wielkości i czy setup pozwala oczekiwać sensownych **kierunków** Δ przy kątach/gap/overlap.  
**Nie:** nie wpuszczamy Cl/Cd 2D do `TARGETS.md` ani na kartę RWiter017.

**Źródła CFD#1 (lokalne case’y, nie git):**  
`/workspace/fs-rear-wing-2d-3el/` — `STATUS.md`, `PODSUMOWANIE.md`, `RAPORT_USTAWIEN.md`, `RAPORT_NIEZALEZNOSC_SIATKI.md`, `SERIES.md`.

**Źródła lit. w KB:**  
[staniszewski-2023-wing.md](staniszewski-2023-wing.md), [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md), [checklist-h1-2d-rw-gap-aoa.md](checklist-h1-2d-rw-gap-aoa.md), [research-overnight-h3-fw-unload-rw-gaps.md](research-overnight-h3-fw-unload-rw-gaps.md).

---

## 1. Co policzył CFD#1 (baseline 2D)

Geometria: S1223 × 3, cięciwy

- main = 310 mm  
- flap1 = 190 mm  
- flap2 = 130 mm  

Kąty: **8° / 20° / 32°**. Domenа endplate 800×500 mm, **bez ziemi**. U∞ = **15 m/s**. k-ω SST, wall functions.

Gap / overlap (z SERIES):

- main→flap1: gap ≈ **11,0 mm** (~**3,5%** c_main), overlap ≈ **12,0 mm** (~**3,9%** c_main)  
- flap1→flap2: gap ≈ **9,6 mm** (~**5,1%** c_f1), overlap ≈ **12,4 mm** (~**6,5%** c_f1)

Siły / współczynniki (średnia last-200 @ 2000 iter, medium ~408k):

- Cl ≈ **−2,52** (±0,06)  
- Cd ≈ **0,28** (±0,01)  
- Cl/Cd ≈ **9,1**  
- Fx ≈ **22 N/m**  
- Fz ≈ **−198 N/m**  

Siatka medium:

- komórki ≈ **408 379**  
- checkMesh OK, maxSkew ≈ **1,06**  
- y+ mean ≈ **20** (min ≈ 0,9 / max ≈ 85) — wall-fn OK  

**Niezależność siatki:** coarse (~201k) i fine (~827k) w raporcie jeszcze **PENDING** w momencie tej notatki — medium to tylko **referencja robocza** serii, nie domknięty dowód niezależności.

A1 (main 6,5°) i A2 (main 9,5°) w toku — **brak** jeszcze ΔCl/ΔCd z serii kątów do porównania z literaturą.

---

## 2. Rząd wielkości Cl / Cd

### Co wolno porównywać

| Porównanie | Werdykt |
|------------|---------|
| 2D izolowane skrzydło CFD#1 vs **całe auto** Jackson (CL_DF 1,15 / CD 1,21) albo RWiter017 (Cx 1,229 / Cz −3,682) | **Nie porównywać absolutów** — inna normalizacja i zakres (sekcja vs pojazd). |
| 2D CFD#1 vs 2D Staniszewski (Fx/Fz w N) | **Kierunki trendów tak; absolutów 1:1 nie** — inne profile, kąty i cięciwy. |
| 2D CFD#1 Cl vs opublikowane 2D/sekcyjne multi-element FS | **Rząd wielkości tak.** |

### Kotwice literaturowe (opublikowane)

**MECDC 2014** (3-el. FS, z notatki overnight H3):  

- Cl = **2,81**  
- Cd = **0,81**  
(ich skrzydło; slot gap 3,6% c, overlap 0,75%)

CFD#1: |Cl| ≈ **2,52**, Cd ≈ **0,28**.  
|Cl| jest w tym samym rzędzie co MECDC (~2,5–2,8). Cd CFD#1 jest **niższy** niż MECDC 0,81 — przy łagodniejszych klapach (20°/32° vs typowe high-DF ~25–30°/…) to **nie wygląda na absurd**; nie twierdzimy, że „lepsze od MECDC”, tylko że nie jest poza skalą high-lift 2D.

**Jackson 2018** — gap/overlap na E423 (main 540 mm):  

- gap = **20 mm** ≈ **3,7%** c  
- overlap = **26,25 mm** ≈ **4,9%** c  
- Study 4: flaps **28° / 60°**, overall ≈ **22,8°** (stall ~25°)

CFD#1 gap main→f1 (~3,5% c) siedzi obok Jackson/McBeath. Kąty klap CFD#1 są **znacznie łagodniejsze** niż Study 4 — spodziewany niższy |Cl| sekcji niż agresywny high-DF Jackson; Jackson i tak publikuje Cl **pojazdu**, nie izolowanej 2D.

**Staniszewski 2023** — 2D izolowane, V = **15 m/s** (ten sam V_ref):  

- baseline: Fx = **49,96 N**, Fz = **−397,61 N**  
- po −6,5° main: Fx = **27,83 N**, Fz = **−502,43 N**  
- overlap −30 mm: Fx = **27,11 N**, Fz = **−565,03 N**  
- gap +5/+10 mm: Fx = **26,98 N**, Fz = **−559,80 N**

CFD#1 Fz ≈ **−198 N/m** to ok. **połowa** |Fz| baseline Staniszewskiego. To **nie** jest fail sam w sobie: inne profile (S1223 vs niepodane w tekście Staniszewskiego), inne kąty startowe i cięciwy. Porównujemy **kierunek** zmian w serii, nie „czy −198 = −398”.

---

## 3. Gap / overlap vs McBeath

McBeath (cyt. Jackson / Craig / checklista H1):

- gap: **1–4%** c  
- overlap: **1–6%** c  
- praktyka Craig: gap ~**2%**, overlap ~**1,5%**

CFD#1:

- gap main→f1 **3,5%** → **w paśmie**  
- gap f1→f2 **5,1%** → **lekko powyżej** 4%  
- overlap main→f1 **3,9%** → **w paśmie**  
- overlap f1→f2 **6,5%** → **lekko powyżej** 6%

Werdykt: setup jest **blisko** wytycznych; druga szczelina i overlap flap1→flap2 są trochę „luźniejsze / bardziej zachodzące” niż klasyczne McBeath. W serii gap/overlap (G1/G2, O1/O2) warto pilnować, czy Δ idzie w stronę Staniszewskiego (patrz niżej), a nie tylko czy %c wraca do 1–4 / 1–6.

---

## 4. Oczekiwany kierunek Δ (literatura) — do sprawdzenia jak skończą A1/A2

Z Staniszewskiego 2023 (2D, ten sam V):

1. **Obniżenie kąta main** względem ich baseline ↑ |Fz| i ↓ Fx (aż do ok. −6,5°; dalej −7° już gorzej).  
   → U CFD#1: **A1** (main **6,5°**) powinno dać **|Cl| ≥ baseline** i raczej niższy Cd niż A2, jeśli zachowanie jest podobne.  
   → **A2** (main **9,5°**) — spodziewany **spadek |Cl|** albo gorszy Cl/Cd vs baseline.

2. **Zmniejszanie overlap** (u nich do −30 mm) ↑ |Fz|; −40 mm już pogarsza.  
   → O1 (ovl −10 mm) powinno iść w stronę większego |Cl|, o ile nie wychodzimy poza optimum.

3. **Drobne +gap** (+5/+10 mm) u nich trzyma wysoki docisk przy niskim oporze.  
   → G1/G2: |Cl| bez dużego spadku, Cd nie powinien wybuchnąć.

4. Jackson: nie pchać overall AOA w stall (~25°). CFD#1 overall jest łagodny — zapas przed stall jest OK na start serii.

**Stan na teraz:** kierunków Δ z runów CFD#1 **jeszcze nie zweryfikowano** (A1/A2 pending). Po ich domknięciu dopisać jedną tabelę ΔCl/ΔCd vs baseline i ten rozdział.

---

## 5. Werdykt (krótko)

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy |Cl|~2,5 / Cd~0,28 to sensowny rząd dla 2D 3-el. high-lift? | **Tak** (kotwica MECDC Cl≈2,81; Cd CFD#1 niższy przy łagodniejszych klapach — OK orientacyjnie). |
| Czy gap/overlap są „z księżyca”? | **Nie** — blisko McBeath/Jackson; f1→f2 lekko poza 4%/6%. |
| Czy wolno porównywać z RWiter017 / Jackson-pojazd? | **Nie** absolutów. |
| Czy niezależność siatki jest domknięta? | **Jeszcze nie** (coarse/fine pending). |
| Czy kierunek Δ kątów zgadza się z Staniszewskim? | **Do sprawdzenia** po A1/A2. |
| Czy coś idzie do TARGETS? | **Nie.** |

**Dla Spec / CFD#1:** medium baseline nadaje się jako **punkt startu serii 2D** (jak ustaliliście). Po A1/A2 — jedna aktualizacja tej notatki z tabelą Δ. Po coarse/fine — dopisać werdykt niezależności.

