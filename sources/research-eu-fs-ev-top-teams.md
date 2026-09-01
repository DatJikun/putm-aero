# Research: top EV teams EU Formula Student (aero intel)

**Status:** notatka robocza pod pakiet aero PUT Motorsport (2026-09-01)  
**Język:** PL  
**Cel intel:** max DF, min drag, balans ~50/50, priorytet **Endurance + Autocross**, kandydat **RW 4-el.**, **DRS OUT**, **fan OUT**.  
**Zakres:** wyłącznie serie EU / FSG-rules (FSG, FS East, FS Austria, FS Czech, FS Netherlands, podobne). **Nie** FSAE USA, **nie** serie Asia-primary (Japonia/Chiny jako główny tor).  
**Zasada liczb:** Cl/Cd/CLA/CDA cytowane **tylko** gdy opublikowane; zdjęcia/opisy = jakościowe. Bez inventowania.

**Kotwica zespołu (kontekst):** `RW_iter017` — Cx **1,229** / Cz **−3,682** / Cm **−0,429** → balans ≈ **61,6%** przód; cel ≈ **50/50**.  
Powiązane: [research-fs-teams-practice.md](research-fs-teams-practice.md), [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md), [TARGETS.md](../TARGETS.md).

---

## 1. Metodologia

1. Zebranie wyników **overall EV** (i dyscyplin dynamicznych) z oficjalnych PDF/stron: FSG 2024–2025, FS East 2023–2024 (2025 odwołane), FS Austria 2024–2025, FS Czech 2025 (via FS World Ranking), uzupełniająco Elo GET-Racing / FS World Ranking.
2. Lista do **~30** silnych teamów EV z Europy (kraj + wyniki). Priorytet: podium / top-10 na FSG/FSA/FS Czech / WRL.
3. Dla top ~15: przegląd stron teamów, Instagram/LinkedIn (publiczne), case studies partnerów (SimScale, Siemens), GitHub/YouTube/tezy uniwersyteckie pod kątem **aero**: FW/RW/UT, CFD, Cd/Cl, balans, DRS, open-wheel photos.
4. Confidence: **high** = oficjalny wynik / cytat z tezy lub strony z liczbą; **med** = opis teamu / blog partnera bez pełnych warunków CFD; **low** = wzmianka jakościowa / PR bez metodologii.

### Źródła wyników (linki)

| Event / źródło | Link |
|----------------|------|
| FSG 2025 Overall Results v3 | https://dev13.fs-g.org/uploads/tx_fsg/scoring2/pdf/FSG25_Overall_Results_v3_rp00019.pdf |
| FSG 2025 winners (news) | https://www.formulastudent.de/pr/news/details/article/20-years-of-formula-student-germany-a-milestone-at-hockenheimring |
| FSG 2024 overall (news) | https://www.formulastudent.de/pr/news/details/article/formula-student-germany-2024-concludes-with-spectacular-racing-and-celebration |
| FSG results hub 2025 | https://www.formulastudent.de/fsg/results/2025 |
| FS Austria 2025 E-Overall | https://fsaustria.at/wp-content/uploads/E_Overall_Results_2025.pdf |
| FS Austria 2024 E-Overall | https://fsaustria.at/wp-content/uploads/E_Overall_Results_2024_v2.pdf |
| FS East 2024 EV Final | https://fseast.eu/wp-content/uploads/2024/08/FS_EAST_2024_EV_Final.pdf |
| FS East 2023 EV | https://fseast.eu/wp-content/uploads/2023/08/FS-East-2023-EV-results_1.2.pdf |
| FS Czech 2025 (WRL event page) | https://fs-world.org/competition/15/event/354 |
| FS Czech results hub | https://fsczech.cz/results-2025/ |
| Elo FS East 2024 EV | https://fselo.get-racing.de/elo_website_electric/comp/2024-EA-ELECTRIC.html |
| FSG team cards (przykł. Aachen) | https://www.formulastudent.de/teams/fse/details/tid/258 |

---

## 2. Rankingi — skrót (EV)

### FSG 2025 (Hockenheim) — Overall
1. **ETH Zürich / AMZ** — 926,54  
2. **RWTH Aachen / Ecurie Aix** — 847,14  
3. **TU Delft** — 819,87  
4. TUM / munichMotorsport — 793,10  
5. Uni Stuttgart / Rennteam — 771,78  
6. Politecnico Milano / Dynamis PRC — 766,99  
7. NTNU / Revolve — 707,71  
8. Chalmers — 704,08  
9. DHBW Stuttgart — 672,16  
10. OTH Amberg / Running Snail — 651,56  
… Tallinn 12., Esslingen 13., eForce Prague / CTU 11., TU Wien 16., KIT 21.

Źródło: FSG25 Overall Results v3.

### FSG 2024 — Overall EV
1. **ETH Zürich / AMZ**  
2. **Tallinn TU UAS / FS Team Tallinn**  
3. **CTU Prague / eForce**  

Źródło: FSG news 2024-08-19.

### FS Austria 2025 — E Overall
1. **FH Joanneum Graz / Joanneum Racing** — 916,2  
2. Uni Stuttgart — 854,9  
3. Politecnico Milano — 845,4  
4. HS Esslingen / Rennstall — 831,2  
5. Uni Innsbruck / Campus Tirol — 821,8  
6. TUM — 783,7  

Źródło: E_Overall_Results_2025.pdf.

### FS Czech 2025 — EV Overall (WRL)
1. **UAS Graz / Joanneum** — 929  
2. **ETH Zürich** — 894  
3. **NTNU Trondheim / Revolve** — 865  
4. PT Milano / Dynamis — 790  
5. CTU Prague — 751  

Źródło: fs-world.org event 354.

### FS East 2024 — EV (skrót dynamicznych / Elo)
Silni: **AMZ**, **Tallinn**, **KIT**, **munichMotorsport**, **TU Graz**, Revolve, Aachen, Esslingen.  
FS East **2025 odwołane**.

### WRL / kontekst 2025
Po sezonie 2025: **AMZ #1**, **Joanneum #2** (komunikat FH JOANNEUM). Tallinn był #1 WRL po sezonie 2024.

---

## 3. Lista ~30 silnych teamów EV (EU)

| # | Team | Kraj | Notable results (2023–2026) |
|---|------|------|------------------------------|
| 1 | AMZ Racing (ETH Zürich) | CH | FSG 2024 & 2025 overall 1.; FS East 2024 1.; FS Czech 2025 2.; WRL #1 (2025) |
| 2 | Ecurie Aix (RWTH Aachen) | DE | FSG 2025 overall 2.; AX FSG25 1.; FSA25 AX 1. (bez Endurance) |
| 3 | Formula Student Team Delft | NL | FSG 2025 overall 3.; FSG25 Skidpad 2.; silny ED |
| 4 | Joanneum Racing Graz | AT | FSA 2025 1.; FS Czech 2025 1.; WRL #2 (2025) |
| 5 | FS Team Tallinn | EE | FSG 2024 2.; Endurance FSG24 1.; FSA24 1.; WRL #1 (2024) |
| 6 | Rennteam Uni Stuttgart (ex-GreenTeam) | DE | FSA 2025 2.; FSG 2025 5.; Endurance FSG25 2. |
| 7 | Dynamis PRC (Politecnico di Milano) | IT | FSA 2025 3.; FS Czech 2025 4.; FSG 2025 6. |
| 8 | Revolve NTNU | NO | FS Czech 2025 3.; FSG 2025 7.; ED top |
| 9 | Rennstall Esslingen | DE | FSA 2025 4.; Endurance FSA25 2.; AX FSA25 3. |
| 10 | munichMotorsport / TUM | DE | FSG 2025 4.; Efficiency FSG25 1.; FSNL 2025 1. |
| 11 | KA-RaceIng (KIT) | DE | FS East 2024 top; FSG ED top; DC silny |
| 12 | Campus Tirol Motorsport (Innsbruck) | AT | FSA 2025 5.; Accel FS Czech 2025 1. |
| 13 | eForce Prague Formula (CTU) | CZ | FSG 2024 3.; FS Czech 2025 5.; FSG 2025 11. |
| 14 | Chalmers Formula Student | SE | FSG 2025 8.; DC FSG25 1. |
| 15 | TU Wien Racing | AT | FSG 2025 16.; teza Kirchberger EDGE14 (aero) |
| 16 | TU Graz Racing Team | AT | FS East / FSA top dynamiczne; FSA25 silny przed Endurance DNF |
| 17 | Elbflorace (TU Dresden) | DE | FSA 2025 10.; Skidpad FSG25 1. |
| 18 | DHBW Stuttgart | DE | FSG 2025 9.; AX FSG25 3. |
| 19 | Running Snail (OTH Amberg) | DE | FSG 2025 10.; Endurance FSG25 4. |
| 20 | URE / TU Eindhoven | NL | FSNL 2025 2.; FSG 2025 22. |
| 21 | Formula Electric Belgium / UGent | BE | WRL / FS Czech mid-pack; SimScale case (Cologne pokrewne w KB) |
| 22 | ETSEIB / UPC Barcelona | ES | FSG 2025 15.; FSA mid |
| 23 | High Speed Karlsruhe (UAS) | DE | Cost/BP silne; FSG mid |
| 24 | Bern Racing Team | CH | FSG / East mid-top |
| 25 | Superior Engineering (Ljubljana) | SI | FS East regular |
| 26 | RaceUP Electric (Padova) | IT | FS East / EU regular EV |
| 27 | BME Formula Racing | HU | FS East / lokalne top HU |
| 28 | Formula Student Team Weingarten | DE | FSA / FS Czech; AX FS Czech 2025 2. |
| 29 | Oxford Brookes Racing | UK | FS Czech 2025 top-15 (starty EU) |
| 30 | PUT Motorsport | PL | kontekst własny; FSG 2025 ~68. overall |

*(Monash / Montréal pojawiają się w wynikach EU, ale to nie teamy EU-primary — pominięte w „~30 EU”.)*

---

## 4. Tabela aero (priorytet top ~15+)

| Team | Event / wynik | Aero notes (tylko opublikowane / jakościowe) | Link | Conf. |
|------|---------------|-----------------------------------------------|------|-------|
| **AMZ Racing** | FSG25 1.; FSG24 1.; WRL#1 | Pełny pakiet FW+RW+UT; FSG card: „3D front and rear wings”, tire wake control; Scientifica: **>2000** simów CFD + walidacja WT; po **banie powered ground effect** (aurona): redesign konceptu, −20 kg — **nie** fan na autach konkursowych post-ban. Osobny projekt accel z fanami = **nie** transfer do Spec (fan OUT). **Brak** publicznych Cl/Cd pakietu konkursowego. | https://www.amzracing.ch/en ; FSG tid; https://scientifica.ch/en/event/amz-racing-from-zero-to-one-hundred-in-0-956-seconds/ | high (proces); **n/a** Cl/Cd |
| **Ecurie Aix** | FSG25 2.; AX1 | eax04: priorytet „high downforce + efficiency”; **redesigned undertray and rear wing**; lightest aero package w serii eax; radiators **on undertray**; STAR-CCM+ (Siemens case: aero DF/drag + cooling). eax05: dalsze optymalizacje aero. **Brak** opublikowanych Cl/Cd. | https://ecurie-aix.de ; https://www.formulastudent.de/teams/fse/details/tid/258 ; Siemens Simcenter case | high (opis); Cl/Cd **not found** |
| **DUT Delft** | FSG25 3. | Historycznie: FW+RW+sidepods+undertray/diffuser; OpenFOAM; skrzydła na unsprung (DUT15); DUT14: **725 N** DF @ **60 km/h** (RW+FW+diffuser) — **stary** bolid, inna regulacja. Współczesne liczby Cl/Cd **not found** w otwartych źródłach 2024–25. | https://delta.tudelft.nl/en/article/team-duts-aerodynamic-challenge ; Racecar Engineering DUT14/15 | med–high (historyczne N); transfer **low** |
| **Joanneum Racing** | FSA25 1.; FSCZ25 1. | JR25: **redesigned front, side and rear wing**; deklaracja **~+17% total downforce** vs poprzednik; **passive aerodynamics** (strona JR25: „even with passive aerodynamics”). **Brak** absolutnych Cl/Cd. | https://www.joanneum-racing.at/en/boxenstopp-43/ ; https://www.joanneum-racing.at/en/jr25-en/ | high (+17% względne); abs. **not found** |
| **FS Team Tallinn** | FSG24 2.; Endurance king | Star-CCM+; pełny aero package (FW→underbody); LinkedIn: nacisk na quality kompozytów vs CFD; historyczna teza DRS (FEST18) — **nie** oznacza DRS na obecnych autach. FSG card: „strong aero package… validated in-house”. Cl/Cd **not found**. | https://www.formulastudent.ee/ ; LinkedIn FSTT; digikogu TalTech (DRS thesis) | med |
| **Rennteam Stuttgart** | FSA25 2.; FSG25 5. | Revised FW+RW; wąskie monocoque → więcej powierzchni skrzydeł; 3D-printed flap ribs (side wing); CFRP aero. Cl/Cd **not found**. | https://www.formulastudent.de/teams/fse/details/tid/224 ; INTAMSYS case | med |
| **Dynamis PRC** | FSA25 3.; FSCZ25 4. | OpenFOAM / SimScale; **aero maps** ride height / rake; V=**16 m/s** w case; mesh ~20–25M; +**12,5%** DF vs poprzednik (case DP12 era); hollow laminate wings; nacisk na endplates RW ↔ UT ↔ tire wake; FW load distribution across span. Cl/Cd punktowe w case: wykresy, **bez** jednej pary „Cl=… Cd=…” w tekście. | https://www.simscale.com/blog/dynamis-prc/ ; LinkedIn aero leads | high (metoda); Cl/Cd abs. **not found** |
| **Revolve NTNU** | FSCZ25 3. | CFRP wing package; HPC CFD (**>1300** iteracji / sezon — Sigma2); multi-element high-lift airfoils; teza 2016: RW **3-element** WT validation; Realizable k-ε w pracy. Współczesne Cl/Cd **not found**. | https://www.revolve.no/ ; https://www.sigma2.no/research/speedy-cars-hpc ; NTNU thesis hdl.handle.net/11250/2433712 | high (proces); Cl/Cd **not found** |
| **Rennstall Esslingen** | FSA25 4. | **Opublikowane:** cornering @ **50 km/h**: **CL\*A = 4,9** ; **CD\*A = 1,65**; nowe RW flaps; tire wake management; aero dostosowane do zmian zawieszenia. | https://www.rennstall-esslingen.com/stallardo25 | **high** (liczby na stronie teamu) |
| **munichMotorsport / TUM** | FSG25 4.; Eff 1. | Silny wynik Endurance+Efficiency → pakiet realnie efektywny; szczegóły Cl/Cd **not found** w tej sesji. | FSG25 Overall PDF | low (wynik); aero detale **gap** |
| **KA-RaceIng** | East/FSG ED | Subteam: FW, RW, sidepods, undertray; CFD + pitot; FSG: „complex aerodynamic package”; historycznie „active aerodynamics” na starszych autach — status 2025 **niezweryfikowany** (nie zakładać DRS). Cl/Cd **not found**. | https://www.ka-raceing.de/subteams.html ; FSG tid/254 | med |
| **Campus Tirol** | FSA25 5. | AERIS: FW+side+RW carbon; **geschlossener Unterboden**; **„Aktive Aerodynamik”** (strona — bez detaili DRS/fan); „Abtrieboptimiertes” pakiet. Cl/Cd **not found**. | https://ct-motorsport.at/aeris/ | med (jakościowe); aktywne aero = **uwaga** vs Spec DRS OUT |
| **eForce Prague** | FSG24 3.; FSCZ25 5. | Silny ED / dynamika; publiczne Cl/Cd EV **not found**. (Strona eforce.cvut.cz/fs13 dotyczy **CV** CarTech — **nie** cytować 157 kg DF jako EV.) | https://eforce.cvut.cz/ ; FSG/WRL | low–med |
| **Chalmers** | FSG25 8.; DC1 | Wyniki dynamiczne; aero detale **not found** w tej sesji. | FSG25 | low |
| **TU Wien Racing** | FSG25 16. | Kirchberger 2023 (EDGE 14): StarCCM+, half-car, inlet **15 m/s**; CLA ≈ **4,66…5,2 m²**, CDA ≈ **1,51…1,72 m²**; A≈**1,19 m²**; UT ~**40%** DF; CFD zwykle **nadmiarowe** vs pressure taps. | https://repositum.tuwien.at/handle/20.500.12708/188917 | **high** (teza) |
| **eMotorsports Cologne** | (benchmark EU, nie top-2025) | SimScale: rozwój **RW→FW→UT**; UT „most efficient”; FW ~**235%** bardziej efektywne niż RW (ich pakiet); rake UT **1°** → ~**+15%** DF UT; setup Accel RW drag **−64,7%** vs high-DF. | https://www.simscale.com/blog/formula-student-aerodynamics/ | high (blog); transfer **med** |

---

## 5. Wzorce użyteczne dla H1–H5 (PUT)

Kontekst hipotez: [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md) — H1 RW, H2 UT/dyfuzor, H3 FW/balance, H4 wąsy TBD, H5 fan OUT.

### H1 — RW (więcej tyłu / ewentualnie 4-el.)
- Top teamy **zawsze** mają agresywne multi-element RW; Esslingen jawnie iteruje **Heckflügel flaps**; Dynamis: endplates RW + interakcja z UT i tire wake; Revolve: high-lift multi-el. + setki/tysiące CFD.
- **3-el.** jest domyślnym „stanem sztuki” w otwartych tezach (Revolve WT, Jackson, Staniszewski) — **4-el. nie jest udokumentowane liczbami** u top EU; to nadal **hipoteza CAD** PUT w envelope T8.
- Po banie powered GE u AMZ nacisk wraca na **pasywny** high-DF package (skrzydła 3D + UT) — spójne z fan OUT.
- **Implikacja:** H1 słuszny kierunek pod cofanie balansu; nie oczekiwać publicznych „Cl 4-el.” jako benchmarku.

### H2 — UT / dyfuzor (tylny udział, efektywność)
- Powtarzalny claim: UT = **najefektywniejszy** generator DF (Cologne; Kirchberger UT ~40%; Centaurus/literature w KB).
- Aachen: radiators **on undertray** — packaging chłodzenia ≠ osobny drag sidepodów.
- Dynamis: **aero maps** FRH×RRH / rake @ ~16 m/s — to jest praktyka top EU pod Endurance/AX, nie pojedynczy Cl@δ=0.
- Campus Tirol / wszyscy top: **closed underbody**.
- Esslingen CLA/CDA (**4,9 / 1,65** @ 50 km/h cornering) = rzadki publiczny punkt odniesienia rzędu wielkości (to **×A**, nie Cx/Cz PUT — nie mieszać bez A_ref).
- **Implikacja:** H2 klucz pod L/D i Endurance przy DRS OUT; mapy yaw/ride height przed zamrożeniem.

### H3 — FW / balans ~50/50
- Dynamis: FW projektowany na **rozkład obciążenia po rozpiętości** i różne attitudes (nie tylko max Fz).
- Tallinn / Aachen / Joanneum: pełny redesign FW razem z RW przy skoku DF.
- Publikowane cele balansu w literaturze FS wahają się (~41% CoP Hogea … ~56% Orion … ~57–62% PUT) — cel PUT **~50/50** jest w środku chmury; top EU **nie publikuje** % front DF.
- **Implikacja:** nie kopiować „balansu mistrza” z Instagrama — mierzyć Cm/Cz na 017; FW jako korektor po H1/H2.

### H4 — wąsy / side devices
- Joanneum: **side wing** w redesignie (+17% DF pakietu).
- Stuttgart: side-wing flap ribs (topology-optimized print).
- Cologne / Dynamis: sidepods / downwashing / tire wake plates.
- **Implikacja:** side devices są standardem top EU; wąsy S1223 PUT = osobna decyzja TBD — brak publicznych Cl wąsów u FSG winners.

### H5 — fan / active
- **Fan / powered GE:** AMZ miał erę powered GE; **zabronione** → redesign aurona. Spec PUT: **fan OUT** — zgodne z aktualnymi regułami/trendem konkursowym.
- **DRS / active:** Tallinn historycznie DRS thesis; Campus Tirol deklaruje „Aktive Aerodynamik”; KA historycznie active aero. Przy Spec **DRS ruchomy OUT** — uczyć się z **pasywnego** trade-offu (Esslingen CLA/CDA, Cologne Accel setup drag cut, Joanneum „passive” + wyniki Endurance).
- **Implikacja:** H5 pozostaje OUT; Endurance wygrywa się niezawodnością + efektywnością pasywnego pakietu (Tallinn Endurance, Joanneum Efficiency/AX, TUM Efficiency FSG25).

### Endurance + Autocross (priorytet Spec)
- Zwycięzcy overall łączą **mocny AX** z **ukończonym / szybkiego Endurance** (AMZ, Joanneum, Tallinn historycznie).
- Aachen FSA25: AX **100 pkt**, ale **0** Endurance → overall tylko 14. — ostrzeżenie: sam max DF bez niezawodności nie wygrywa sezonu.
- Przy DRS OUT: cel Cx ≲ 1,23 przy |Cz|≥3,682 jest spójny z tym, że top teamy nie „wyłączają” skrzydeł na prostych w EV ruleset EU.

---

## 6. Czego **nie** znaleziono (honest gaps)

| Gap | Uwaga |
|-----|-------|
| Publiczne **Cl/Cd** (bezwymiarowe) pakietów AMZ / Aachen / Delft 2024–25 / Tallinn / Joanneum | **Nie opublikowane** w otwartych źródłach tej sesji |
| % balans przód/tył top FSG winners | **Not found** |
| Potwierdzenie **4-element RW** u top EU z liczbami | Tylko 3-el. w tezach otwartych; 4-el. = hipoteza PUT |
| Szczegóły geometrii UT (kąty dyfuzora, liczba tuneli) top 5 | Brak CAD/CFD screenshots z liczbami |
| Aktualny status DRS u Campus Tirol / KA 2025 | Tylko hasło „active”; bez procedury / legalności sezonu |
| YouTube/IG CFD screenshots z czytelnymi Cl | Przegląd jakościowy ograniczony; brak wiarygodnych frame-grabs z metrykami |
| Pełne FSG 2023 EV podium w tej notatce | Skupiono 2024–2025 + East/FSA/Czech |
| eForce EV absolute DF | FS.13 na domenie eForce = **CV** — nie mieszać |
| GitHub aero repos top teamów | Nie znaleziono publicznych pełnych modeli CAD/CFD |

**Nie inventowano** żadnych Cl/Cd. Jedyna świeża para opublikowana wprost przez team EU w tej rundzie: **Esslingen CL\*A 4,9 / CD\*A 1,65 @ 50 km/h cornering** (+ Kirchberger CLA/CDA z tezy 2023 + historyczne 725 N Delft).

---

## 7. Shortlista „co podglądać” pod PUT Spec

1. **Esslingen Stallardo’25** — rzadkie CLA/CDA; tire-wake + RW flaps.  
2. **Dynamis aero maps** — metoda, nie liczby.  
3. **Kirchberger / EDGE14** — UT udział + walidacja CFD vs tor.  
4. **Joanneum JR25** — skok DF pasywnym FW/side/RW bez fan/DRS.  
5. **Aachen eax04/05** — UT redesign + radiators on UT + light aero.  
6. **AMZ** — skala CFD/WT i wake management; **nie** fan car.

---

*Koniec notatki. Aktualizacja: 2026-09-01 (Europe/Warsaw).*
