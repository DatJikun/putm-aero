# FS Aero — baza wiedzy (indeks)

Stan na 2026-09-01. Tu trzymamy źródła i zamrożone ustalenia zespołu. Liczby tylko ze źródeł — bez zgadywania.

---

## Ustalenia zamrożone (zespół)

**Punkt odniesienia (baseline):** `RW_iter017` = **aktualny bolid** po zawodach  
- osoba: Michał Narożny, status Done, data 27.12.2025  
- Cx = **1,229**, Cz = **−3,682**, Cm = **−0,429**, efektywność ≈ **2,996**  
- źródło: [sources/team-rwiter017-baseline.md](sources/team-rwiter017-baseline.md), CSV `team/rw-iters-2025-2026.csv`  
- wariant `RW_iter017.2` — tylko kontrola rozbieżności skryptu, nie zamienia kotwicy  
- `Baseline002` = historyczny miks (FWiter011+RWiter017+UTiter002), **nie** kotwica

**Cel projektowy (lead):** jak największy docisk przy balansie około **50/50** (roboczo **48–52%** na przód).  
Przy tym samym docisku nie pogarszać oporu względem baseline (orientacyjnie Cx ≲ **1,23**).  
Prędkość odniesienia w pracach PUT i w setupie CFD: **15 m/s** (do potwierdzenia na karcie Spec).

**Zakres elementów (na start):**
- skrzydło tylne, przednie, podłoga i sekcje boczne — **wchodzą**
- tylne skrzydło: rozważamy **4 elementy** (kandydat vs obecne 3)
- wąsy S1223 — **jeszcze nie wiadomo** (dobór profilu pod miejsce na aucie)
- wentylator spod podłogi — **nie**
- DRS ruchomy — **nie**; ewentualnie tylko **pasywny** (jak testy 019/020)
- model turbulencji Fluent: **Realizable k-ε + EWT**; OF: to samo / wall functions y+>30 (16 GB)

**Priorytet eventów:** Endurance + Autocross. Cel: maksymalny docisk przy możliwie niskim **oporze**. Balans z ~61,6% przód w stronę ~50/50 (~12 pp).

**Potwierdzone:** wiersz `Baseline_1` z arkusza podłogi **nie jest** tym samym bolidem co `RW_iter017`. RWiter017 = aktualny bolid po zawodach. Liczb balansu ~69% z Baseline_1 nie używamy jako startu.

**Balans RWiter017:** ≈ **61,6% przód** (z Cm/Cz arkusza; Mikołaj: „jak w arkuszu”). Do ~50/50 ≈ **12 pp** — cofamy docisk (RW/UT). Postpro z OneDrive = JPG bez CSV sił → kotwica z arkusza zostaje.

**Otwarte:**
- masa bolidu, budżet energii
- decyzja DRS z regulaminu

Łańcuch iteracji przedniego skrzydła (`team/fw-iters-2025-2026.csv`) to kontekst rozwoju FW, **nie** baseline całego bolidu.

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
| [sources/team-rwiter017-baseline.md](sources/team-rwiter017-baseline.md) | Claim baseline `RW_iter017` + uwagi o balansie |
| [team/rw-iters-2025-2026.csv](team/rw-iters-2025-2026.csv) | Arkusz iteracji skrzydła tylnego |
| [team/ut-iters-with-balance-2026.csv](team/ut-iters-with-balance-2026.csv) | Arkusz podłogi z kolumną balansu (`Baseline_1` ≈ 69% przód) |
| [team/fw-iters-2025-2026.csv](team/fw-iters-2025-2026.csv) | Arkusz iteracji skrzydła przedniego (kontekst) |

## Research (robocze)

| Plik | Opis |
|------|------|
| [sources/research-balance-shift.md](sources/research-balance-shift.md) | Cofanie balansu przy \|Cz\|≥3,682 i Cx≈1,23: RW+UT główne, wąsy kandydat, DRS na końcu; szacunek balansu 017 z Cm/Cz ≈61,7% (do potwierdzenia Fluent) |
| [sources/research-fs-teams-practice.md](sources/research-fs-teams-practice.md) | Praktyka FS z literatury (Jackson/Nagłowski/Staniszewski): zakresy Cx/Cz/balans, udział FW/RW/UT, Endurance vs Autocross (yaw UT), implikacje H1→H2 |
| [sources/research-balance-levers-h1-h5.md](sources/research-balance-levers-h1-h5.md) | Dźwignie balansu H1–H5 dla Spec: mechanizm, kierunek DF/drag/balans, evidence, ryzyka T8/yaw, pierwszy CFD, kill criteria (DRS OUT; 4-el. RW = hipoteza) |

## Regulamin

| Plik | Opis |
|------|------|
| [sources/fs-rules-2026-t8.md](sources/fs-rules-2026-t8.md) | Claims + cytaty T8 / T2.2 / T11.11 z FS Rules **2026 v1.1** |
| [sources/rules-aero-boxes-loopholes.md](sources/rules-aero-boxes-loopholes.md) | Brief Aero Pack: boxy, DRS/fan, loophole’y i ryzyko Scrutineering |
| [team/rules-current.pdf](team/rules-current.pdf) | PDF źródłowy |
