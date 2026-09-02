# Deep dive H1: overlap / gap / AOA w serii 2D RW

**Status:** notatka badawcza dla Spec + CFD (2026-09-02 Europe/Warsaw)  
**Język:** PL, pełne zdania  
**Zasada:** liczby tylko z cytowanych źródeł lokalnych i opublikowanych. Nie inventujemy Cl/Cd. Nie wpisujemy Cl/Cd 2D do `TARGETS.md` ani na kartę `RW_iter017`.

**Kotwica pakietu (zamrożona, tylko jako limit później na aucie):**  
Cx = **1,229**  
|Cz| = **3,682**  
Cm = **−0,429**  
balans ≈ **61,6%** przód → cel ~**50/50**  
V CFD = **15 m/s**  
DRS OUT, fan OUT  
kolejność: **H1 RW → H2 floor → H3 FW unload**

**Źródła cytowane:**  
[checklist-h1-2d-rw-gap-aoa.md](checklist-h1-2d-rw-gap-aoa.md) · [research-overnight-h3-fw-unload-rw-gaps.md](research-overnight-h3-fw-unload-rw-gaps.md) · [staniszewski-2023-wing.md](staniszewski-2023-wing.md) · [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md) · [sanity-cfd1-2d-rw-vs-lit.md](sanity-cfd1-2d-rw-vs-lit.md) · `SPEC-H1-2D-GATE.md`

Mirror: `/workspace/fs-aero-kb/sources/research-h1-overlap-gap-deep-dive.md`

---

## 1. Kolejność sweepów i kroki (opublikowane liczby na osobnych liniach)

Checklista H1 i Staniszewski 2023 ustalają jedną kolejność. Nie mieszamy kątów, overlap i gap w jednym case.

### 1.1 Sweep 1 — kąty (najpierw)

Najpierw main, potem profile 2 i 3. To jest ten sam porządek co w pracy Staniszewskiego i w checklistie H1.

Kroki z Staniszewski 2023:

- krok main ≈ **1,5°**
- krok profili 2 i 3 ≈ **2,0°**
- baseline main u Staniszewskiego: **7,5°**

Opublikowane punkty 2D izolowanego RW (V = **15 m/s**, Tab. 3/4):

- baseline (MP 7,5°): Fx = **49,96 N**
- baseline (MP 7,5°): Fz = **−397,61 N**
- po −6,5° main: Fx = **27,83 N**
- po −6,5° main: Fz = **−502,43 N**

Wniosek z tekstu pracy: obniżanie kąta main względem 7,5° podnosi |Fz| i obniża Fx aż do ok. −6,5°. Dalsze −7,0° już pogarsza Fz. Zmiana kątów tylnych elementów (±2°) po optymalizacji main nie była korzystna względem ich baseline.

Zakresy AOA z McBeath (cyt. Jackson / checklista):

- Flap1 (high-DF 3-el.): ok. **25–30°**
- Flap2: ok. **30–70°**
- overall AOA trzymaj poniżej stall (~**25°** u Jackson)

Konkret Jackson 2018 (profil E423 — nie kopiować 1:1 na nasz S1223):

- Flap1 = **28°**
- Flap2 = **60°**
- overall AOA ≈ **22,81°** (Study 4)
- stall wskazany przy ~**25°**

CFD#1 (nasza seria 2D, sanity): baseline kąty **8° / 20° / 32°**. To są kąty łagodniejsze niż Study 4 Jacksona. Na starcie jest zapas przed stall overall ~25°.

### 1.2 Sweep 2 — overlap (po kątach)

Krok z Staniszewskiego:

- overlap krok **10 mm**

Opublikowane optimum 2D (iter003.5):

- overlap = **−30 mm** względem ich baseline
- Fx = **27,11 N**
- Fz = **−565,03 N** (najwyższy |Fz| w tabeli 2D)

Przy **−40 mm** Fz już spada — nie idź w ciemno dalej w stronę większego odsłonięcia.

Zakresy McBeath / Craig (cyt. overnight H3):

- overlap: **1–6%** cięciwy poprzedniego elementu
- praktyka Craig: overlap ~**1,5%** c
- peak CFD Craig: overlap ~**1,2–2%** c
- overlap **2,6%** → obniżony lift (Craig)

Jackson 2018 (E423, main 540 mm):

- overlap = **26,25 mm**
- to ≈ **4,9%** c_main

CFD#1 baseline (sanity):

- overlap main→flap1 ≈ **12,0 mm** (~**3,9%** c_main)
- overlap flap1→flap2 ≈ **12,4 mm** (~**6,5%** c_f1)

Druga szczelina overlap f1→f2 siedzi lekko powyżej pasma McBeath 1–6%. W serii O1/O2 (checklista / SERIES) warto iść w stronę mniejszego overlap (kierunek Staniszewski −30 mm), a nie tylko „wracać do %c”.

### 1.3 Sweep 3 — gap (po overlap)

Kroki z Staniszewskiego:

- gap kroki **5–20 mm**
- drobne **+5 / +10 mm** (iter004.5)

Opublikowane iter004.5:

- Fx = **26,98 N**
- Fz = **−559,80 N**

To trzyma wysoki docisk przy niskim oporze względem ich serii kątów/overlap.

Zakresy McBeath / Craig:

- gap: **1–4%** cięciwy poprzedniego elementu
- praktyczny cel ~**2%** c (Craig „rekomendowany”)
- peak CFD Craig: gap ≈ **1,6%** c
- finalny wybór Craig: gap **2%** + overlap **1,5%** (żeby ugięcie nie zamykało szczeliny)

Jackson 2018:

- gap = **20 mm**
- to ≈ **3,7%** c_main

CFD#1 baseline:

- gap main→flap1 ≈ **11,0 mm** (~**3,5%** c_main) — w paśmie 1–4%
- gap flap1→flap2 ≈ **9,6 mm** (~**5,1%** c_f1) — lekko powyżej 4%

Apostolidis (BETA, jakość dla RW też): zmniejszanie gap ↑ DF aż warstwy się zlejają → ryzyko stall na przednim elemencie; za duży gap → utrata efektu klapy. Dla FW u nich przy gap **> 25 mm** efekt klapy zanika. To nie jest mm-recepta na nasze RW, tylko kierunek: nie schodzić w „paper-thin” i nie otwierać szczeliny w nieskończoność.

Hokkanen / McBeath: **convergent slot** bywa ważniejszy niż ślepy procent. Przy CAD pilnuj kształtu szczeliny, nie tylko %c.

### 1.4 Sweep 4 — opcjonalnie 1× 4-el.

Dopiero po zbieżnym 3-el. (kąty + overlap + gap). Jedno porównanie, nie default Spec. W KB brak opublikowanych Cl/Cd 4-el. dla naszego auta — nie inventujemy.

### 1.5 Co zapisać z każdego runu (checklista)

- gap mm i %c poprzedniego elementu  
- overlap mm i %c  
- AOA main + flaps  
- Fx, Fz (osobne linie) albo Cl, Cd (osobne linie)  
- czy stall / zlepanie warstw (jakościowo z Cp)  
- cells, residua (okno last-200)

Ten sam V_ref / gęstość / znaki sił co w workflow (15 m/s jeśli tak w Fluent / OpenFOAM).

---

## 2. Jakie Δ jest czytelne wobec ~8% szumu Cl z meshu

To rozdział o **szumie numerycznym** serii CFD#1. Nie służy do przepisywania absolutów na auto.

### 2.1 Skąd bierze się ~8%

Z raportu niezależności siatki CFD#1 (sanity §6.1), okno t = 1810–2000:

- coarse ≈ 201k: Cl = **−2,93**, Cd = **0,49**
- medium ≈ 408k: Cl = **−2,53**, Cd = **0,28**
- fine ≈ 827k: Cl = **−2,72**, Cd = **0,095**

Δ względem medium:

- coarse → medium: ΔCl ≈ **+16%**, ΔCd ≈ **−44%**
- medium → fine: ΔCl ≈ **−8%**, ΔCd ≈ **−66%**

Werdykt sanity: pełnej niezależności siatki nie ma. Cl skacze o ~**8%** medium→fine — powyżej roboczego progu ~2–3% pod „pewne” trendy. Cd nie zbiega z gęstością; fine Cd ≈ 0,10 jest podejrzanie niski i **nie** jest kotwicą fizyczną.

Medium zostaje wspólną siatką do **rankingu Δ** przy identycznym przepisie. Nie jest absolutem „jak w tunelu”.

### 2.2 Co wolno uznać za sygnał, a co za szum

Reguła Spec (`SPEC-H1-2D-GATE.md`) + sanity:

- decyzja kąta / overlap / gap tylko gdy |ΔCl| jest **wyraźnie większe** niż szum meshu (~**8%** Cl medium→fine) **albo** gdy trend Cd / jakościowy Cp jest czytelny i powtarzalny na ≥2 sąsiednich punktach;
- pojedynczy wyskok Cl poniżej szumu **nie** idzie do CAD;
- ΔCd bywa czytelniejsze niż ΔCl na medium (patrz A1 / A1b poniżej) — ale sam Cd bez sensownego docisku też nie wygrywa case’u.

Opublikowane Δ z serii kątów CFD#1 na medium (sanity §6.5; baseline Cl ≈ −2,53 / Cd ≈ 0,28):

| case | main | ΔCl vs base | ΔCd vs base |
|------|------|-------------|-------------|
| A1 | 6,5° | ≈ **−1%** | ≈ **−11%** |
| A1b | 3,5° | ≈ **−0,9%** | ≈ **−33%** |
| A1c | 1° | ≈ **−3,7%** | ≈ **−32%** |
| A2 | 9,5° | ≈ **−3,7%** | ≈ **+21%** |
| A2b | 12,5° | ≈ **−1,4%** | ≈ **+52%** |

Wszystkie |ΔCl| są **≪ ~8%** szumu meshu. Z Cl **nie** wyciągamy decyzji kąta na medium. Czytelne są głównie skoki Cd (A1/A1b w dół; A2/A2b w górę).

A1c: Cd praktycznie jak A1b (−32% vs −33%). Dalsze obniżanie main nie tnie już oporu. To pasuje do Staniszewskiego: jest optimum kąta main, poniżej którego zysk się wypłaszcza / psuje.

### 2.3 Co to znaczy dla overlap i gap

Na medium (przed zamknięciem bramki medium+) oczekuj, że drobne kroki overlap ±10 mm i gap +5/+10 mm dadzą |ΔCl| często **poniżej** 8%. Wtedy:

- rankingujemy **kierunek** (Cd, Cl/Cd, Cp w szczelinie), nie absolut Cl;
- nie zamrażamy geometrii CAD na podstawie jednego punktu z |ΔCl| < szum;
- po otwarciu bramki **medium+** (cel Spec: |ΔCl| med→med+ ≪ 8%, bez izotropowego MESH_SCALE=0.707) powtarzamy najlepsze 1–2 punkty overlap/gap na nowej siatce i dopiero wtedy wybieramy kierunek do 3D.

Porównanie absolutów 2D CFD#1 z 2D Staniszewskiego (Fz ≈ −198 N/m vs Fz baseline −397,61 N) **nie** jest fail: inne profile, kąty i cięciwy. Porównujemy kierunki trendów, nie „czy −198 = −398”.

Absolutów 2D **nie** porównujemy z Jackson-pojazd (CL_DF **1,15** / CD **1,21**) ani z RWiter017 (Cx **1,229** / |Cz| **3,682**).

---

## 3. Kryteria kill (Cd spike / stall jak A2b)

Kill działa na dwóch poziomach: seria 2D H1 oraz później pakiet na aucie.

### 3.1 Kill w serii 2D (Spec gate + sanity)

Z `SPEC-H1-2D-GATE.md` punkt 6: jeśli |ΔCd| rośnie mocniej niż zysk docisku bez uzasadnienia (stall / oscylacje) — punkt odpada mimo ładnego Cl.

Przykład A2 → A2b (sanity / SERIES):

- A2 (main 9,5°): ΔCd ≈ **+21%**, |ΔCl| ≈ 3,7% (w szumie)
- A2b (main 12,5°): ΔCd ≈ **+52%**, ΔCl ≈ **−1,4%**

Cd mocno w górę bez sensownego zysku docisku = obraz drogi w stronę stall / złego AOA. To jest spójne z ostrzeżeniem Jacksona: nie pchać overall AOA w stall (~**25°**).

Praktyczne kill 2D (pełne zdania, do logu runu):

1. **Cd spike bez |Cl|:** ΔCd ≫ 0 przy |ΔCl| w szumie meshu albo spadku |Cl| → stop kierunku (jak A2b).  
2. **Overall AOA → stall:** nie wchodź w okolice ~**25°** overall (Jackson); Study 4 trzyma ≈ **22,81°**.  
3. **Overlap poza optimum:** u Staniszewskiego −40 mm już pogarsza Fz — nie ciągnij dalej „bo −30 było dobre”.  
4. **Gap za mały / za duży:** zlepanie BL (Cp / wizualizacja) albo utrata efektu klapy (Apostolidis: FW > **25 mm** gubi flap effect — orientacja jakościowa).  
5. **Zbieżność:** residua / oscylacje Cl-Cd bez plateau last-200 → punkt „nieużywać”, nie do rankingu.  
6. **Trend jednopunktowy:** wybór tylko gdy kierunek powtarza się na ≥2 sąsiednich punktach sweepu (gate Spec).

### 3.2 Kill na aucie (po H1 2D → Fluent 3D)

Z checklisty H1 / Spec:

- nie pogarszaj |Fz| względem najlepszej 2D z serii bez powodu;
- na aucie spadek |Cz| poniżej **3,682** względem RWiter017 oznacza stop;
- Cx trzymaj w okolicy **1,23** (cel Spec overnight);
- nie odpalać H3 (unload FW) przed H1 + H2;
- nie wpisywać Cl/Cd z Jackson / MECDC / cudzych teamów do `TARGETS.md`.

MECDC 2014 (kotwica rzędu wielkości 2D, nie target):

- Cl = **2,81**
- Cd = **0,81**
- slot gap **3,6%** c, overlap **0,75%**

CFD#1 |Cl| ≈ **2,52** siedzi w tym samym rzędzie. To nie jest pozwolenie na kopiowanie Cd 0,81 ani Cl 2,81 na nasze skrzydło.

---

## 4. Czego nie znaleziono (gaps)

Status z overnight H3 + sanity + publiczne abstrakty. Brak = **nie znaleziono** / nie inventować.

| Brak | Status |
|------|--------|
| Opublikowane Cl/Cd **RWiter017** / PUT 2026 po H1 gap-overlap | nie istnieją publicznie |
| Tabela ΔCl/ΔCd overlap/gap dla geometrii CFD#1 (S1223 310/190/130) vs Staniszewski 1:1 | **nie znaleziono** (inne profile; tylko kierunki) |
| Walidacja tunelowa gap RW dla geometrii Staniszewskiego 2023 | brak w pracy |
| Pełne mm slot gap z tezy Peterson (Oregon State) | proprietary / abstrakt only |
| Pełna tabela gap/overlap z LUT Metropolia HPF026 | **nie znaleziono** w publicznym abstrakcie |
| MECDC 2014 full PDF w sesji overnight | liczby ze snippeta; PDF **not fetched** |
| Bezpośredni paper „overlap X mm → ΔCz Y na FS half-car @ 15 m/s” dla auta jak 017 | **nie znaleziono** |
| Opublikowane FW = **588 N** (wątek H3, nie H1) | **nie znaleziono** |
| Pełny PDF EngProc 2025 (MDPI CDN) | PDF **not fetched** w sesji overnight |
| Potwierdzenie niezależności siatki CFD#1 (Cd fine) | wynik **negatywny**; medium+ w toku |
| Cl/Cd 4-el. dla naszego pakietu | **nie znaleziono** — tylko 1 case porównawczy planowany |

Nie wypełniamy tych luk domysłami.

---

## 5. Krótka checklista Spec — po otwarciu bramki medium+

Bramka medium+ otwiera się, gdy porównanie medium ↔ medium+ spełnia cel Spec: |ΔCl| med→med+ ≪ **8%**, Cd last-200 ma plateau, y+ ścian ~**25–40** (wall-fn), bez artefaktu fine Cd. Do tego czasu medium służy tylko do diagnostyki kierunku (Cd spike / stall path), nie do zamrażania CAD.

Gdy bramka jest zielona, Spec robi po kolei:

1. **Zamroź przepis siatki medium+** (ten sam BC, V = 15 m/s, Aref/Lref 2D, last-200). Baseline na medium+ policzony i zapisany.  
2. **Dokończ kąty na medium+** — powtórz A1 (kierunek Staniszewski: main w dół) i odrzuć ścieżkę A2b (Cd↑). Flapy ±2° dopiero po zbieżnym main. Nie wchodź w overall ~25°.  
3. **Overlap ±10 mm** względem baseline CFD#1; celuj w stronę mniejszego overlap (orientacja Staniszewski −30 mm). Stop przed reżimem −40 mm / zanim Fz spadnie. Zapisz mm i %c.  
4. **Gap +5 / +10 mm** po overlap. Szukaj utrzymania |Cl| bez Cd spike. Pilnuj convergent slot i ugięcia (Craig + T8).  
5. **Decyzja kierunku** tylko gdy Δ spełnia `SPEC-H1-2D-GATE.md` (ten sam setup, Δ vs baseline, zbieżność, powtórka, trend ≥2 punktów, kill Cd).  
6. **Jedno porównanie 4-el.** najwyżej — nie default.  
7. **Na auto (Fluent):** te same kierunki geometrii; metryki z karty — |Cz| ≥ **3,682**, Cx ≈ **1,23**, balans w stronę 50/50. Cl/Cd 2D **nie** lądują w TARGETS.  
8. **Log per run:** nazwa, mm/°, Cl, Cd (osobne linie), stall/Cp, cells. DRS/fan OUT.

Kolejka pakietu zostaje: **H1 → H2 → H3**. H3 tylko gdy H1+H2 nie domykają balansu.

---

## 6. Claims (skrót)

| claim | evidence | confidence |
|-------|----------|------------|
| Kolejność H1 2D: kąty → overlap → gap → opcjonalnie 4-el. | checklista H1; Staniszewski 2023 | **high** |
| Main ↓ (do ~−6,5° u Staniszewskiego) ↑ \|Fz\| i ↓ Fx w 2D | Tab. 3/4: −502,43 N / 27,83 N | **high** (2D izolowane) |
| Overlap −30 mm → max \|Fz\| 2D (−565,03 N); −40 mm gorzej | Tab. 3/4 iter003.5 | **high** (ich geometria) |
| Gap +5/+10 mm trzyma wysoki DF (Fz −559,80 N) | iter004.5 | **high** (ich geometria) |
| McBeath gap 1–4%c / overlap 1–6%c; cel ~2%c / ~1,5%c | Jackson; Craig; overnight H3 | **high** |
| Jackson Study 4: gap 20 mm, overlap 26,25 mm, flaps 28°/60°, overall 22,81°, stall ~25° | jackson-2018 | **high** |
| CFD#1 \|Cl\|~2,5 w rzędzie MECDC Cl 2,81; gap/overlap blisko McBeath | sanity | **med–high** (rząd, nie target) |
| Szum Cl medium→fine ~8%; Cd fine niezbieżny | sanity §6.1 | **high** (ten pipeline) |
| A2b: ΔCd +52% bez zysku Cl = kill / stall path | sanity §6.5; SERIES | **high** (ten pipeline) |
| \|ΔCl\| A1…A2b ≪ 8% → brak decyzji kąta z Cl na medium | sanity | **high** |
| Cl/Cd 2D → TARGETS / RWiter017 | zakaz Spec | **high** (decyzja) |

---

**Koniec notatki.** Nie robić git push z tej sesji.
