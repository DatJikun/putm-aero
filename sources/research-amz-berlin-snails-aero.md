# Intel aero: AMZ, FaSTTUBe (Berlin), Running Snail (+ pokrewne EU EV)

**Status:** notatka robocza (2026-09-01, Europe/Warsaw)  
**Język:** PL, ton teamowy  
**Cel:** podgląd praktyki aero top EU EV pod Spec PUT — H1 RW / H2 UT, DRS OUT, fan OUT, balans ~61,6% → ~50%.  
**Zasada liczb:** Cl/Cd/CLA/CDA i siły N cytujemy **tylko** gdy źródło je publikuje. Brak liczby = *not found*. Nic nie dopisujemy „z głowy”.

**Kotwica PUT:** `RW_iter017` — Cx **1,229** / Cz **−3,682** / Cm **−0,429** → balans ≈ **61,6%** przód; cel ≈ **50/50**.

---

## Wstęp

Trzy teamy z briefu: **AMZ Racing (ETH Zürich)**, berlinowski EV (weryfikacja nazwy poniżej) oraz **Running Snail Racing Team (OTH Amberg-Weiden)**. Dla każdego: jak budują aero (narzędzia CFD, walidacja, co widać z foto/stron/partnerów), obecność FW/RW/UT oraz opublikowane liczby ze linkami.

Przy okazji: **nie ma** aktywnego Formula Student EV teamu „Equipe Rennwagen FU Berlin”. Freie Universität Berlin robiła kiedyś projekty autonoma (Spirit of Berlin itd.), ale nie startuje w FS EV. Berlinowski team FS to **FaSTTUBe** (TU Berlin) — to on zastępuje „Equipe / FU” w tej notatce.

Na końcu krótko 2–4 podobne top EU EV, przy których wyszło dobre publiczne materiały aero, oraz luki i implikacje pod PUT.

---

## 1. AMZ Racing (ETH Zürich)

### Kim są i skąd materiał
AMZ to stały top overall EV (FSG 2024 i 2025 #1, WRL #1 po sezonie 2025). Publiczne źródła o aero są głównie **procesowe** (Siemens, AirShaper/Streamwise, Scientifica, karty FSG), nie „ściągą Cl/Cd z bolidu konkursowego”.

### Jak projektują aero
Siemens case study opisuje workflow: CAD w **NX**, struktura/ruch w **Simcenter 3D / Nastran**, aero w **STAR-CCM+**. Ciśnienia z CFD wracają do NX pod obciążenia skrzydeł i geometrię.  
Źródło: https://resources.sw.siemens.com/en-US/case-study-academic-motorsports-club-zurich/

Scientifica (opis pakietu aero): pakiet optymalizowany przez **ponad 2000** różnych symulacji CFD, potem walidacja w tunelu.  
Źródło: https://scientifica.ch/en/event/amz-racing-from-zero-to-one-hundred-in-0-956-seconds/

Profil LinkedIn aerodynamika (sezon 2024 / Dufour): redesign FW i RW — nowe FW poprawia przepływ do sidepodów i RW; zakrzywione (3D) RW pozwala na większe kąty natarcia; deklarowany **względny** skok docisku vs poprzedni prototyp. Jako CFD lead: mesh dependency, pipeline pod różne warunki jazdy, parametryczny CAD, porównanie **RANS vs LES**. Walidacja w **RUAG Automotive Wind Tunnel** + pomiary Pitot / ProCap (Streamwise).  
Źródło (profil): https://www.linkedin.com/in/robi-bernardoni-a5b6bb325  
Opublikowany względny claim:
- ΔDF ≈ +25% vs poprzedni prototyp (bez absolutnego Cl/Cd)

### Walidacja (WT + CFD)
AirShaper / Streamwise: bolid **eiger** w tunelu z moving belt; CFD porównawcze jako **DES** uśrednione ~1,2 s czasu fizycznego; pomiary ProCap ~5 h łącznie; porównanie Cp_total i streamlines wokół FW — topologia ogólnie zgadza się, lokalnie różnią się pozycje rdzeni wirów i rozmiary stref niskiego ciśnienia. Wir tip z górnego elementu nosa jest celowo prowadzony w stronę RW.  
Źródło: https://airshaper.com/blog/3d-flow-measurement-formula-student

LinkedIn Streamwise (2024, Dufour): kolejne sesje ProCap wokół FW i koła; dane do korelacji CFD↔WT; facility RUAG.  
Źródło: https://www.linkedin.com/posts/andrin-landolt-6aa86a6a_forumlastudent-windtunnel-aerodynamics-activity-7211262289281191936-lwuI

### Co widać z kart FSG / konceptów (jakościowo)
Karty FSG (opisy sezonów): **3D front and rear wings**, tire wake control; na **Dufour** (2024) pojawia się też **powered ground effect**; na **aurona** (2025) — redesigned aerodynamic kit z 3D FW/RW po erze fanów (reguły / ban powered GE → nacisk wraca na pakiet pasywny).  
Źródła: https://www.formulastudent.de/teams/fse/details/tid/248 (karta teamu; legacy czasem 500 — treść znana też z mirrorów FSG)  
Strona teamu: https://www.amzracing.ch/en

### FW / RW / UT
- **FW:** tak (multi-element / 3D main, wake control wokół opon) — potwierdzone WT planes + opisy FSG/LinkedIn.  
- **RW:** tak (3D / curved, agresywny AoA).  
- **UT / underbody:** tak (pełny pakiet ground-effect; na Dufour dodatkowo powered GE — **nie** kopiować do Spec PUT: fan OUT).

### Liczby absolutne Cl/Cd / N
**Not found** w otwartych źródłach dla pakietu konkursowego Dufour/aurona. Nie podajemy zmyślonych wartości. Jedyny jawny aero-metric w tej rundzie dla AMZ to względne **+25% DF** (LinkedIn) oraz skala procesu (**>2000** CFD + WT).

---

## 2. FaSTTUBe — Formula Student Team TU Berlin

### Weryfikacja nazwy
Szukane warianty „Equipe Rennwagen FU Berlin” / Equipe FU **nie** wskazują aktywnego teamu FS EV. Berlin = **FaSTTUBe** (Technische Universität Berlin, od 2005; EV od ~2018; FT24/FT25/FT26 jako linia EV/DV).  
Źródła: https://fasttube.de/team/ ; https://www.tu.berlin/kfz/studium-lehre/seminare-studentische-projekte/fasttube ; https://www.formulastudent.de/teams/fse/details/tid/230

### Jak projektują aero
Strona teamu (Aero / Composites): projekt skrzydeł i innych elementów przez **CFD**, potem wytwarzanie w CFRP / kompozytach. Przykładowe zespoły: **wings, CFD simulation, underbody**.  
Źródło: https://fasttube.de/team/

LinkedIn teamu (rekrutacja Aero & Composites): CFD + analiza aero, manufacturing skrzydeł i body, nacisk na efektywność i masę.  
Źródło: https://www.linkedin.com/posts/fasttube_speed-isnt-just-about-power-its-about-activity-7447237487846014976-AYxe

Historycznie (2017–2018) partner **FRIENDSHIP SYSTEMS / CAESES** wspierał FaSTTUBe oprogramowaniem i ekspertyzą optymalizacji kształtu. Blog CAESES opisuje pracę nad RW (Carolina Cura, FSG): parametryczne **3 airfoile + endplate** w CAESES, CFD w **STAR-CCM+**, DoE Sobol + lokalna optymalizacja, potem check na full vehicle.  
Źródła:  
https://www.friendship-systems.com/news/2017/friendship-systems-supports-fasttube/  
https://www.caeses.com/blog/2018/simulation-driven-design-of-a-race-car-rear-wing/

Opublikowane wyniki optymalizacji RW (CAESES + STAR-CCM+, full vehicle check):
- ΔDF (full vehicle) ≈ +3,9% vs baseline RW
- wkład 2D (profile/pozycje) ≈ +2,14%
- wkład 3D (endplate) ≈ +2,44%

Blog podkreśla też (literatura / praktyka FS, nie Cl bolidu FT26): RW potrafi dawać rząd **~1/3** całkowitego DF pakietu — traktuj jako orientację, nie jako metrykę FaSTTUBe 2025.

### Walidacja
Publicznie: głównie **CFD + build**. Brak w tej rundzie otwartego case’u WT full-scale dla FaSTTUBe porównywalnego z AMZ/RUAG. FT26 w karcie FSG: AWD EV+DV, steel spaceframe, transparent bodywork — aero nadal w pakiecie (skrzydła + underbody według subteamu).

### FW / RW / UT
- **FW:** tak (wings w opisie Aero).  
- **RW:** tak (historyczna optymalizacja 3-el. + endplate; nadal w scope Aero).  
- **UT / underbody:** tak (jawnie „underbody” na stronie teamu).

### Liczby absolutne Cl/Cd / N
**Not found** dla aktualnych FT24–FT26. Jedyna opublikowana para liczb w tym wątku to **względne %** z case’u CAESES 2018 (powyżej).

---

## 3. Running Snail Racing Team (OTH Amberg-Weiden)

### Kim są
Team FH Amberg-Weiden; FSG 2025 overall ~10., Endurance FSG25 4. — solidny mid/top EU EV, nie „showcase Siemens” jak AMZ, ale dużo praktyki manufacturing + CFD w CV członków.

### Jak projektują aero
OTH news (RS25, czerwiec 2025): **nowe aerodynamikpaket z 3D-printu** + przebudowane chassis; potem testy i systemy przed sezonem (HU / CZ / DE).  
Źródło: https://www.oth-aw.de/hochschule/aktuelles/news/rs25-enthuellt-running-snail-startet-mit-neuem-rennwagen-in-die-saison/

CV / LinkedIn członków aero:
- projekt i optymalizacja skrzydeł przez **CFD** oraz **wind tunnel testing** (Dumitru M.);
- rozwój **rear wing** (predevelopment + advanced) na RS24; covers aero/structural na RS25 z eksperymentalną formą 3D-print (Luis Meschede); CAD **Creo Parametric**.  
Źródła: https://www.linkedin.com/in/dumitru-m-e323 ; https://www.linkedin.com/in/luis-meschede-b5bb9a23a

Case Ansys (2024): **Ansys Discovery + Mechanical** — głównie **topologia bellcranków/uprightów** (nie pełny aero package). Wartość dla nas: team ma szybki loop symulacji (do ~20 sim/dzień na GPU Discovery) i kulturę iterate→print. Nie mylić z narzędziem CFD aero.  
Źródło PDF: https://ansys.synopsys.com/content/dam/amp/2024/april/case-studies/running-snail-racing/running-snail-racing-team-case-study-v2.pdf

Opublikowane (struktura, nie aero):
- bellcrank Ti: masa −40%, sztywność +56% vs frezowany odpowiednik (Ansys case)

### Walidacja
Członkowie deklarują **CFD + WT** przy skrzydłach. Brak publicznego raportu z liczbami sił / Cl dla RS24/RS25. RS25: pakiet aero drukowany — widać nacisk na szybkie iteracje geometrii i tooling.

### FW / RW / UT
- **FW:** tak (skrzydła w scope Aero Research / covers nose itd.).  
- **RW:** tak (jawny rozwój RW RS24).  
- **UT:** *prawdopodobne* w pełnym „Aerodynamikpaket”, ale **brak** jawnego opisu undertray z liczbami / screenshotami w źródłach tej rundy → oznaczamy jako **presence TBD / not confirmed in public text**.

### Liczby absolutne Cl/Cd / N aero
**Not found.** Nie cytujemy nic poza względnymi metrykami strukturalnymi Ansys.

---

## 4. Pokrewne top EU EV (krótko, dobre publiczne aero)

### Formula Student Team Delft (DUT)
FSG 2025 overall 3. Aero dept: CFD + dane torowe; DUT25 — ~**20** full-car CFD/tydzień, każda **6–12 h** na HPC (DelftBlue + ClusterVision); walidacja underbody techniką volumetric PIV („ring-of-fire”, TU Delft). Historycznie (DUT15 era): FW+RW+sidepods+undertray; skrzydła montowane na unsprung.  
Źródła: https://www.tudelft.nl/en/student/community/associations/formula-student-team-delft ; https://www.aandrijvenenbesturen.nl/jubileumauto-formula-student-team-delft/ ; https://www.linkedin.com/posts/elias-stammeijer_looking-back-on-my-third-and-final-year-activity-7373713835721142272-4pvC ; https://delta.tudelft.nl/en/article/team-duts-aerodynamic-challenge  
Cl/Cd 2024–25: **not found**. (Stary claim „upside down >100 km/h” = jakościowy, bez N.)

### TUfast (TUM) — xb024
Strona bolidu: zintegrowany pakiet **multi-element wings + full undertray + four-fan Powerground**; aktywne zarządzanie ciśnieniem front/rear fans; CFD-to-track correlation; **rear-biased balance**. Dla PUT: ciekawy opis UT+RW, ale **fan = OUT** w naszym Spec — nie przenosimy Powerground.  
Źródło: https://tufast-racingteam.de/xb024-2/  
LRZ / CoolMUC: HPC pod chassis/aero/cooling. https://www.lrz.de/en/news/detail/winning-races-with-supercomputing

### Rennstall Esslingen (Stallardo’25) — rzadkie liczby publiczne
Na stronie teamu (cornering @ 50 km/h):
- CL\*A ≈ 4,9
- CD\*A ≈ 1,65  

Plus: nowe RW flaps, tire wake management. To **×A**, nie Cx/Cz PUT — nie mieszać bez A_ref.  
Źródło: https://www.rennstall-esslingen.com/stallardo25

### eMotorsports Cologne / SimScale (benchmark metody, nie top FSG 2025)
Kolejność rozwoju **RW → FW → UT**; 2D STAR-CCM+ airfoile → 3D SimScale; FW ~**235%** bardziej efektywne niż RW (ich pakiet); rake UT **1°** → ~**+15%** DF UT; setup Accel: drag RW **−64,7%** vs high-DF.  
Źródło: https://www.simscale.com/blog/formula-student-aerodynamics/

### Joanneum Racing Graz (JR25) — pasywny skok DF
Redesign FW / side / RW; deklaracja **~+17% total downforce** vs poprzednik; strona podkreśla passive aerodynamics. Abs. Cl/Cd: **not found**.  
Źródła: https://www.joanneum-racing.at/en/jr25-en/ ; https://www.joanneum-racing.at/en/boxenstopp-43/

---

## 5. Luki (uczciwie)

| Gap | Uwaga |
|-----|--------|
| Absolutne Cl/Cd / N dla AMZ Dufour/aurona | **Not found** — tylko +25% względne i >2000 CFD |
| Absolutne Cl/Cd FaSTTUBe FT24–26 | **Not found** — tylko % z CAESES 2018 |
| Absolutne Cl/Cd Running Snail RS24/RS25 | **Not found** |
| Potwierdzenie tekstowe UT u Running Snail | Pakiet aero jest; undertray nie opisany jawnie w źródłach tej rundy |
| % balans przód/tył AMZ / FaSTTUBe / Snail | **Not found** (TUfast: „rear-biased” bez liczby) |
| Aktualny solver CFD FaSTTUBe 2025–26 | Historycznie STAR-CCM+ + CAESES; dziś strona mówi tylko „CFD” |
| Equipe / FU Berlin FS EV | **Nie istnieje** jako team FS EV — to FaSTTUBe |
| Publiczne 4-el. RW u tych trzech | **Not found** — CAESES FaSTTUBe = 3 airfoile |

---

## 6. Implikacje dla PUT (H1 RW / H2 UT, DRS OUT, fan OUT, balans ~61,6% → ~50%)

1. **H1 RW** — AMZ i historyczny FaSTTUBe traktują RW jako duży dźwignię DF (3D / multi-element, endplate DoE). CAESES pokazuje, że nawet drobne ruchy endplate + sekcji dają kilka % na full car. To wspiera agresywniejsze RW (i ewentualnie 4-el. w envelope T8) jako dźwignię cofania balansu z ~61,6% przodu. Nie mamy publicznych Cl 4-el. u top EU — to nadal nasza hipoteza CAD.

2. **H2 UT** — FaSTTUBe i Delft/TUfast trzymają **closed underbody** w centrum pakietu; Cologne i Kirchberger (KB) powtarzają, że UT jest najefektywniejszy. Przy DRS OUT i Endurance priority UT + rake/ride-height maps dają DF bez tyle dragu co samo RW. AMZ po banie powered GE wraca do pasywnego ground effect — spójne z **fan OUT**.

3. **DRS OUT** — żaden z trzech deep-dive teamów nie daje nam gotowego publicznego „low-drag flap schedule” na Endurance. Cologne pokazuje, że regulowany AoA RW potrafi ściąć drag o dziesiątki % między setupami — my musimy wziąć ten trade-off **pasywnie** (mapa AoA / flap fixed per event albo kompromis AX↔Endurance).

4. **Fan OUT** — Dufour (AMZ) i xb024 (TUfast) pokazują erę Powerground / powered GE. Reguły i nasz Spec to odcinają. Uczyć się od nich **diffuser expansion / seal / correlation**, nie od wentylatorów.

5. **Balans ~50/50** — publicznie top teamy prawie nie publikują % front DF. TUfast mówi wprost o rear-biased. My mierzymy Cm/Cz na 017: najpierw H1/H2 (więcej tyłu), potem FW jako korektor (H3), bez kopiowania Instagrama.

6. **Proces > tajne Cl** — AMZ wygrywa skalą: tysiące CFD + prawdziwy WT + korelacja 3D flow. Delft: dziesiątki full-car CFD/tydzień + PIV underbody. Running Snail: szybki print + CFD/WT na skrzydłach. Dla PUT: gonić **mapy** (ride height, rake, yaw) i korelację torową, nie pojedynczy Cl@δ=0.

7. **Berlin naming** — w kolejnych briefach pisać **FaSTTUBe (TU Berlin)**; FU Equipe odłożyć do archiwum pomyłek.

---

## Źródła (zbiorczo)

- Siemens AMZ: https://resources.sw.siemens.com/en-US/case-study-academic-motorsports-club-zurich/  
- Scientifica AMZ: https://scientifica.ch/en/event/amz-racing-from-zero-to-one-hundred-in-0-956-seconds/  
- AirShaper ProCap / AMZ: https://airshaper.com/blog/3d-flow-measurement-formula-student  
- Streamwise LinkedIn (Dufour WT): https://www.linkedin.com/posts/andrin-landolt-6aa86a6a_forumlastudent-windtunnel-aerodynamics-activity-7211262289281191936-lwuI  
- AMZ site: https://www.amzracing.ch/en  
- FaSTTUBe team: https://fasttube.de/team/  
- TU Berlin FaSTTUBe: https://www.tu.berlin/kfz/studium-lehre/seminare-studentische-projekte/fasttube  
- CAESES RW FaSTTUBe: https://www.caeses.com/blog/2018/simulation-driven-design-of-a-race-car-rear-wing/  
- FRIENDSHIP SYSTEMS FaSTTUBe: https://www.friendship-systems.com/news/2017/friendship-systems-supports-fasttube/  
- OTH RS25: https://www.oth-aw.de/hochschule/aktuelles/news/rs25-enthuellt-running-snail-startet-mit-neuem-rennwagen-in-die-saison/  
- Ansys Running Snail PDF: https://ansys.synopsys.com/content/dam/amp/2024/april/case-studies/running-snail-racing/running-snail-racing-team-case-study-v2.pdf  
- TUfast xb024: https://tufast-racingteam.de/xb024-2/  
- SimScale Cologne: https://www.simscale.com/blog/formula-student-aerodynamics/  
- Esslingen Stallardo’25: https://www.rennstall-esslingen.com/stallardo25  
- Delft / Stammeijer PIV: LinkedIn Elias Stammeijer (DUT25 aero)  

Powiązane w KB: [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md), [research-fs-teams-practice.md](research-fs-teams-practice.md), [TARGETS.md](../TARGETS.md).

*Koniec notatki. Bez inventowania Cl/Cd.*
