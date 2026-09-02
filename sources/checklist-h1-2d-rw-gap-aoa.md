# Checklist H1 — seria 2D RW (gap / overlap / AOA)

**Dla kogo:** Spec + CFD (2D izolowane RW przed 3D na aucie).  
**Zasada:** to punkt startu i kroki z literatury PUT / Jackson / McBeath — **nie** nowe targety Cx/Cz. Baseline RWiter017 bez zmian.  
**Źródła lokalne:** [staniszewski-2023-wing.md](staniszewski-2023-wing.md), [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md), [research-overnight-h3-fw-unload-rw-gaps.md](research-overnight-h3-fw-unload-rw-gaps.md).

---

## 0. Zanim ruszysz

- Geometria: 3 elementy (domyślna ścieżka Spec); 4-el. tylko **jedna** porównawcza.
- Ten sam V_ref / gęstość / znaki sił co w Fluent (15 m/s jeśli tak w workflow).
- Zapisz gap i overlap w **mm** i w **% cięciwy** poprzedniego elementu.
- Kill: nie pogarszaj |Fz| względem najlepszej 2D z serii bez powodu; na aucie |Cz| ≲ 3,682 vs RWiter017 = stop (per Spec).

---

## 1. Zakresy startowe (McBeath, cyt. w Jackson / Craig)

- gap: **1–4%** c (praktycznie celuj w ~**2%** c)
- overlap: **1–6%** c (praktyka Craig ~**1,5%** c; peak CFD Craig ~**1,2–2%** c)
- Flap1 AOA (high-DF 3-el.): ok. **25–30°**
- Flap2 AOA: ok. **30–70°**
- Overall AOA: trzymaj poniżej stall (~**25°** u Jackson; Study 4 ≈ **22,81°**)

Konkret Jackson (E423, nie kopiować 1:1 na nasz profil):

- gap = **20 mm**
- overlap = **26,25 mm**
- Flap1 / Flap2 = **28° / 60°**

---

## 2. Kolejność sweepów 2D (Staniszewski 2023)

1. **Kąty** — najpierw main (kroki ~**1,5°**), potem profile 2 i 3 (~**2,0°**).
2. **Overlap** — krok **10 mm** (u Staniszewskiego optimum 2D przy overlap **−30 mm**:  
   - Fx = **27,11 N**  
   - Fz = **−565,03 N**  
   Przy **−40 mm** Fz już spada — nie idź w ciemno dalej.
3. **Gap** — kroki **5–20 mm**; drobne **+5 / +10 mm** (iter004.5) trzymało wysoki docisk:  
   - Fx = **26,98 N**  
   - Fz = **−559,80 N**
4. Dopiero potem opcjonalnie **1×** wariant 4-el. (porównanie, nie default).

---

## 3. Co zapisać z każdego runu

- gap mm / %c  
- overlap mm / %c  
- AOA main + flaps  
- Fx, Fz (osobne linie)  
- czy stall / zlepanie warstw (jakościowo z Cp)

---

## 4. Czego nie robić

- Nie wpisywać Cl/Cd z Jackson / MECDC / cudzych teamów do `TARGETS.md`.
- Nie odpalać H3 (unload FW) przed H1 + H2.
- Nie porównywać smoke half-car OpenFOAM z RWiter017, dopóki geometria jest dziurawa.

