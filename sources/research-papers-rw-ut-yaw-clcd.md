# Przegląd literatury: tylne skrzydło (3 czy 4 elementy), podłoga w zakręcie, opublikowane liczby docisku i oporu

**Status:** Notatka badawcza do bazy źródeł, stan na 2026-09-01.  
**Język:** Polski, ton koleżeński — pełne zdania, bez telegraficznego skrótu.  
**Zakres:** Publiczne prace, tezy i strony teamów. Preferujemy materiały z EU Formula Student oraz reguł FSG dla EV; inne serie FS/FSAE oznaczamy wprost.  
**Zasada:** Każda liczba w tekście ma link, DOI albo cytat. Jeśli czegoś nie ma w źródle, piszemy **nie znaleziono**. Nic nie wymyślamy.  
**Nasz punkt wyjścia:** konfiguracja RWiter017 ma Cx **1,229**, Cz **−3,682** oraz Cm **−0,429**. Z tego wychodzi balans około **61,6%** na przód. Cel zespołu to mniej więcej pół na pół. Ruchome DRS i wentylator spod podłogi są u nas wyłączone. Rozważamy czteroelementowe tylne skrzydło oraz mocniejszą podłogę.

**Powiązane notatki w bazie:**  
[staniszewski-2023-wing.md](staniszewski-2023-wing.md) · [staniszewski-2024-energy.md](staniszewski-2024-energy.md) · [naglowski-2024-package.md](naglowski-2024-package.md) · [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md) · [research-aero-for-targets.md](research-aero-for-targets.md) · [research-balance-shift.md](research-balance-shift.md) · [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md) · [michalecki-fan-ground-effect.md](michalecki-fan-ground-effect.md)

---

## Po ludzku — o co chodziło

Szukaliśmy **otwartych** prac o trzech rzeczach, które nas bolą. Po pierwsze: czy komuś udało się opublikować porównanie **trzech versus czterech elementów** na tylnym skrzydle razem z liczbami. Po drugie: jak **podłoga i dyfuzor** zachowują się przy kącie (skręt / wiatr boczny) oraz w zakręcie i co to robi z balansem. Po trzecie: jakie wartości **Cl, Cd i balansu** leżą w tabelach dla całych pakietów Formula Student.

Wniosek w skrócie brzmi tak. **Trzyelementowe tylne skrzydło jest dobrze udokumentowane**, w tym w naszych notatkach ze Staniszewskiego i Jacksona. **Czteroelementowe skrzydło istnieje w tezach**, ale **nie znaleźliśmy uczciwego porównania head-to-head „3 vs 4 na tym samym aucie” z różnicą współczynników docisku i oporu**. Za to **mapy podłogi przy kącie i w zakręcie** oraz kilka **pełnych pakietów z liczbami** da się zebrać i tu poniżej to robimy.

---

## 1. Tylne skrzydło: trzy czy cztery elementy?

### Co już mamy w bazie (trzy elementy)

Poniższa tabela zbiera to, co już leży w bazie wiedzy o skrzydłach trzyelementowych.

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| PUT RW w Staniszewski 2023 = **3 profile**; 2D izolowane: baseline Fz≈**−398 N**, overlap −30 mm → Fz≈**−565 N** @ 15 m/s; na pojeździe Cx≈**0,72**, Cz≈**−2,03** | tabele pracy | **wysoka** | [staniszewski-2023-wing.md](staniszewski-2023-wing.md) |
| Jackson 2018 (Huddersfield, UK FS): RW **3 el.** E423; gap/overlap wg McBeath; DRS closed CL_DF **1,15**, CD **1,21**; DRS open CL **0,26**, CD **0,79** (−**35%** siły oporu) | abstract + results | **wysoka** | [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md); https://www.fieldsjournal.org.uk/article/414/galley/124/download/ |
| Top EU w otwartych źródłach traktują **3-el. RW jako default**; **brak** publicznych liczb „4-el. bije 3 o X%” u AMZ/Aachen/Delft | research-eu-fs-ev-top | **wysoka** (gap) | [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md) |

Innymi słowy: nasze własne źródła i Jackson solidnie opisują układ trzech elementów. Topowe teamy europejskie w publicznych materiałach traktują trzyelementowe RW jako domyślne rozwiązanie. Nigdzie u AMZ, Aachen ani Delft nie znaleźliśmy otwartej liczby w stylu „czwarty element bije trzeci o X procent”.

### Źródła zewnętrzne o 4 elementach / multi-element (liczby tylko wtedy, gdy naprawdę są)

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| **Dynamics UPC** (Quintanas i Yani, 2023, Manresa): w sezonie dodano **czwarty flap** do RW; motywacja = więcej parametrów setupu (kąty + gurney na 3./4. foil); w konkluzji PDF: RW generuje **240 N** docisku, druga konfiguracja flapów obniża opór całego auta o **58 N**, masa RW **7 kg** | abstract + conclusion PDF (UPCommons) | **wysoka** (istnienie 4. foila + N/kg); **średnia** (warunki CFD/V nie w abstractcie — nie porównywać 1:1 z 017) | https://hdl.handle.net/2117/396194 |
| **University of Pretoria** (FSAE, nie EU): za McBeathem zrobiono RW **4-el.** (main E423 + slat + 2 flaps S1223); JavaFoil (inviscid) CL≈**5,7**; Fluent (viscous laminar) CL≈**4,2**; FW Fluent CL≈**3,6** — to **izolowane 2D skrzydło**, nie pełne auto | paper w UP repository | **wysoka** (liczby 2D); **niska** transfer na pakiet PUT | https://repository.up.ac.za/handle/2263/62356 ; bitstream https://repository.up.ac.za/bitstreams/58f0b6ab-1b15-4838-98d1-87fd075c4911/download |
| SV-JME 2016 (SAE Formula): porównanie bazy **2 flaps** vs advanced (**slat + 1 flap**, nie „3 vs 4”): DF **162,4 N → 171,6 N** (~**+6%**) przy tym samym height | DOI | **wysoka** (Δ); **niska** jako 3vs4 | https://doi.org/10.5545/sv-jme.2016.3240 |
| Fluids MDPI 2022 (FS DRS, **3 el.** main 4° / flap1 28° / flap2 60°): 3D z aktuatorami CL≈**1,160**, CD≈**0,397**; DRS → ~**−78%** CD skrzydła — **nie** 4-el. | abstract HTML (pełny HTML MDPI czasem blokowany) | **wysoka** jako 3-el. ref. | https://doi.org/10.3390/fluids7090309 |
| LUT / Metropolia HPF026 (teza, EV FS): parametric study **secondary flaps / slot gaps** + cascade na baseline RW — focus na lap/DF trade-off, **nie** jawne „3 vs 4” z tabelą ΔCl | LUTPUB abstract | **średnia** (kierunek) | https://lutpub.lut.fi/handle/10024/171732 |
| IIUM 2017 (FS downforce package): 2-el. 2D max CL≈**3,63** (L/D 21,5) lub L/D≈**54,1** przy CL≈**2,83**; gurney **0,05·c1** → **+5,8%** DF | DOI | **średnia** (2-el., nie 3vs4) | https://doi.org/10.31436/iiumej.v18i2.679 |

Kilka zdań kontekstu do tej tabeli. UPC naprawdę dorzuciło czwarty flap w sezonie i w konkluzji PDF podaje **240 N** docisku z RW, obniżenie oporu całego auta o **58 N** przy drugiej konfiguracji flapów oraz masę RW **7 kg**. Nie mamy jednak w abstractcie pełnych warunków CFD ani prędkości, więc tych niutonów nie wolno porównywać jeden do jednego z naszym `RW_iter017`. Pretoria opisuje czteroelementowe RW według McBeatha, ale to izolowane skrzydło dwuwymiarowe. SV-JME, Fluids MDPI, LUT i IIUM dają kontekst multi-element, ale żadne z nich nie jest czystym head-to-head „trzy versus cztery elementy na tym samym aucie”.

### Werdykt tematu 1

**Opublikowanego porównania head-to-head trzech versus czterech elementów na tym samym tylnym skrzydle, z różnicą współczynników docisku i oporu/Fz, nie znaleziono.**

Czteroelementowe RW **nie jest „rzadkie jak yeti”** — UPC i Pretoria to robią albo opisują. Nie ma jednak gotowej tabeli w stylu „ile procent zysku daje czwarty element”, którą można wkleić do Specu.

Geometrię startową nadal bierzemy z McBeatha (przez Jacksona): gap **1–4%c**, overlap **1–6%c**. Ostatnie flapy ustawiamy wysoko, mniej więcej w zakresie **25–70°**, tuż przed stalem.

---

## 2. Podłoga i dyfuzor — balans przy kącie i w manewrach

### Nasze prace PUT (już w bazie)

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| UT&SW **silnie wrażliwe** na kierunek napływu; przy δ≠0 spadek sił z podłogi; FW/RW „płaskie”; nie ekstrapolować zakrętu z δ=0 | Staniszewski 2024 s. 55–56 | **wysoka** | [staniszewski-2024-energy.md](staniszewski-2024-energy.md) |
| Pełny pakiet (z UT) vs FW&RW: wyższe \|Cz\| w całym δ; Cx krzywe przecinają się ~**10°**; proxy energii toru **F2/F1 = 0,973 → −2,7%** mimo **+~10 kg** UT | wzór (20) + s. 67–68 | **wysoka** (proxy F_ham); **średnia** jako Wh | [staniszewski-2024-energy.md](staniszewski-2024-energy.md) |
| Nagłowski baseline @15 m/s: Fz_ut ≈ **−202 N** z Fz_all ≈ **−561 N** (~**36%**); balans **60,3%** przód | Tab. 5.2–5.3 | **wysoka** (ich model ≠ 017) | [naglowski-2024-package.md](naglowski-2024-package.md) |

Z naszych własnych prac wynika więc, że undertray i sidewalls mocno reagują na kierunek napływu. Przy δ różnym od zera siły z podłogi spadają, a skrzydła zachowują się względnie „płasko”. Nie wolno ekstrapolować zachowania w zakręcie z samego δ = 0. Pełny pakiet z UT daje wyższe \|Cz\| w całym zakresie δ; krzywe Cx przecinają się około **10°**. Proxy energii toru spada z **F2/F1 = 0,973** do **−2,7%**, mimo że undertray waży około **+10 kg**. U Nagłowskiego undertray daje około **36%** całego Fz przy balansie **60,3%** na przód — to jednak inny model niż `RW_iter017`.

### Chalmers CFS 2021 — tabele: jazda na wprost, zakręt, hamowanie

Źródło: De Wilde et al., *Development and performance evaluation of undertray diffusers during racing manuevers*, Chalmers BSc 2021.  
PDF: https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download  

Scenariusz zakrętu w tej pracy to R≈**12,5 m**, V≈**40 km/h**, poślizg nadwozia **3,5°**, roll **0,7°**, kąt skrętu kół około **7,2–7,4°** (Tab. 3.4).  
Uwaga metrologiczna: w tej pracy CL oznacza **współczynnik docisku** (ujemny lift zapisany jako dodatni CL), a aero balance jest podany **w stronę tyłu**.

**Tabela 4.1 — mały dyfuzor (0 mm start), komponenty:**

| Scenariusz | CD | CL | CL M&D | CL FW | CL RW | Aero balance (tył) |
|----------|---:|---:|-------:|------:|------:|-------------------:|
| Na wprost | **1,433** | **3,612** | 0,435 | 1,352 | 1,032 | **50,06%** |
| Zakręt | **1,302** | **3,544** | 0,436 | 1,325 | 0,983 | **49,90%** |
| Hamowanie (pitch ~1°) | **1,355** | **2,799** | 0,336 | 0,773 | 1,013 | **67,17%** |

**Kąt ekspansji (start 500 mm) — Tab. 4.3 (fragment):**

| Design | Scenariusz | CD | CL | CL M&D | Balance (tył) |
|--------|----------|---:|---:|-------:|--------------:|
| **13°** | Na wprost | 1,419 | **3,729** | 0,515 | 49,68% |
| **13°** | Zakręt | 1,380 | **3,603** | 0,470 | 49,38% |
| 15° | Na wprost | 1,424 | 3,640 | 0,483 | 50,36% |
| 19° | Na wprost | 1,402 | 3,663 | 0,497 | 49,35% |

Wniosek autorów brzmi następująco. Kąt **13°** wybrano za odporność w manewrach, a nie dlatego, że zawsze daje maksymalny CL w jednym punkcie. Strakes i side floors dalej pomagają. Typowa literatura startuje od około **15°**; zbyt stromy dyfuzor prowadzi do separacji.

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| Cornering przy R=12,5 m prawie nie zabija CL całego auta vs straight (**3,544 vs 3,612**), ale **braking pitch** zabija FW (−**43%** CL_FW) i cofa balans mocno do tyłu (**67%** tył) | Tab. 4.1 | **wysoka** | Chalmers PDF: https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download |
| 13° ekspansji: najwyższy CL w badanych kątach + lepsza kontrola wirów vs 15–19° | Tab. 4.3 + dyskusja | **wysoka** na CFS; **średnia** transfer | Chalmers PDF: https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download |

### Oregon State (FSAE undertray) — yaw + roll

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| UT + auto w CFD: nominal ~**50 lb** DF; przy **5° yaw** (bez roll) DF ↑ do **62 lb**; **1° roll** przy yaw obniża DF o **~6%** | § Results | **wysoka** (lb, ich model) | https://ir.library.oregonstate.edu/downloads/7h149t91w |
| Lokalizacja wejścia dyfuzora przesuwa peak podciśnienia → dźwignia **balansu** UT | literatura + design discussion | **wysoka** (kierunek) | https://ir.library.oregonstate.edu/downloads/7h149t91w |

U Oregon State nominalny docisk undertray plus auta wynosi około **50 lb**. Przy yaw **5°** bez roll docisk rośnie do **62 lb**. Dodanie **1°** roll przy yaw obniża DF o około **6%**. Lokalizacja wejścia dyfuzora przesuwa peak podciśnienia i działa jak dźwignia balansu undertray.

### FST Lisboa / Técnico — aeromap (EU EV)

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| Na FST10e **yaw** najbardziej wrażliwy: **~16%** zmiany docisku w badanym zakresie; **roll ~9%** DF i **~12%** przesunięcia CoP; ride height **~10%** CD·A i **~20%** −CL·A między peakami; mapa **>100** punktów | abstract tezy | **wysoka** na FST10e; **średnia** transfer | https://scholar.tecnico.ulisboa.pt/records/WjT08GaGU4ee77V1ZI_WgpbeDe_scfAseZd-?lang=en |

Na FST10e yaw okazał się najbardziej wrażliwym kątem: około **16%** zmiany docisku w badanym zakresie. Roll daje około **9%** zmiany DF i około **12%** przesunięcia środka ciśnienia. Ride height zmienia CD·A o około **10%** oraz −CL·A o około **20%** między peakami. Mapa ma ponad **100** punktów.

### Kirchberger / TU Wien EDGE 14 (EU EV)

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| UT generuje **~40%** docisku EDGE 14 — „most important” device w ich narracji | § Validation | **wysoka** (ich auto) | https://doi.org/10.34726/hss.2023.115880 ; PDF https://repositum.tuwien.at/bitstream/20.500.12708/188917/1/Kirchberger%20Michael%20-%202023%20-%20CFD%20Simulation%20and%20Validation%20of%20a%20Formula%20Student...pdf |
| Mesh study (half-car): CLA stagnuje ~**5,1–5,2 m²**, CDA ~**1,7 m²** na najdrobniejszych siatkach; typowy design mesh base 33 mm: CLA **4,72**, CDA **1,57**; converged run CLA **−4,66**, CDA **1,51–1,57** | Tab. 2.1–2.3 | **wysoka** (CLA/CDA = ×A) | https://doi.org/10.34726/hss.2023.115880 ; PDF https://repositum.tuwien.at/bitstream/20.500.12708/188917/1/Kirchberger%20Michael%20-%202023%20-%20CFD%20Simulation%20and%20Validation%20of%20a%20Formula%20Student...pdf |

U Kirchbergera undertray generuje około **40%** docisku EDGE 14 i w ich narracji jest „najważniejszym” urządzeniem. W mesh study half-car CLA stagnuje około **5,1–5,2 m²**, a CDA około **1,7 m²** na najdrobniejszych siatkach. Typowy design mesh z bazą 33 mm daje CLA **4,72** i CDA **1,57**. Zbieżny run to CLA **−4,66** oraz CDA **1,51–1,57**.

### Inne (modelowanie cornering)

| Twierdzenie | Skąd wiemy | Pewność | Link |
|-------|----------|------------|------|
| NTNU (Revolve context): stały yaw ≠ prawdziwy cornering (rotating flow) — efekty momentów bywają **przeciwne** do fixed-yaw | thesis abstract | **wysoka** (metoda) | http://hdl.handle.net/11250/2433712 |
| ASME JEF (Balasko/Zonta, 2025): w corneringu CLA spada **>20%** (mocniej przy małych R); możliwy **rearward** shift balansu / understeer z FW stall | abstract / guest PDF snippet | **med–high** (pełny PDF paywall) | https://doi.org/10.1115/1.4069995 |
| SAE 2017-01-5016 (under tray diffuser FS): best CFD case inlet **3°** / outlet **10°** / GC **30 mm** (L/D); słaby: 5°/16°/50 mm — **paywall abstract**, liczby z abstractu | DOI | **średnia** | https://doi.org/10.4271/2017-01-5016 |

NTNU ostrzega, że stały yaw to nie to samo co prawdziwy cornering z rotating flow — efekty momentów bywają nawet **przeciwne** do fixed-yaw. ASME JEF 2025 raportuje spadek CLA o **więcej niż 20%** w corneringu, mocniejszy przy małych promieniach, oraz możliwy rearward shift balansu albo understeer ze stallu przedniego skrzydła. SAE 2017-01-5016 podaje najlepszy przypadek CFD z inlet **3°**, outlet **10°** i ground clearance **30 mm**; słaby przypadek to 5°/16°/50 mm. Pełny tekst jest za paywallem, więc liczby bierzemy z abstractu.

### Werdykt tematu 2

Mamy **konkretne mapy i tabele** z Chalmers, Oregon, FST Lisboa oraz Staniszewskiego 2024. Wspólny obraz jest jasny. **Undertray to duży udział docisku i największa wrażliwość na yaw oraz attitude.** Braking pitch potrafi bardziej rozwalić balans niż typowy zakręt Formula Student. **Nie wolno zamrażać undertray na samym δ = 0.**

---

## 3. Opublikowane liczby docisku, oporu i balansu dla całych pakietów

> **Uwaga metrologiczna:** Cx/Cz PUT (Fluent, Aref zespołu) nie są tym samym co CLA/CDA w metrach kwadratowych, ani tym samym co Cl/Cd ze stron teamów (często bez Aref albo z DRS). **Nie wolno mieszać tych wielkości w jednym wykresie bez wspólnego Aref.**

| Źródło / kontekst | Cl / Cz / CLA | Cd / Cx / CDA | Balans | Warunki | Link | Conf. |
|-------------------|---------------|---------------|--------|---------|------|-------|
| **PUT RWiter017** (kotwica) | Cz **−3,682** | Cx **1,229** | **≈61,6%** przód (`1/2+Cm/Cz`) | 15 m/s, half-car | [research-balance-shift.md](research-balance-shift.md) | **wysoka** |
| **Nagłowski 2024** (PUT, inny model) | Cz **−4,071** | Cx **1,453** | **60,3%** przód | 15 m/s | [naglowski-2024-package.md](naglowski-2024-package.md) | **wysoka** |
| **Staniszewski 2023** 3D pojazd | Cz **−2,036** | Cx **0,726** | nie podano | 15 m/s | [staniszewski-2023-wing.md](staniszewski-2023-wing.md) | **wysoka** |
| **Jackson 2018** + RW DRS closed | CL_DF **1,15** | CD **1,21** | nie (DF głównie tył) | 26,8 m/s; A=1,18 m² | Jackson / Fields | **wysoka** |
| **Jackson** DRS open | CL_DF **0,26** | CD **0,79** | — | A=0,99 m² | [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md); https://www.fieldsjournal.org.uk/article/414/galley/124/download/ | **wysoka** |
| **Chalmers CFS** small diffuser straight | CL **3,612** | CD **1,433** | **~50%** tył | 40 km/h | Chalmers PDF Tab. 4.1 | **wysoka** |
| **Chalmers** 13° diffuser straight | CL **3,729** | CD **1,419** | 49,68% tył | 40 km/h | Tab. 4.3 | **wysoka** |
| **Kirchberger EDGE14** | CLA **≈4,66…5,2 m²** | CDA **≈1,51…1,72 m²** | — | half-car StarCCM+; mesh study | reposiTUm DOI | **wysoka** |
| **Rennstall Esslingen** Stallardo25 | CL\*A **4,9** | CD\*A **1,65** | nie znaleziono | cornering **50 km/h** (strona teamu) | https://www.rennstall-esslingen.com/stallardo25 | **wysoka** |
| **PoliTO SC24** Andromeda (EV) | ClA ≈ **4,75** | CdA ≈ **1,45** | nie znaleziono | CFD + WT Dec 2023 (teza Cravero) | https://webthesis.biblio.polito.it/35911/1/tesi.pdf | **wysoka** |
| **eForce CTU.25** (EV, **z DRS**) | Cl **−5,9** | Cd **2,02** | masa 52/48 (nie aero) | DF **320 kg @ 100 km/h**; DRS −**30%** drag | https://eforce.cvut.cz/ctu-25-en/ | **wysoka** (strona); Aref **nie podany** |
| **Wordley & Saunders / Monash 2005** (FSAE WT) | — | CD **0,83** (baseline cytowany przez Jackson) | — | WT | SAE 2006-01-0806/0808 (abstract) | **średnia** (paywall pełny tekst) |
| **AMZ / Aachen / Delft / Tallinn / Joanneum 2024–25** | **nie znaleziono** publicznych Cl/Cd pakietu konkursowego | — | **nie znaleziono** % aero | — | [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md) | **wysoka** (gap) |
| Maryland TR25 active aero (FSAE IC, **nie** EU EV) | CD **1,44 → 0,73** (−49%); CoP **78%→20%** front DF | — | active | AIAA 2026 abstract | https://doi.org/10.2514/6.2026-110799 | **średnia** (inna klasa; DRS-like) |

### MDPI CarMaker Part 2 (ART_X) — mapa Cd versus crosswind + DRS

Źródło: https://www.mdpi.com/2673-4591/79/1/77 (2024) — DRS off/on, kąty ±0…20°.

| Crosswind [°] | CD DRS off | CD DRS on |
|--------------:|----------:|----------:|
| 0 | **1,711** | **1,314** (~−25%) |
| ±5 | 1,528 | 1,173 |
| ±10 | 1,367 | 1,045 |
| ±20 | 1,190 | 0,913 |

Ta tabela jest przydatna jako **wzór mapy yaw**, a nie jako target PUT — u nas DRS jest OUT.

---

## Czego uczciwie nie znaleziono

Poniżej wypisujemy uczciwie to, czego nie znaleźliśmy albo czego nie wolno przeskalować na nasz pakiet.

1. **Brak publikacji Δ(3-el → 4-el) na tym samym RW** z Cl/Cd/Fz i wspólnym Aref. Hipoteza H1 zostaje więc **hipotezą CAD/CFD**, a nie twierdzeniem typu „literatura mówi +X%”.
2. Topowe teamy EU (AMZ, Aachen, Delft, Tallinn, Joanneum) **nie publikują** Cl/Cd ani balansu konkursowego. Mamy tylko procesy oraz rzadkie CLA/CDA (Esslingen, Kirchberger, PoliTO, CTU).
3. W Staniszewskim 2024 **konkretne Cx(δ)/Cz(δ) są tylko na wykresach**. W plain text brak tabeli punktowej — nie OCR-owano wykresów.
4. ASME cornering 2025: pełny PDF stoi za paywallem. Mamy snippet o spadku CLA **>20%**, ale nie pełną tabelę.
5. U Quintanasa liczby **240 N / 58 N / 7 kg** pochodzą z conclusion PDF (UPCommons). **Prędkość, Aref oraz to, czy pomiar dotyczy izolowanego RW czy full-car, nie zostały wyciągnięte w tej sesji z pełnego tekstu.** Nie wolno więc skalować tych wartości na `RW_iter017`.
6. CTU.25 podaje Cl/Cd **z DRS w pakiecie**. U nas DRS jest OUT. Traktujemy te liczby jako górny rząd wielkości DF, a nie jako setup do kopiowania.
7. Fan oraz powered ground effect leżą poza zakresem Specu (OUT). Szczegóły są w notatce Michalecki w KB.

---

## Co z tego wynika dla naszego zespołu

**H1 — kandydat na RW 4-elementowe.** Literatura **nie da Ci gotowego ΔCl**. Daje motywację: UPC podkreśla więcej parametrów setupu oraz ekspozycję ostatniego flapu; Pretoria i McBeath pokazują, że układ 4-elementowy jest osiągalny w boxie FSAE. Daje też ostrzeżenia: Staniszewski przypomina, że 2D nie równa się 3D coupling; UPC waży RW około **7 kg**; trzeba pilnować sztywności według T8.3. Gate dla nas: tabela na pakiecie 017 z Δbalans / ΔCx / ΔCz względem baseline 3-elementowego; Cx ≲ **1,23**, \|Cz\| ≥ **3,682**.

**H2 — undertray.** To jest **najmocniej udokumentowana** dźwignia w tym researchu. Chalmers daje **13°** plus strakes i manewry. Oregon pokazuje yaw **5°** oraz spadek około **6%** przy roll. FST Lisboa raportuje około **16%** zmiany DF od yaw. Staniszewski 2024 daje mapy δ oraz **−2,7%** proxy energii. Kirchberger przypisuje undertray około **40%** DF. Szukamy więc **tylniejszego** docisku dyfuzora **bez** dokręcania nosa przedniego skrzydła. Bramka decyzyjna: mapa Cx/Cz versus δ (plus roll/ride height, jeśli starczy budżetu) przed zamrożeniem geometrii.

**Balans 61,6% → około 50%.** Żaden top team nie opublikował instrukcji „róbcie 50% tak jak my”. Chalmers celuje w okolice **50/50** (nawet z narracją rear-biased). Nasze dźwignie to **H1 RW + H2 UT**, potem ewentualnie odciążenie FW (H3), a wąsy zostają TBD (H4). Nie dokręcamy samego przedniego skrzydła.

**DRS OUT / fan OUT.** Jackson oraz MDPI/CTU pokazują, że otwarty DRS zjada docisk. U nas w 019/020 \|Cz\| wynosi około **3,01**, czyli poniżej **3,682**. Fan jest opisany u Michaleckiego. Nie projektujemy peak-DF przez te ścieżki.

**Kolejność pracy:** H1 → H2 → (H3) → H4. Zawsze na **pełnym pakiecie** oraz przynajmniej z **mapą versus δ**.

---

## Lista źródeł

| # | Źródło | Temat | Liczby? |
|---|--------|-------|---------|
| 1 | Staniszewski 2023 (PUT) | RW 3-el. | tak |
| 2 | Staniszewski 2024 (PUT) | yaw/δ, UT | tak (proxy) |
| 3 | Nagłowski 2024 (PUT) | pakiet Fz/balans | tak |
| 4 | Jackson 2018 | RW 3-el. + DRS | tak |
| 5 | Quintanas UPC 2023 | RW **4-el.** | tak (N, kg) |
| 6 | Pretoria FSAE paper | RW 4-el. 2D CL | tak |
| 7 | Chalmers undertray 2021 | UT manewry | tak (tabele) |
| 8 | Oregon State undertray | yaw/roll UT | tak |
| 9 | FST Lisboa aeromap abstract | yaw sensitivity | tak (%) |
| 10 | Kirchberger 2023 EDGE14 | CLA/CDA, UT% | tak |
| 11 | PoliTO Cravero 2025 | ClA/CdA SC24 | tak |
| 12 | eForce CTU.25 page | Cl/Cd + DF kg | tak |
| 13 | Esslingen Stallardo25 | CL\*A/CD\*A | tak |
| 14 | MDPI Eng. Proc. 79/77 | Cd vs yaw + DRS | tak |
| 15 | SV-JME 2016 | multi-el. ΔDF | tak |
| 16 | Fluids 2022 DRS 3-el. | CL/CD skrzydła | tak |
| 17 | IIUM 2017 | 2-el. CL | tak |
| 18 | NTNU cornering CFD thesis | metoda yaw vs rotate | qualitative+ |
| 19 | ASME JEF 2025 cornering | CLA −>20% | tak (snippet) |
| 20 | LUTPUB Metropolia RW study | parametric flaps | abstract |
| 21 | research-eu-fs-ev-top (KB) | top EU gaps | meta |

**Liczba źródeł z liczbami (Cl/Cd/Fz/CLA/%/N):** **≥ 16** (wiersze 1–16 powyżej plus snippet ASME).  
**Źródła bez head-to-head 3 vs 4:** ta luka jest jawna i pozostaje otwarta.
