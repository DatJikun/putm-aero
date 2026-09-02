# FS Aero — baza wiedzy (indeks)

Stan na 2026-09-01 (aktualizacje nocne do 2026-09-02).
Tu trzymamy źródła i zamrożone ustalenia zespołu.
Liczby tylko ze źródeł — bez zgadywania.

---

## Ustalenia zamrożone (zespół)

**Punkt odniesienia (baseline):** `RW_iter017` to **aktualny bolid** po zawodach.

- Osoba w arkuszu: Michał Narożny, status Done, data 27.12.2025.
- Cx = **1,229**
- Cz = **−3,682**
- Cm = **−0,429**
- efektywność ≈ **2,996**
- Źródło: [sources/team-rwiter017-baseline.md](sources/team-rwiter017-baseline.md) oraz CSV `team/rw-iters-2025-2026.csv`.
- Wariant `RW_iter017.2` służy tylko do kontroli rozbieżności skryptu Fluent. **Nie** zamienia kotwicy.
- `Baseline002` to historyczny miks (FWiter011 + RWiter017 + UTiter002). To **nie** jest kotwica.

**Cel projektowy (lead):** jak największy docisk przy balansie około **50/50** (roboczo **48–52%** na przód).
Przy tym samym docisku nie pogarszamy oporu względem baseline (orientacyjnie Cx ≲ **1,23**).
Prędkość odniesienia w pracach PUT i w setupie CFD: **15 m/s**.

**Zakres elementów (na start):**

- Skrzydło tylne, przednie, podłoga i sekcje boczne — **wchodzą**.
- Tylne skrzydło: rozważamy **4 elementy** jako kandydata względem obecnych 3.
- Wąsy (profil typu S1223) — **jeszcze nie wiadomo**; dobór profilu dopiero pod miejsce na aucie.
- Wentylator spod podłogi — **nie**.
- DRS ruchomy — **nie**; ewentualnie tylko układ **pasywny** (jak testy 019/020), poza ścieżką peak-docisku.
- Model turbulencji Fluent: **Realizable k-ε + Enhanced Wall Treatment**.
  OpenFOAM: to samo albo wall functions przy y+ > 30 (maszyna 16 GB).

**Priorytet eventów:** Endurance i Autocross.
Cel: maksymalny docisk przy możliwie niskim oporze.
Balans: z ok. **61,6%** na przód w stronę ok. **50/50** (ok. **12 punktów procentowych**).

**Potwierdzone:** wiersz `Baseline_1` z arkusza podłogi **nie jest** tym samym bolidem co `RW_iter017`.
RWiter017 = aktualny bolid po zawodach.
Liczb balansu ok. 69% z Baseline_1 nie używamy jako startu.

**Balans RWiter017:** ≈ **61,6%** na przód (z Cm/Cz arkusza; decyzja: „jak w arkuszu”).
Do ok. 50/50 brakuje ok. **12 pp** — cofamy docisk (tylnie skrzydło / podłoga), nie dokręcamy samego przodu.
Postprocessing z OneDrive to JPG bez CSV sił, więc kotwica z arkusza zostaje.

**Aref:**

- half-car ≈ **0,50 m²** (w simach bywa 0,49–0,51)
- pełny bolid ≈ **1,0 m²**

**Otwarte:**

- masa bolidu i budżet energii,
- wąsy — ostateczny dobór profilu.

Łańcuch iteracji przedniego skrzydła (`team/fw-iters-2025-2026.csv`) to kontekst rozwoju FW.
To **nie** jest baseline całego bolidu.

---

## Literatura (prace dyplomowe / paper)

| # | Plik | Krótko |
|---|------|--------|
| 1 | [sources/staniszewski-2023-wing.md](sources/staniszewski-2023-wing.md) | Staniszewski 2023 — optymalizacja 3-elementowego skrzydła tylnego (2D/3D, 15 m/s). Na pojeździe Cx/Cz ≈ 0,72 / −2,03 (inny pakiet niż dzisiejszy baseline). |
| 2 | [sources/staniszewski-2024-energy.md](sources/staniszewski-2024-energy.md) | Staniszewski 2024 — mapy Cx/Cz vs kąt skrętu i proxy energii; podłoga pomaga mimo +~10 kg. |
| 3 | [sources/naglowski-2024-package.md](sources/naglowski-2024-package.md) | Nagłowski 2024 — wąsy S1223; baza Cz=−4,071 / Cx=1,453 / balans ~60% przód @15 m/s (kotwica literaturowa, nie nasz hard target). |
| 4 | [sources/michalecki-fan-ground-effect.md](sources/michalecki-fan-ground-effect.md) | Michalecki — wentylator pod podłogą na PM08 nie bije bazy; stąd fan OUT. |
| 5 | [sources/jackson-2018-cfd-drs.md](sources/jackson-2018-cfd-drs.md) | Jackson 2018 — DRS na RW (literatura zewnętrzna). |
| 6 | [sources/strojny-2015-rp.md](sources/strojny-2015-rp.md) | Strojny 2015 — druk 3D w procesie budowy; bez liczb aero. |

Indeksy cząstkowe: [index-batch-a.md](index-batch-a.md), [index-batch-b.md](index-batch-b.md).

---

## Dane zespołu (CSV)

| Plik | Co to jest |
|------|------------|
| [sources/team-rwiter017-baseline.md](sources/team-rwiter017-baseline.md) | Claim baseline `RW_iter017` oraz uwagi o balansie |
| [team/rw-iters-2025-2026.csv](team/rw-iters-2025-2026.csv) | Arkusz iteracji skrzydła tylnego |
| [team/ut-iters-with-balance-2026.csv](team/ut-iters-with-balance-2026.csv) | Arkusz podłogi z kolumną balansu (`Baseline_1` ≈ 69% przód) |
| [team/fw-iters-2025-2026.csv](team/fw-iters-2025-2026.csv) | Arkusz iteracji skrzydła przedniego (kontekst) |

## Research (robocze)

| Plik | Opis |
|------|------|
| [sources/research-balance-shift.md](sources/research-balance-shift.md) | Cofanie balansu ~61,6% → 50/50; shortlista H1–H5 |
| [sources/research-aero-for-targets.md](sources/research-aero-for-targets.md) | Rady aero pod max docisk + niski opór + Endurance/Autocross (H1–H4) |
| [sources/research-overnight-rw-multi-element.md](sources/research-overnight-rw-multi-element.md) | Noc: multi-element RW 3 vs 4, kąty/gap/overlap, DRS pasywny vs aktywny (EU FS) |
| [sources/research-overnight-ut-yaw-balance.md](sources/research-overnight-ut-yaw-balance.md) | Noc: podłoga/dyfuzor → balans + yaw; Staniszewski 2024 + Chalmers/OSU/Jowsey |
| [sources/research-papers-rw-ut-yaw-clcd.md](sources/research-papers-rw-ut-yaw-clcd.md) | Zbiorcza notatka paperów: 3 vs 4 el. RW, UT+yaw, opublikowane Cl/Cd/balans |
| [OVERNIGHT-BRIEF.md](OVERNIGHT-BRIEF.md) | Brief na jedną stronę (rano): co znaleziono, luki, PDF do dropu |
| [sources/research-balance-levers-h1-h5.md](sources/research-balance-levers-h1-h5.md) | Szczegóły dźwigni H1–H5 (mechanizm, ryzyka, kryteria zabicia ścieżki) |
| [sources/research-fs-teams-practice.md](sources/research-fs-teams-practice.md) | Praktyka innych teamów FS (FW/RW/UT, Cl/Cd/balans, Endurance vs Autocross) |
| [sources/research-amz-berlin-snails-aero.md](sources/research-amz-berlin-snails-aero.md) | AMZ / FaSTTUBe (Berlin) / Running Snail — narzędzia, walidacja, publiczne ΔDF; absolutne Cl/Cd nie znalezione |
| [sources/research-overnight-h3-fw-unload-rw-gaps.md](sources/research-overnight-h3-fw-unload-rw-gaps.md) | Noc 2: H3 odciążenie FW + reguły gap/overlap/AOA na RW; checklist pod serię CFD |
| [sources/checklist-h1-2d-rw-gap-aoa.md](sources/checklist-h1-2d-rw-gap-aoa.md) | Checklist H1: seria 2D RW — gap/overlap/AOA (bez nowych Cl/Cd do TARGETS) |
| [sources/sanity-cfd1-2d-rw-vs-lit.md](sources/sanity-cfd1-2d-rw-vs-lit.md) | Sanity-check baseline 2D CFD#1 vs Staniszewski/Jackson/McBeath (rząd wielkości; bez TARGETS) |
| [sources/research-h2-undertray-balance-levers.md](sources/research-h2-undertray-balance-levers.md) | H2 podłoga: dźwignie balansu tył, ride height, yaw, checklista pomiarów CFD |
| [sources/research-eu-fs-ev-top-teams.md](sources/research-eu-fs-ev-top-teams.md) | Przegląd topowych teamów EU FS EV pod pakiet aero PUT |
| [sources/research-aero-dev-tooling.md](sources/research-aero-dev-tooling.md) | Jak teamy EU FS organizują rozwój aero: tooling, workflow i śledzenie iteracji CFD |

## Regulamin

| Plik | Opis |
|------|------|
| [sources/fs-rules-2026-t8.md](sources/fs-rules-2026-t8.md) | Claims + cytaty T8 / T2.2 / T11.11 z FS Rules **2026 v1.1** |
| [sources/rules-aero-boxes-loopholes.md](sources/rules-aero-boxes-loopholes.md) | Brief Aero Pack: boxy, DRS/fan, luki i ryzyko Scrutineering |
| [team/rules-current.pdf](team/rules-current.pdf) | PDF źródłowy |
| [sources/claims-from-eu-fs-ev-top.md](sources/claims-from-eu-fs-ev-top.md) | Claims do założeń z notatki EU EV |

- [SPEC-MORNING.md](SPEC-MORNING.md) — one-pager Spec na rano
- [SPEC-FROM-OVERNIGHT.md](SPEC-FROM-OVERNIGHT.md) — co nocny research zmienia w celach
- [TARGETS.md](TARGETS.md) — pełna karta celów
