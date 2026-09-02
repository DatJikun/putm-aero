# Checklist H1 — seria tylnego skrzydła w Fluent (kąty → overlap → gap)

**Status:** 2026-09-02 — OpenFOAM 2D w pokoju **stop**; dalsza seria H1 idzie u Was w Fluent.  
**Zasada:** kolejność i kille z literatury / notatek H1. **Nie** wklejamy cudzych Cl/Cd do `TARGETS.md`. Baseline auta zostaje RWiter017.

Źródła: [checklist-h1-2d-rw-gap-aoa.md](checklist-h1-2d-rw-gap-aoa.md) · [research-h1-overlap-gap-deep-dive.md](research-h1-overlap-gap-deep-dive.md) · [staniszewski-2023-wing.md](staniszewski-2023-wing.md) · [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md) · [sanity-cfd1-2d-rw-vs-lit.md](sanity-cfd1-2d-rw-vs-lit.md) §6.8–6.9.

---

## 0. Zanim ruszysz geometrię

- Ten sam przepis ściany / y+ w całej serii (u Was: jak w Fluent workflow — EWT / y+ w sensownym paśmie wall treatment).  
- Nie mieszaj przepisów meshu między wariantami „porównawczymi”.  
- Raportuj **Δ** Cx/Cz/Cm/balans vs RWiter017 (albo vs ustalony baseline RW na aucie), nie absolutów z paperów.  
- Guard Spec: |Cz| nie poniżej kotwicy **3,682**; Cx orientacyjnie ≲ **1,23**; balans w stronę ~50/50.

---

## 1. Kolejność (obowiązkowa)

1. **Kąty** — najpierw main, potem klapy (kroki jak Staniszewski: main ok. **1,5°**, klapy ok. **2°**).  
2. **Overlap** — krok ok. **10 mm** (u Staniszewskiego 2D peak ok. **−30 mm** vs ich baseline; **−40 mm** już gorsze Fz).  
3. **Gap** — drobno **+5 / +10 mm** po dobrym overlap.  
4. Opcjonalnie **jedno** porównanie 4-el. — nie default; **bez** porównywania absolutów 3 vs 4.

McBeath (start slotów): gap **1–4%** c, overlap **1–6%** c.

---

## 2. Kill — stall / zły AOA

Odrzuć wariant (nie do CAD), gdy:

- Cd / Cx **ostro w górę** bez zysku docisku (wzorzec A2/A2b z diagnostyki OF: Cd +21% / +52%),  
- klapy / overall AOA wchodzą w rejon stall (u Jacksona ostrzeżenie ~**25°** overall — u Was inne profile, ten sam ostrzegacz),  
- overlap za daleko w minus i |Fz|/|Cz| spada,  
- gap wychodzi poza sensowny zakres i znika efekt klapy.

Jackson Study 4 (kontekst, nie target): flaps **28° / 60°**, overall ≈ **22,8°**.

---

## 3. Co zapisać z runu

- kąty main + flaps  
- gap mm i %c, overlap mm i %c  
- Cx, Cz, Cm, balans % (osobne linie)  
- krótko: stall / separacja (Cp)

---

## 4. Czego nie robić

- Nie brać Cl/Cd z izolowanego 2D OF ani ze Staniszewskiego jako liczb na kartę auta.  
- Staniszewski = **literatura / kierunek**, nie „wasze stare Fluent 2D”.  
- Nie otwierać H3 (unload FW), dopóki H1+H2 nie są na stole.
