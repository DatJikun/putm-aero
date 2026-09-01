# Research: cofanie balansu przy |Cz| ≥ 3,682 i Cx ≈ 1,23

**Status:** notatka robocza do repo (Spec 2026-09-01)

**Kotwica:** `RW_iter017` — Cx **1,229** / Cz **−3,682** / Cm **−0,429** @ **15 m/s**

**Cel:** max docisk, spokojny opór, balans jak najbliżej **50/50** (pasmo 48–52% przód)

**Zasada:** nie dokręcać samego przedniego skrzydła na ślepo. Główne dźwignie: **tylnie skrzydło + podłoga**. Wąsy = TBD. Ruchomy DRS = OUT; pasywny osobno.

Metryka porównawcza (CFD#1): moment przy **x = 0,765 m**, Lref **1,53 m**, half-car — tak samo w Fluent i później w OpenFOAM.

---

## 0. Najpierw: ile pp brakuje do 50/50?

W arkuszu **RW** nie ma kolumny balansu dla RWiter017. Trzeba ją **policzyć z Fluenta** (ten sam podział przód/tył co w Excelu).

### Orientacja z Cm i Cz (nie zastępuje pomiaru)

Formuły z arkusza Baseline zespołu:

- `CzA_F = Cz/2 + Cm`
- `CzA_R = Cz/2 − Cm`
- `Balans Front = CzA_F / Cz`  (= `1/2 + Cm/Cz`)

Dla RWiter017 przy **ujemnym** Cz (jak w sheetcie RW):

| Wielkość | Wartość |
|----------|---------|
| Cm/Cz | (−0,429)/(−3,682) ≈ 0,1165 |
| **Balans Front** | **≈ 61,6%** |

**Zamrożone 2026-09-01** (Mikołaj: „jak w arkuszu” + Spec/Koordynator). Folder postpro z OneDrive ma tylko JPG (Cp/WSS/y+) — **bez CSV sił**, więc kotwica zostaje z Cm/Cz. Gap do 50/50 ≈ **12 pp**.

**Nie używać** ~69% z Baseline002 / Baseline_1 jako startu dla 017 (inne modele).

---

## 1. Główna dźwignia A — tylnie skrzydło (RW)

**Źródło:** Staniszewski 2023 (izolowane RW 2D + weryfikacja 3D na pojeździe).

Co wiadomo z tekstu:

- Przy 15 m/s, 3 elementy: obniżanie kąta main i overlap do ok. **−30 mm** podnosi |Fz| 2D z ~398 N do ~**560–565 N**; overlap −40 mm już pogarsza.
- Na **całym pojeździe** Cx/Cz prawie stoją w miejscu (~0,72 / −2,03 na *ich* pakiecie) — autor ostrzega przed niepewnością CFD i **sprzężeniem** RW z body / elementem boczno-przypodłogowym.
- Wniosek do nas: RW to właściwe miejsce na **więcej docisku z tyłu**, ale iteracje muszą iść **na pakiecie**, nie tylko na kaskadzie 2D.

**Hipotezy do sprawdzenia na RWiter017 (kolejność):**

1. Delikatnie zwiększyć udział tylnych elementów / overlap w stronę optimum Staniszewskiego — pilnować Cx ≲ 1,23 i |Cz| ≥ 3,682.
2. Nie przenosić ślepo optimum 2D na auto (lekcja coupling z 2023).
3. Każda iteracja: Cx, Cz, Cm, **balans %** przy x=0,765 m.

Pewność literaturowa co do kierunku „więcej RW → więcej tyłu”: **średnia–wysoka** (fizyka oczywista; liczby 2D nie przenoszą się 1:1).

---

## 2. Główna dźwignia B — podłoga (UT)

**Źródła:** Staniszewski 2024 (mapy Cx/Cz vs kąt skrętu + proxy energii); Nagłowski 2024 (udział Fz_ut w pakiecie).

Co wiadomo:

- Staniszewski 2024: pełny pakiet z UT vs samo FW&RW → ok. **−2,7%** średniej siły hamującej (proxy energii) mimo **+~10 kg**; podłoga mocno reaguje na kąt skrętu.
- Nagłowski: w baseline Fz_ut rzędu **−200 N** przy Fz_all ≈ −561 N — UT to duży kawałek docisku, często „tylny”.

**Hipotezy:**

1. Szukać przyrostu docisku **podłogi / dyfuzora z tyłu** (nie dokładać nosa).
2. Gate przed zamrożeniem geometrii UT: mapa Cx/Cz vs δ + model toru (jak w założeniach Spec) — bo sam Cx@δ=0 kłamie przy UT.
3. Pilnować masy (+kg za energię tylko jeśli proxy to zwraca).

Pewność kierunku „UT → dźwignia balansu / energii”: **wysoka** w literaturze PUT; wielkość kroku na *naszym* 017: **do zmierzenia**.

---

## 3. Kandydat — wąsy (Selig S1223)

**Źródło:** Nagłowski 2024.

- Baseline: balans **60,3%** przód; najlepsza iter111.4: **57,3%** — wąsy **cofały** balans o kilka pp, wspierały RW/UT, lekko psuły L/D (efektywność −2,802 → −2,770).
- Blisko FW wąs **kradnie** powietrze spod przedniego skrzydła.
- Same wąsy bywają nośne (Fz_whiskers > 0) — nie traktować ich jako generatora docisku.

**Rola u nas:** dopiero po RW+UT; świadomy trade-off kilku pp balansu vs Cx/L/D. Nie baseline.

---

## 4. Na końcu — DRS (po regulaminie)

**Źródła:** Jackson 2018; własne `RW_iter019` / `020` (pasywne DRS na bazie 017).

- Jackson: zamknięte → dużo DF i drag; otwarte → CD spada mocno, DF też.
- Wasze 019/020: Cx spada do **~0,83**, |Cz| do **~3,01** — czyli **mniej** docisku niż kotwica 3,68. Przy celu |Cz| ≥ 3,682 DRS open **nie** jest narzędziem do trzymania peak DF; to narzędzie prostych / oporu, jeśli regulamin pozwoli.

DRS nie rozwiązuje problemu „za dużo z przodu przy high-DF”. Najpierw regulamin, potem osobna gałąź.

---

## 5. Czego nie robić

- Nie dokręcać samego FW, żeby „dogonić docisk” — pcha balans jeszcze bardziej na przód.
- Nie mieszać liczb Nagłowskiego (Cz≈−4,07) / PM08 (Cz≈−2) z RWiter017 bez wspólnego Aref/modelu.
- Nie brać balansu z Baseline002 / Baseline_1 jako balansu 017.
- Nie optymalizować izolowanego RW w 2D i wklejać na auto bez checku pakietu (Staniszewski 2023).

---

## 6. Plan pracy (propozycja KB)

| # | Krok | Kto | Done gdy |
|---|------|-----|----------|
| 1 | Fluent postpro: balans % RWiter017 przy x=0,765 m (oraz potwierdzenie szacunku ~61,7% z Cm/Cz) | zespół / CFD Fluent | jest % i pp do 50/50 |
| 2 | Seria RW na pakiecie 017: kąty/overlap/gap pod więcej tyłu, guardrale \|Cz\|≥3,682, Cx≲1,23 | CAD + Fluent | tabela Δbalans / ΔCx / ΔCz |
| 3 | Seria UT (dyfuzor / uszczelnienie tyłu), potem gate Cx(δ)+tor | CAD + Fluent | j.w. + nota energii |
| 4 | Opcjonalnie wąsy (Nagłowski-style), jeśli po 2–3 nadal za dużo z przodu | CAD + Fluent | trade-off pp vs L/D |
| 5 | DRS tylko po decyzji regulaminowej | Spec + lead | IN/OUT |

OpenFOAM (CFD#1) wchodzi, gdy będzie CAD 017 — te same BC i moment, model docelowy **k-ω SST**.

---

## Claims (skrót)

| claim | evidence | confidence |
|-------|----------|------------|
| Główne dźwignie cofania balansu = RW + UT, nie samo FW | Spec + fizyka pakietu; Staniszewski 2023/2024 | **high** (kierunek) |
| Balans 017 ≈ **61,6%** przód (kotwica robocza) | wzór Excel + Cm/Cz RW_iter017 + decyzja zespołu; postpro bez CSV | **high** (roboczo); **med** vs pełny raport Fluent |
| Wąsy cofają balans o kilka pp przy lekkim koszcie L/D | Nagłowski Tab. 5.2 (60,3→57,3%) | **high** na ich aucie; **low–med** transfer |
| Optimum overlap RW ~−30 mm w 2D | Staniszewski 2023 | **high** 2D; **med** na pojeździe |
| Pasywne DRS 019/020: Cx↓, \|Cz\|↓ poniżej 3,68 | CSV RW | **high** |
| Fan OUT | Michalecki | **high** |

---

## 7. Shortlista hipotez pod ~12 pp (do zatwierdzenia Spec)

Cel iteracji: **zmniejszyć udział przodu o rząd ~12 pp** przy |Cz| ≥ 3,682 i Cx ≲ 1,23. Bez dokręcania samego FW.

| # | Hipoteza | Dźwignia | Co mierzyć | Ryzyko / limit | Źródło kierunku |
|---|----------|----------|------------|----------------|-----------------|
| H1 | Więcej docisku z **tylnego skrzydła** (kąty / overlap / szczelina w stronę optimum 2D, ale na pakiecie) | RW | Δbalans, ΔCz, ΔCx, Cm | Coupling ze body — optimum 2D ≠ 3D | Staniszewski 2023 |
| H2 | Mocniejszy / bardziej „tylny” **dyfuzor–UT** (bez obniżania nosa FW) | UT | j.w. + GC ≥30 mm (T 2.2.1) | Masa, Cx(δ), kontakt z torem | Staniszewski 2024; T8 |
| H3 | Lekkie **odciążenie przodu** (kąt/elementy FW w dół), tylko jeśli H1–H2 nie domykają 12 pp | FW | j.w. | Łatwo stracić \|Cz\| — ostatnia dźwignia, nie pierwsza | cel balansu + T 8.2.1 box FW |
| H4 | **Wąsy** — tylko jeśli H1–H3 nie domykają; profil **dobrać pod lokalizację** (nie automatycznie S1223) | wąsy | Δbalans vs L/D; keep-out kół | TBD decyzji | Nagłowski (kierunek); dobór profilu otwarty |
| H5 | Ruchomy DRS | — | — | **OUT** (decyzja Mikołaja). Pasywne klapy tylko jako osobna gałąź oporu, nie peak-DF | decyzja 2026-09-01 |

**Kolejność:** H1 → H2 → (H3 gdy trzeba) → H4 jeśli nadal za dużo z przodu. H5 ruchomy = OUT.
