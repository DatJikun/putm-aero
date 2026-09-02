# Preferencje Spec przed H2: dźwignie balansu przez undertray

**Status:** notatka preferencji dla Spec (przed CFD H2), 2026-09-02 Europe/Warsaw  
**Język:** PL, ton koleżeński  
**Zasada:** liczby tylko z cytowanych źródeł; nie przepisujemy Cl/Cd cudzych aut na `RW_iter017`. Braki = **nie znaleziono**.

**Kotwica:** `RW_iter017` @ 15 m/s — Cx = **1,229**, Cz = **−3,682**, Cm = **−0,429**, balans ≈ **61,6%** przód → cel ~**50/50** (~**12 pp** do tyłu).  
**Kolejka:** H1 RW najpierw (bramka 2D jeszcze nie zielona — szum siatki), potem H2 floor.  
**Zamrożone:** DRS OUT, fan OUT; eventy Endurance + Autocross.

Nie duplikujemy tu całej nocnej notatki UT. Budujemy na:  
[research-overnight-ut-yaw-balance.md](research-overnight-ut-yaw-balance.md) · [research-balance-shift.md](research-balance-shift.md) · [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md) · [staniszewski-2024-energy.md](staniszewski-2024-energy.md) · [naglowski-2024-package.md](naglowski-2024-package.md) · [research-papers-rw-ut-yaw-clcd.md](research-papers-rw-ut-yaw-clcd.md).

---

## 1. Dźwignie, które cofają balans przez podłogę

Cel H2: więcej docisku **z tyłu** UT (dyfuzor / uszczelnienie), bez dokręcania nosa FW. Poniżej same dźwignie CAD + opublikowane liczby na osobnych liniach (cudze auta — kierunek, nie target 017).

### 1.1 Lokalizacja throat / wejście dyfuzora

Peak niskiego Cp siedzi przy wejściu dyfuzora. Przesunięcie throat wzdłuż auta przesuwa center of pressure — to bezpośrednia dźwignia balansu (Jensen/OSU za Katzem).

- mechanizm: throat dalej do tyłu → peak Cp dalej do tyłu → więcej % tyłu  
- źródło kierunku: https://ir.library.oregonstate.edu/downloads/7h149t91w  
- **Δbalans % na RWiter017 przy przesunięciu throat: nie znaleziono** (brak naszej mapy CAD↔postpro)

### 1.2 Kąt ekspansji dyfuzora

Zbyt stromy kąt → separacja w środku kanału → spadek DF i skok drag. W 2D optimum bywa bardzo płaskie; w 3D wiry wejściowe pozwalają na większe kąty zanim się oderwie.

Chalmers CFS 2021 (ich auto, CL = docisk dodatni, balance = % **tyłu**):

- CL straight (13°) = 3,729  
- CL cornering (13°) = 3,603  
- CD straight (13°) = 1,419  
- aero balance rear (13°, straight) = 49,68%  
- CL straight (19°) = 3,663  
- CD straight (19°) = 1,402  
- autorzy wybrali **13°** za odporność w straight / brake / corner, nie za absolutny peak w jednym case  

Źródło: https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download

SAE 2017-01-5016 (ich CFD, 27 iteracji inlet/outlet/GC):

- best L/D: inlet = 3°, outlet = 10°, GC = 30 mm  
- słaby przypadek: inlet = 5°, outlet = 16°, GC = 50 mm  

Źródło: https://doi.org/10.4271/2017-01-5016  
**Bezwzględne Cl/Cd z tej pracy w abstractcie: nie znaleziono** (tylko ranking L/D).

### 1.3 Strakes / fences / multi-channel

Strakes dzielą kanały, ograniczają spanwise migrację separacji i wspierają „diffuser pumping”. Chalmers po strakes + side floors (kąt 13°, ich CFS):

- CL straight = 3,854  
- CL cornering = 3,619  
- CL braking = 3,005  
- aero balance przy hamowaniu ≈ 67% rear (ich definicja)  

Źródło: Chalmers Tab. 4.5 / overnight UT note.

Jowsey & Passmore 2010 (bluff body, tunel; multi-channel 2–4):

- multi-channel daje duże zyski DF tuż powyżej optimum płaskiego dyfuzora  
- przyrost drag = minimalny  
- teza Jowsey 2013: multi-channel podnosi DF powyżej ~13°, do ~**13%** dla kątów mid-range 16°–19°  

Źródła: https://doi.org/10.1243/09544070JAUTO1339 · https://dspace.lboro.ac.uk/2134/13646

SAE 2017-01-2163 (vanes + flap na dyfuzorze FSAE-like):

- vanes: DF ↑ do **13%**  
- vane + flap razem: DF ↑ do **25%** (max w ich serii)  

Źródło: https://saemobilus.sae.org/papers/numerical-investigation-aerodynamic-effects-vanes-flaps-automotive-underbody-diffusers-2017-01-2163  
Uwaga: to nie jest nasze auto; traktujemy jako rząd wielkości dźwigni, nie jako promise na 017.

### 1.4 Ride height (prześwit)

Ground effect: mała zmiana RH → duża zmiana obciążeń. FSG T 2.2.1: static GC ≥ **30 mm**; sliding skirts / kontakt z torem = OUT (T 2.2.2).

FST Lisboa FST10e (aeromap, abstract):

- ride height → ~**10%** zmiany CD·A między peakami  
- ride height → ~**20%** zmiany −CL·A między peakami  

Źródło: https://scholar.tecnico.ulisboa.pt/records/WjT08GaGU4ee77V1ZI_WgpbeDe_scfAseZd-?lang=en

ZHAW / Zurich UAS Racing (model 1:4, WT + CFD):

- rake **3°** = najwyższa efektywność w ich teście  
- wpływ rake większy przy niższym RH; wydajność ↑ do **~10%**  

Źródło: https://doi.org/10.21256/zhaw-29935

**Mapa RH dla RWiter017: nie znaleziono** (brak zamrożonych CSV / postpro sił vs prześwit).

### 1.5 Rake (pitch podłogi: tył wyżej niż przód)

Rake ładuje podłogę i wzmacnia wiry krawędziowe; przy niskim RH efekt jest mocniejszy. ASME JEF (eksperyment bluff body + dyfuzor): rake podnosi DF na wszystkich RH i kątach dyfuzora, najmocniej przy niskim RH; kara drag = mała → L/D też rośnie. Mechanizm: więcej loadu z przodu floor (pumping), słabszy peak ssania w throat (mniej ryzyka stallu dyfuzora), silniejsze wiry streamwise.

Źródło: https://doi.org/10.1115/1.4067506  
**Konkretne Cl/Cd vs kąt rake w abstractcie: nie znaleziono** (tylko kierunek + mechanizm).

### 1.6 Kick-up / gurney na wyjściu dyfuzora

Kick-up / mini-flap na TE dyfuzora pomaga „wysysać” powietrze spod auta (podobnie jak flap w SAE 2017-01-2163). Willemsen (TU/e, FSAE context) wymienia gurney na końcu dyfuzora jako parametr optymalizacji obok kąta i RH.

Źródło kontekstowe: https://pure.tue.nl/ws/files/67736767/851403-1.pdf  
**Opublikowane Cl/Cd / Δbalans dla samego kick-up na FS full-car w naszych źródłach: nie znaleziono.**

### 1.7 Udział UT w pakiecie (orientacja PUT, inny model)

Nagłowski 2024 (nie 017):

- Fz_ut = −201,88 N  
- Fz_all = −561,00 N  
- udział UT ≈ **36%** Fz  
- balans baseline = **60,3%** przód  

Źródło: [naglowski-2024-package.md](naglowski-2024-package.md)

Kirchberger EDGE 14:

- UT ≈ **~40%** docisku auta  

Źródło: https://doi.org/10.34726/hss.2023.115880

---

## 2. Wrażliwość na RH, yaw i cornering — co się psuje

### 2.1 Yaw / δ (zakręt)

Staniszewski 2024 (PUT, już w KB): UT&SW mocno traci przy δ≠0; FW/RW są względnie płaskie. Pełny pakiet i tak ma wyższe |Cz| w całym δ vs samo FW&RW; krzywe Cx przecinają się ~10°. Proxy energii toru:

- F2/F1 = 0,973 → **−2,7%** średniej F_ham mimo **+~10 kg** UT  

Źródło: [staniszewski-2024-energy.md](staniszewski-2024-energy.md)

FST Lisboa:

- yaw → ~**16%** zmiany docisku w badanym zakresie (najbardziej wrażliwy parametr attitude)  
- roll → ~**9%** DF i ~**12%** przesunięcia CoP  

Oregon State Jensen:

- yaw **5°** (bez roll): DF → **62 lb** (vs niższy case prosty w tej samej sekcji)  
- yaw **5°** + roll **1°**: DF **−6%** względem samego yaw  

Źródło: https://ir.library.oregonstate.edu/downloads/7h149t91w

Chalmers cornering (R≈12,5 m, slip 3,5°, roll 0,7°): CL całego auta prawie stoi vs straight (np. small diffuser 3,544 vs 3,612), ale **pitch hamowania** zabija FW i cofa balans mocno do tyłu (~67% rear).

ASME JEF 2025 (cornering, snippet):

- CLA spada **>20%** (mocniej przy małych R)  

Źródło: https://doi.org/10.1115/1.4069995  
Pełna tabela: paywall — **nie odczytano**.

NTNU: stały yaw ≠ prawdziwy rotating-flow cornering; momenty bywają przeciwne.  
Źródło: http://hdl.handle.net/11250/2433712

### 2.2 Co konkretnie „pęka”

1. **Stall dyfuzora** — za duży kąt + za niski RH + pitch/yaw jednocześnie → bąbel separacji, spadek DF tyłu, skok drag.  
2. **Utrata rear DF w łuku** — Staniszewski: siły z UT&SW spadają przy δ≠0; auto „na papierze” z tyłu przy δ=0 może wrócić w stronę front-bias w Autocross/Endurance.  
3. **Migracja balansu przy brake** — Chalmers: pitch → dużo % tyłu; setup 50/50 na prostej ≠ 50/50 w sekwencji brake–turn.  
4. **GC / Tech** — static ≥30 mm; dynamic rake przy obciążeniu aero może zbliżyć podłogę do toru (T 2.2.2).  
5. **Masa** — +~10 kg UT (Staniszewski) bez zwrotu F_ham na modelu toru = zły deal pod Endurance.

---

## 3. Checklist pomiarów Fluent / OpenFOAM (seria H2)

Praktyczna lista metryk — **bez** recepty solvera / meshingu.

### Siły i momenty (każdy case)

- Cx, Cz, Cm (half-car, V = **15 m/s**, moment @ **x = 0,765 m**, Lref **1,53 m** — jak CFD#1)  
- balans % przód = `1/2 + Cm/Cz` **oraz** ten sam podział przód/tył co w Excelu zespołu (potwierdzić postpro)  
- Fz_UT / Fx_UT (jeśli reporty komponentów działają) + udział Fz_UT / Fz_all  
- Δ vs kotwica 017: Δbalans [pp], ΔCz, ΔCx  

### Guardrale sukcesu (jak TARGETS / H2 w levers)

- |Cz| ≥ **3,682**  
- Cx ≲ **1,23**  
- balans w stronę **48–52%** przód (~**12 pp** od **61,6%**)  

### Cp / diagnostyka floor

- Cp na spodzie (kontury + kilka przekrojów streamwise przez kanały)  
- skin friction / odrywanie w dyfuzorze (czy jest bąbel w środku kanału)  
- wizualnie: czy peak ssania siedzi tam, gdzie chcieliśmy throat  

### Mapa yaw / attitude (gate przed zamrożeniem geometrii)

Minimum kandydatów UT:

1. δ = **0°** (porównanie do 017)  
2. yaw / δ ≈ **5°** (tani stress test jak OSU) **albo** punkty z Tab. 9 Staniszewskiego (r ≈ 17,5 → 4,4 m)  
3. opcjonalnie: pitch hamowania (~1° jak Chalmers), jeśli kinematyka stoi  

Dla każdego punktu mapy: Cx, Cz, Cm, balans %, jakościowo Cp dyfuzora.

### Czego nie mierzyć „dla ozdoby”

- izolowane 2D dyfuzora bez pakietu (coupling z kołami / RW jak u Staniszewskiego 2023 dla skrzydeł)  
- DRS open / fan suction (oba OUT)  
- Wh baterii z samego CFD — tylko proxy F_ham + model toru, jeśli robimy notę energii  

---

## 4. Luki / nie znaleziono

1. **Δbalans [pp] vs przesunięcie throat / kąt / rake na RWiter017** — nie znaleziono (brak CSV sił UT z postpro 017).  
2. **Konkretne Cx(δ), Cz(δ) punktowo ze Staniszewskiego 2024** — tylko na wykresach; plain text bez tabeli.  
3. **Tabele yaw liczbowe z tezy Jowsey** — PDF dspace nie ekstrahowany w tej sesji; paper 2010 ma kierunek multi-channel, nie gotową mapę yaw do wklejenia.  
4. **Kick-up: opublikowane Cl/Cd / Δbalans na FS full-car** — nie znaleziono.  
5. **Cl/Cd absolute z SAE 2017-01-5016** — abstract podaje tylko ranking L/D (3°/10°/30 mm vs 5°/16°/50 mm).  
6. **Zamrożona mapa RH/rake dla 017** — nie znaleziono.  
7. Head-to-head „nasz stary UT vs nowy dyfuzor” z udziałem Fz_UT na 017 — do zmierzenia w Fluent, nie z literatury.

---

## 5. Implikacja dla PUT: po H1, co w H2 first

Kolejka zostaje: **H1 RW → H2 UT**. Bramka 2D H1 nadal nie zielona (szum siatki) — nie startujemy H2 CAD/CFD „na zapas” jako zamiennika RW.

Gdy H1 da tabelę Δbalans/ΔCx/ΔCz na pakiecie 017, pierwsza fala H2 (kolejność preferencji Spec):

1. **Throat location + kąt ekspansji** na bazie 017 (bez ruszania nosa FW) — 2–3 warianty kąta wokół „umiarkowanego” (literatura: Chalmers **13°** robust; SAE outlet **10°** best L/D; nie od razu 19°). Cel: Δbalans ≥~2 pp przy guardralach.  
2. **Strakes / side fences** na zwycięzcy kąta — jeden case „on/off”, metryki jak wyżej + Cp w corner/yaw.  
3. **Mini-mapa δ** (0° + ~5° + jeden punkt ~10–15°) **zanim** zamrozimy geometrię — kill, jeśli średni |Cz| / proxy toru gorsze niż baza.  
4. Dopiero potem: **rake / RH sweep** (CAD + ewentualnie attitude), z GC ≥30 mm z marginesem.  
5. Kick-up / TE flap — **opcjonalnie**, bo brak twardych liczb FS; jeden case, nie pierwsza dźwignia.

Kill criteria (z [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md)): brak Δbalans i braku wzrostu |Cz| przy Cx≲1,23; mapa δ gorsza na modelu toru; GC/T 2.2.2 nieutrzymalne; +kg bez zwrotu F_ham.

---

## Claims (skrót)

| claim | evidence | confidence |
|-------|----------|------------|
| Throat location = dźwignia CoP/balansu UT | Jensen/OSU + Katz | **high** (kierunek) |
| ~13° ekspansji bywa bardziej robust niż 19° w manewrach | Chalmers Tab. 4.3 | **med** (ich auto); kierunek „nie max angle” **high** |
| Strakes + side floors: CL straight = 3,854 (CFS) | Chalmers | **med–high** (ich CFD) |
| UT yaw-sensitive; mapa δ = gate | Staniszewski 2024 | **high** |
| RH: ~10% CD·A / ~20% −CL·A między peakami (FST10e) | Carreira abstract | **high** na FST10e; transfer **med** |
| Rake podnosi DF, najmocniej przy niskim RH | ASME 10.1115/1.4067506; ZHAW RA 3° | **high** (kierunek); Δ na 017 **TBD** |
| Kick-up ΔCl na FS full-car | — | **nie znaleziono** |
| Gap 017 ≈ 12 pp (61,6%→50%) | Cm/Cz + Spec | **high** (roboczo) |

---

## Źródła (URL / DOI / KB)

- Chalmers 2021 — https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download  
- Jensen OSU 2010 — https://ir.library.oregonstate.edu/downloads/7h149t91w  
- Jowsey & Passmore 2010 — https://doi.org/10.1243/09544070JAUTO1339  
- Jowsey teza — https://dspace.lboro.ac.uk/2134/13646  
- SAE 2017-01-5016 — https://doi.org/10.4271/2017-01-5016  
- SAE 2017-01-2163 — https://saemobilus.sae.org/papers/numerical-investigation-aerodynamic-effects-vanes-flaps-automotive-underbody-diffusers-2017-01-2163  
- FST Lisboa aeromap — https://scholar.tecnico.ulisboa.pt/records/WjT08GaGU4ee77V1ZI_WgpbeDe_scfAseZd-?lang=en  
- ZHAW rake/RH — https://doi.org/10.21256/zhaw-29935  
- ASME rake bluff body — https://doi.org/10.1115/1.4067506  
- Kirchberger EDGE14 — https://doi.org/10.34726/hss.2023.115880  
- Staniszewski / Nagłowski / overnight UT / levers H1–H5 — lokalne `sources/`
