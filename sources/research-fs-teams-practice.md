# Research: jak inne zespoły FS ustawiają pakiet aero (FW / RW / UT)

**Status:** notatka claims-based do Spec (2026-09-01)  
**Język:** PL  
**Zasada:** każda liczba ma źródło (teza / artykuł / URL). Brak liczby = **TBD / not found** — bez inventowania.

**Kotwica zespołu (kontekst, nie „literatura zewnętrzna”):** `RW_iter017` — Cx **1,229** / Cz **−3,682** / Cm **−0,429** → balans ≈ **61,6%** przód; cel ≈ **50/50**; priorytet **Endurance + Autocross**; DRS ruchomy **OUT**; fan **OUT**; rozważyć RW **4-elementowe**.  
Źródła wewnętrzne KB: [naglowski-2024-package.md](naglowski-2024-package.md), [staniszewski-2023-wing.md](staniszewski-2023-wing.md), [staniszewski-2024-energy.md](staniszewski-2024-energy.md), [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md), [team-rwiter017-baseline.md](team-rwiter017-baseline.md), [TARGETS.md](../TARGETS.md).

**Uwaga konwencji:** PUT używa **Cx, Cz** (Cz ujemny = docisk). Publikacje EN często **Cl/CL, Cd/CD** albo **CLA/CDA [m²]**. Różne A_ref, V i modele — **nie uśredniać** w jeden „typowy Cl/Cd FS”.

---

## 1. Summary for Spec

Typowy pakiet aero bolidu FS/FSAE w otwartych tezach i case’ach to **przednie skrzydło (FW) + tylne skrzydło (RW) + undertray/dyfuzor (UT)**, czasem sidepody / side wings / „bullhorns”. Kolejność rozwoju bywa **RW → FW → UT** (RW dyktuje dużą część oporu; FW równoważy balans i prowadzi powietrze; UT jest najefektywniejszym generatorem docisku) — opis eMotorsports Cologne / SimScale.

W publicznych liczbach **bezwymiarowe** |Cl| / Cx całych pakietów high-DF leżą mniej więcej w przedziale **~3–4+** docisku i **~1,2–1,5** oporu (Hogea 2026; Nagłowski 2024; kotwica 017), ale starsze / inne pakiety bywają wyraźnie niższe (Jackson z samym RW ~CL_DF 1,15; Staniszewski 2023 ~|Cz| 2,0). **Balans** publikowany jako % przód pojawia się zarówno jako **~56%** (Orion Racing / IJRASET), **~40,6%** CoP forward (WashU / Hogea), jak i **~57–62%** w modelach PUT wysokiego DF — nie ma jednego „standardu branżowego”, tylko decyzja pod CG i handling.

Dla **Autocross** zespoły często maksymalizują docisk (nawet kosztem L/D); dla **Endurance** liczy się też opór i energia (regulowane klapy / DRS tam, gdzie legalne; mapy Cx,Cz vs yaw/ride height). Przy decyzji Spec **DRS OUT** nie ma „otwartego” low-drag na prostych jak u Jacksona — trade-off Endurance trzeba brać **pasywnie** (AOA RW, mapy UT).

---

## 2. Tabela przykładów zespołów / prac (claim | evidence | confidence)

| claim | evidence | confidence |
|-------|----------|------------|
| Standardowy zestaw urządzeń: **FW + RW + undertray/dyfuzor** (opcjonalnie sidepody / side wings) | Kirchberger 2023 (TU Wien EDGE 14): „frontwing, undertray and rearwing”; SimScale / eMotorsports Cologne (Umicore Loup): RW, FW, undertray; Hogea et al. 2026: undertray → multi-element FW/RW → sidepods | **high** (powtarzalny opis w wielu źródłach) |
| Kolejność rozwoju: najpierw **RW** (opór / energia), potem **FW** (balans + prowadzenie przepływu), potem **UT** (efektywność) | SimScale blog, Pfeiffer / eMotorsports Cologne: „development started with the rear wing… determining factor for… energy consumption”; FW „equalizes the rear wing… guides air to undertray”; UT „most efficient” | **med** (jeden dobrze opisany case; nie dowód, że wszyscy tak robią) |
| UT jest **najefektywniejszym** elementem (dużo DF, mało drag) | SimScale: „most efficient… without generating much drag”; Kirchberger: UT „generates **40%** of the downforce” EDGE 14; literatura w tezie Centaurus (snippet CORE): „about **40–50%** by the undertray-diffuser… front and rear wings… each about **20–30%**” | **high** kierunek; **med** na % (różne auta; Centaurus PDF nie pobrano w całości — cytat ze snippeta CORE) |
| FW ~**235%** bardziej efektywne niż RW (w jednym pakiecie Cologne) | SimScale: „around **235%** more efficient” (ground effect) | **med** (jedna liczba zespołowa; inna geometria) |
| Cele liczbowe pakietu WashU / Hogea: **−Cl = 3,19**, **Cd = 1,29**, **CoP = 40,6%** forward | Hogea, Hogea, Agarwal, AIAA 2026-1898 abstract: „−Cl of **3.19**, Cd of **1.29** and a CoP of **40.6%** forward”; DOI https://doi.org/10.2514/6.2026-1898 | **high** (liczby w abstrakcie); **med** transfer (A_ref / V nie w abstrakcie) |
| Orion Racing India baseline aero balance: **56%** front DF (regulowane klapy) | Pamnani et al., IJRASET 2020: „slight front dominated downforce of **56%** was selected as baseline”; DOI https://doi.org/10.22214/ijraset.2020.32700 | **high** (decyzja projektowa w paperze) |
| Heave zmienia balans o ok. **±5%** front (mapa Orion) | IJRASET 2020 §V.1: „A **+-5%** change is observed in aerodynamic balance” przy heave | **high** (ich model); **low–med** transfer |
| CFD V odniesienia często **~15–16 m/s** (typowy zakres FS) | Kirchberger: inlet **15 m/s** (z telemetrii toru); IJRASET BC: inlet **−16 m/s**; PUT Nagłowski / Staniszewski: **15 m/s** | **high** (powtarzalna praktyka) |
| TU Wien EDGE 14 (StarCCM+, half-car): CLA ≈ **4,66…5,2 m²**, CDA ≈ **1,51…1,72 m²**; A czołowa ≈ **1,19 m²** | Kirchberger 2023 Tab. 2.1 / §2.2; residuals CLA **−4,66** @1800 iter | **high** CLA/CDA jak w tezie; **med** jako „Cl/Cd” (to współczynniki × powierzchnia — nie mieszać z Cx/Cz PUT bez A_ref) |
| Walidacja torowa: CFD bywa **nadmiarowe** w docisku UT | Kirchberger: pressure taps → CFD ma niższe ciśnienie ssące → „not as much downforce… undertray”; średni błąd wielkości ~**9,3%**; Kansas coast-down (Wordley-related KU thesis abstract): drag ~**5%**, downforce do **~18%** odchyłki CFD↔tor | **high** kierunek (CFD≠tor); wielkości zależą od setupu |
| Jackson (Huddersfield): pojazd+RW DRS closed **CL_DF=1,15 / CD=1,21**; open **0,26 / 0,79**; −**35%** siły oporu | Jackson 2018; notatka KB jackson-2018; V=**26,8 m/s** | **high** |
| RW 3-el. E423, overall AOA **22,81°** (flaps 28°/60°) przed stall ~25° | Jackson 2018 | **high** (ich RW) |
| Optymalizacja AI/GA kątów skrzydeł FSAE: +**14,8%** DF FW, +**28,4%** DF RW; profile **MSHD** i **Selig 1223**; AoA FW 4,5°/28°/56° → 5,5°/33°/59,5°; RW 9,5°/40° → 12,2°/41,9° | Abstract IJFT 2025 https://doi.org/10.1016/j.ijft.2025.101440 (pełny PDF w tej sesji: timeout) | **med** (abstract); pełne warunki CFD **TBD** bez PDF |
| eMotorsports Cologne: setup Accel RW ma drag **64,7%** niższy niż high-DF (Autocross/Skidpad) | SimScale blog (regulowane klapy) | **med** (blog zespołu; nie paper peer-review) |
| Rake UT **1°** → ok. **+15%** DF z undertraya (Cologne) | SimScale: „rake angle of only **1°** increases… undertray by around **15%**” | **med** (jeden case) |
| PUT Nagłowski 2024 @15 m/s: Cz≈**−4,07**, Cx≈**1,45**, balans **60,3%** → **57,3%** z wąsami; udział Fz FW≈**39%** / UT≈**36%** / RW≈**24%** | naglowski-2024-package.md Tab. 5.2–5.3 | **high** (ich model) |
| PUT Staniszewski 2023 pojazd: Cx≈**0,726**, Cz≈**−2,036** @15 m/s (RW 3-el.) | staniszewski-2023-wing.md | **high**; **nie** „typowy high-DF 2024+” |
| PUT Staniszewski 2024: pełny pakiet (UT&SW) wyższe \|Cz\| vs FW&RW dla każdego δ; Cx krzywe przecinają się ~10°; proxy F_ham **−2,7%** mimo **+~10 kg** | staniszewski-2024-energy.md | **high** (kierunek / proxy) |
| PUT newsletter X.2025 (testy torowe DRS): opór siłowy −**42%**, Cx −**>30%**, docisk **>1150 N** | https://www.putmotorsport.pl/newsletter/pazdziernik2025/ | **med** (komunikat PR; V / konfiguracja DRS closed/open / A_ref nie podane w newsletterze) |
| Wrażliwość laptime (TU Wien): **+10% DF → ~−1%** lap; wrażliwość masy ~**2×** wrażliwości DF | Kirchberger Fig. 1.1 / §1.2 | **med** (jeden zespół / tor) |
| Monash / Hendy: aero mapy FRH×RRH×roll×steer×yaw jako narzędzie setupu (nie same Cl@δ=0) | Monash Motorsport blog Hendy 2019; LEAP guest blog | **high** (metoda); liczby Cl/Cd mapy **not found** w otwartym blogu |
| Hogea: start optymalizacji od **undertraya**, potem skrzydła (odwrotnie niż Cologne) | AIAA abstract: „beginning with an undertray, followed by… front and rear wings” | **high** (opis procesu w abstrakcie); pokazuje, że kolejność **nie jest uniwersalna** |

---

## 3. Zakresy Cl/Cd / balansu — zestawienie (nie uśredniać)

| Źródło | V | Docisk | Opór | Balans / CoP | Uwagi |
|--------|---|--------|------|--------------|-------|
| Hogea 2026 (WashU FSAE) | n/d w abstrakcie | −Cl **3,19** | Cd **1,29** | CoP **40,6%** forward | Pełny pakiet po iteracjach |
| Nagłowski 2024 (PUT) | 15 m/s | Cz **−4,071** | Cx **1,453** | **60,3%** przód | Baseline; wąsy → 57,3% |
| **RWiter017 (zespół)** | 15 m/s (kontekst) | Cz **−3,682** | Cx **1,229** | ≈**61,6%** przód | Kotwica Spec |
| Staniszewski 2023 (PUT) | 15 m/s | Cz **−2,036** | Cx **0,726** | n/d | Wcześniejszy / niższy DF |
| Jackson 2018 + RW closed | 26,8 m/s | CL_DF **1,15** | CD **1,21** | n/d (FW balance pominięty) | Głównie efekt RW |
| Jackson DRS open | 26,8 m/s | CL_DF **0,26** | CD **0,79** | n/d | −35% siły oporu |
| Kirchberger / EDGE 14 | 15 m/s | CLA ≈ **4,7–5,2 m²** | CDA ≈ **1,5–1,7 m²** | n/d %; UT ~**40%** DF | A≈1,19 m²; CLA≠Cl |
| Orion / IJRASET | 16 m/s (BC) | Cl mapy (wykresy) | Cd mapy | baseline **56%** front | Wartości Cl/Cd punktowe w tekście **not found** (tylko mapy) |

**Claim roboczy pod Spec:** pakiety „dojrzałe” high-DF w otwartej literaturze 2024–2026 lądują blisko **|Cl|~3–4 / Cd~1,2–1,5**, co jest **spójne rzędem** z RWiter017 i Nagłowskim; Jackson (~1,15) i Staniszewski 2023 (~2,0) to inne etapy / inne cele — **nie** traktować jako target 2026. | evidence: tabela powyżej | **med** (mała próbka; różne A_ref).

**Balans:** publikowane cele wahają się od **~41%** (Hogea CoP forward) do **~56%** (Orion) i **~57–62%** (PUT high-DF). Cel zespołu **~50/50** leży **wewnątrz** tej chmury, ale **bliżej środka** niż obecne ~61,6%. | **med**

---

## 4. Endurance vs Autocross — implikacje

Punkty FSG (Kirchberger Tab. 1.1, rules 2023): Endurance **250**, Autocross **100**, Efficiency **75**, Accel **50**, Skidpad **50** — Endurance + Efficiency mocno ważą w EV.

| Event | Co robią / deklarują inne zespoły | Implikacja przy Spec (DRS OUT, Endurance+AX priorytet) | conf. |
|-------|-----------------------------------|------------------------------------------------------|-------|
| **Autocross** | Max DF; L/D drugorzędne (SimScale: „lap times… shorter with more downforce, even if… efficiency decreases”); regulowane klapy w high-DF | Trzymać \|Cz\| ≥ 3,682; nie ciąć DF pod Cx bez modelu AX | **high** kierunek |
| **Endurance** | Opór i energia; Cologne: RW Accel setup −64,7% drag vs high-DF; Jackson DRS −35% drag; Staniszewski: mapa Cx/Cz(δ) + model toru, UT yaw-sensitive | Bez DRS: szukać **pasywnego** kompromisu Cx przy zachowaniu DF; **gate yaw na UT** przed zamrożeniem | **high** metoda; wielkość na 017 = **TBD** |
| **Efficiency** | Część punktów EV; UT może obniżyć proxy energii mimo masy (Staniszewski −2,7% F_ham / +~10 kg) | Pilnować masy UT vs zwrot energetyczny | **med** |
| **Accel / proste** | Low AOA / DRS open (Jackson, Cologne) | Przy DRS OUT: nie priorytet P1; nie pogarszać Cx 017 „za darmo” | **high** (decyzja Spec) |
| **Dynamic attitude** | Orion/Monash: aeromapy heave/pitch/roll/yaw; heave ±5% balans | Nie projektować tylko @δ=0 / nominal RH | **high** (proces) |

**Claim:** przy priorytecie Endurance+Autocross i DRS OUT bramka projektowa = **mapa Cx,Cz vs δ (i ewent. RH)** + jasny target balansu ~50/50 przez **RW+UT**, nie dokręcanie samego FW. | Staniszewski 2024 + SimScale + IJRASET + research-balance-shift | **high** (proces); Δ pp na 017 = **TBD CFD**.

---

## 5. Gaps / TBD

| Gap | Status |
|-----|--------|
| Bezwymiarowe Cl/Cd EDGE 14 (tylko CLA/CDA m² + A≈1,19) — pełna tabela % balansu | **TBD** (nie w plain text Kirchberger jako % front) |
| Pełny PDF Centaurus (udziały 40–50 / 20–30) — weryfikacja stron | **TBD** (download CORE nieudany w sesji; zostaje snippet) |
| Pełny tekst IJFT 2025 (warunki V, A_ref, cały pojazd vs izolowane skrzydła) | **TBD** (timeout ScienceDirect) |
| FSG Design Reports z publicznymi tabelami Cl/Cd 2024–2026 | **not found** w tej sesji (często nieotwarte) |
| Typowy udział FW/RW/UT „branżowy” poza Nagłowski / Kirchberger / Centaurus snippet | **TBD** — za mało jawnych tabel |
| Liczby 4-elementowego RW w otwartej literaturze FS | **not found** (Jackson / Staniszewski = 3 el.; Cologne „three-element + leading-edge flap”) |
| V i stan DRS przy newsletterze PUT (>1150 N, −42% opór) | **TBD** (PR) |
| Wspólny A_ref Fluent PUT vs Hogea / Jackson do porównania 1:1 | **TBD** (TARGETS: Aref nadal wymagane) |
| Wpływ yaw na balans u innych zespołów (poza „changes marginally” Orion) | **TBD** ilościowo |

---

## 6. Limity (czego nie wnioskować)

1. Nie uśredniać Jackson (CL~1 @26,8 m/s) z Nagłowskim (Cz~−4 @15 m/s) w „średni Cl FS”.  
2. Nie mylić **CLA [m²]** (Kirchberger) z **Cz** (PUT) bez A_ref.  
3. „CoP 40,6% forward” (Hogea) i „56% front” (Orion) to **różne cele** — nie wybierać „prawdziwszego” bez relacji do CG i tire model.  
4. Blog SimScale / newsletter PUT = dobre **kierunki**, słabsza **metryka** niż teza/paper.  
5. DRS w literaturze **nie** jest ścieżką peak-DF (Jackson open ↓DF) — zgodne z decyzją Spec OUT.  
6. 4-el. RW = hipoteza CAD w envelope T8, **bez** liczb z literatury w tej notatce.

---

## Źródła (URL / DOI)

1. Hogea E.N., Hogea R.J., Agarwal R.K. — *3D Iterative Parametric Optimization… FSAE…*, AIAA 2026-1898, https://doi.org/10.2514/6.2026-1898  
2. Pamnani et al. — *Tuning… Aerodynamic Maps*, IJRASET 8(XII) 2020, https://doi.org/10.22214/ijraset.2020.32700 / https://www.ijraset.com/fileserve.php?FID=32700  
3. Kirchberger M. — *CFD Simulation and Validation of a Formula Student Car*, TU Wien 2023, https://repositum.tuwien.at/bitstream/20.500.12708/188917/1/Kirchberger%20Michael%20-%202023%20-%20CFD%20Simulation%20and%20Validation%20of%20a%20Formula%20Student...pdf  
4. Pfeiffer N. — *Formula Student Aerodynamics With CFD*, SimScale blog (eMotorsports Cologne), https://www.simscale.com/blog/formula-student-aerodynamics/  
5. Jackson F.F. — *Aerodynamic optimisation…*, 2018 (KB: jackson-2018-cfd-drs.md)  
6. Nagłowski K. — praca inż. PUT 2024 (KB: naglowski-2024-package.md)  
7. Staniszewski A. — prace PUT 2023/2024 (KB: staniszewski-*.md)  
8. IJFT 2025 AI-assisted CFD… — https://doi.org/10.1016/j.ijft.2025.101440 (abstract)  
9. PUT Motorsport newsletter X.2025 — https://www.putmotorsport.pl/newsletter/pazdziernik2025/  
10. Centaurus / Thireus thesis snippet — CORE / http://hdl.handle.net/11615/49094 (udziały % — do pełnej weryfikacji PDF)  
11. Monash Hendy aero map — https://www.monashmotorsport.com/blog/aeromapthesis  
12. KU coast-down validation abstract — https://kuscholarworks.ku.edu/… (drag ~5%, DF do ~18%)
