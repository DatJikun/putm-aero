# Research papers: RW 3 vs 4 el. · UT/yaw · Cl/Cd/balans (FS / FSAE)

**Status:** notatka badawcza Źródła (2026-09-01)  
**Język:** PL, ton koleżeński  
**Zakres:** publiczne prace / tezy / strony teamów; preferencja EU FS / FSG-rules EV; inne FS/FSAE oznaczone.  
**Zasada:** każda liczba z linkiem/DOI/cytatem; brak = **nie znaleziono**. Bez inventowania.  
**Kotwica PUT:** `RW_iter017` — Cx **1,229** / Cz **−3,682** / Cm **−0,429** → balans ≈ **61,6%** przód; cel ≈ **50/50**; **DRS OUT**, **fan OUT**; H1 = RW 4-el. kandydat; H2 = UT.

**Cross-linki w KB:**  
[staniszewski-2023-wing.md](staniszewski-2023-wing.md) · [staniszewski-2024-energy.md](staniszewski-2024-energy.md) · [naglowski-2024-package.md](naglowski-2024-package.md) · [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md) · [research-aero-for-targets.md](research-aero-for-targets.md) · [research-balance-shift.md](research-balance-shift.md) · [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md) · [michalecki-fan-ground-effect.md](michalecki-fan-ground-effect.md)

---

## Intro (po ludzku)

Szukaliśmy **otwartych** prac o trzech rzeczach, które nas bolą: (1) czy komuś udało się opublikować **3 vs 4 elementy** na tylnym skrzydle z liczbami, (2) jak **podłoga/dyfuzor** zachowuje się w yaw/skręcie i co to robi z balansem, (3) jakie **Cl/Cd/balans** leżą w tabelach dla całych pakietów FS. Wniosek w skrócie: **3-elementowe RW jest dobrze udokumentowane** (w tym nasze Staniszewski/Jackson); **4-elementowe istnieje w tezach**, ale **brak uczciwego head-to-head „3 vs 4 na tym samym aucie” z ΔCl/Cd**; za to **yaw/cornering mapy UT** i kilka **pełnych pakietów z liczbami** da się zebrać.

---

## 1) Multi-element rear wing: 3 vs 4 elementy

### Co już mamy w KB (3 el.)

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| PUT RW w Staniszewski 2023 = **3 profile**; 2D izolowane: baseline Fz≈**−398 N**, overlap −30 mm → Fz≈**−565 N** @ 15 m/s; na pojeździe Cx≈**0,72**, Cz≈**−2,03** | tabele pracy | **high** | [staniszewski-2023-wing.md](staniszewski-2023-wing.md) |
| Jackson 2018 (Huddersfield, UK FS): RW **3 el.** E423; gap/overlap wg McBeath; DRS closed CL_DF **1,15**, CD **1,21**; DRS open CL **0,26**, CD **0,79** (−**35%** siły oporu) | abstract + results | **high** | [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md); https://www.fieldsjournal.org.uk/article/414/galley/124/download/ |
| Top EU w otwartych źródłach traktują **3-el. RW jako default**; **brak** publicznych liczb „4-el. bije 3 o X%” u AMZ/Aachen/Delft | research-eu-fs-ev-top | **high** (gap) | [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md) |

### Źródła zewnętrzne o 4 el. / multi-el. (liczby tylko gdy są)

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| **Dynamics UPC** (Quintanas i Yani, 2023, Manresa): w sezonie dodano **czwarty flap** do RW; motywacja = więcej parametrów setupu (kąty + gurney na 3./4. foil); w konkluzji PDF: RW generuje **240 N** docisku, druga konfiguracja flapów obniża opór całego auta o **58 N**, masa RW **7 kg** | abstract + conclusion PDF (UPCommons) | **high** (istnienie 4. foila + N/kg); **med** (warunki CFD/V nie w abstractcie — nie porównywać 1:1 z 017) | https://hdl.handle.net/2117/396194 |
| **University of Pretoria** (FSAE, nie EU): za McBeathem zrobiono RW **4-el.** (main E423 + slat + 2 flaps S1223); JavaFoil (inviscid) CL≈**5,7**; Fluent (viscous laminar) CL≈**4,2**; FW Fluent CL≈**3,6** — to **izolowane 2D skrzydło**, nie pełne auto | paper w UP repository | **high** (liczby 2D); **low** transfer na pakiet PUT | https://repository.up.ac.za/handle/2263/62356 ; bitstream https://repository.up.ac.za/bitstreams/58f0b6ab-1b15-4838-98d1-87fd075c4911/download |
| SV-JME 2016 (SAE Formula): porównanie bazy **2 flaps** vs advanced (**slat + 1 flap**, nie „3 vs 4”): DF **162,4 N → 171,6 N** (~**+6%**) przy tym samym height | DOI | **high** (Δ); **low** jako 3vs4 | https://doi.org/10.5545/sv-jme.2016.3240 |
| Fluids MDPI 2022 (FS DRS, **3 el.** main 4° / flap1 28° / flap2 60°): 3D z aktuatorami CL≈**1,160**, CD≈**0,397**; DRS → ~**−78%** CD skrzydła — **nie** 4-el. | abstract HTML (pełny HTML MDPI czasem blokowany) | **high** jako 3-el. ref. | https://doi.org/10.3390/fluids7090309 |
| LUT / Metropolia HPF026 (teza, EV FS): parametric study **secondary flaps / slot gaps** + cascade na baseline RW — focus na lap/DF trade-off, **nie** jawne „3 vs 4” z tabelą ΔCl | LUTPUB abstract | **med** (kierunek) | https://lutpub.lut.fi/handle/10024/171732 |
| IIUM 2017 (FS downforce package): 2-el. 2D max CL≈**3,63** (L/D 21,5) lub L/D≈**54,1** przy CL≈**2,83**; gurney **0,05·c1** → **+5,8%** DF | DOI | **med** (2-el., nie 3vs4) | https://doi.org/10.31436/iiumej.v18i2.679 |

### Werdykt tematu 1

- **Opublikowane head-to-head 3 vs 4 elementy na tym samym RW z ΔCl/Cd/Fz: nie znaleziono.**
- **4-el. RW nie jest „rzadkie jak yeti”** — UPC i Pretoria to robią / opisują — ale **nie ma gotowej tabeli „ile % zysku za 4. element”**, którą można wkleić do Spec.
- Geometria startowa nadal z McBeathem (przez Jackson): gap **1–4%c**, overlap **1–6%c**; ostatnie flapy wysoko (~25–70°) przed stall.

---

## 2) Undertray / dyfuzor + balans w yaw / steer / cornering

### PUT (już w KB)

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| UT&SW **silnie wrażliwe** na kierunek napływu; przy δ≠0 spadek sił z podłogi; FW/RW „płaskie”; nie ekstrapolować zakrętu z δ=0 | Staniszewski 2024 s. 55–56 | **high** | [staniszewski-2024-energy.md](staniszewski-2024-energy.md) |
| Pełny pakiet (z UT) vs FW&RW: wyższe \|Cz\| w całym δ; Cx krzywe przecinają się ~**10°**; proxy energii toru **F2/F1 = 0,973 → −2,7%** mimo **+~10 kg** UT | wzór (20) + s. 67–68 | **high** (proxy F_ham); **med** jako Wh | j.w. |
| Nagłowski baseline @15 m/s: Fz_ut ≈ **−202 N** z Fz_all ≈ **−561 N** (~**36%**); balans **60,3%** przód | Tab. 5.2–5.3 | **high** (ich model ≠ 017) | [naglowski-2024-package.md](naglowski-2024-package.md) |

### Chalmers CFS 2021 — pełne tabele straight / cornering / braking (EU FS EV)

Źródło: De Wilde et al., *Development and performance evaluation of undertray diffusers during racing manuevers*, Chalmers BSc 2021.  
PDF: https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download  
Scenariusz cornering: R≈**12,5 m**, V≈**40 km/h**, body slip **3,5°**, roll **0,7°**, steer ~**7,2–7,4°** (Tab. 3.4).  
Uwaga: w tej pracy CL = **współczynnik docisku** (ujemny lift jako dodatni CL); aero balance podany **rearwards**.

**Tabela 4.1 — mały dyfuzor (0 mm start), komponenty:**

| Scenario | CD | CL | CL M&D | CL FW | CL RW | Aero balance (tył) |
|----------|---:|---:|-------:|------:|------:|-------------------:|
| Straight | **1,433** | **3,612** | 0,435 | 1,352 | 1,032 | **50,06%** |
| Cornering | **1,302** | **3,544** | 0,436 | 1,325 | 0,983 | **49,90%** |
| Braking (pitch ~1°) | **1,355** | **2,799** | 0,336 | 0,773 | 1,013 | **67,17%** |

**Kąt ekspansji (start 500 mm) — Tab. 4.3 (fragment):**

| Design | Scenario | CD | CL | CL M&D | Balance (tył) |
|--------|----------|---:|---:|-------:|--------------:|
| **13°** | Straight | 1,419 | **3,729** | 0,515 | 49,68% |
| **13°** | Cornering | 1,380 | **3,603** | 0,470 | 49,38% |
| 15° | Straight | 1,424 | 3,640 | 0,483 | 50,36% |
| 19° | Straight | 1,402 | 3,663 | 0,497 | 49,35% |

Wniosek autorów: **13°** wybrane za **robustness** w manewrach (nie zawsze max CL w jednym punkcie); strakes/side floors dalej pomagają; typowo literatura ~**15°** jako start, zbyt stromy → separacja.

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| Cornering przy R=12,5 m prawie nie zabija CL całego auta vs straight (**3,544 vs 3,612**), ale **braking pitch** zabija FW (−**43%** CL_FW) i cofa balans mocno do tyłu (**67%** tył) | Tab. 4.1 | **high** | Chalmers PDF j.w. |
| 13° ekspansji: najwyższy CL w badanych kątach + lepsza kontrola wirów vs 15–19° | Tab. 4.3 + dyskusja | **high** na CFS; **med** transfer | j.w. |

### Oregon State (FSAE undertray) — yaw + roll

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| UT + auto w CFD: nominal ~**50 lb** DF; przy **5° yaw** (bez roll) DF ↑ do **62 lb**; **1° roll** przy yaw obniża DF o **~6%** | § Results | **high** (lb, ich model) | https://ir.library.oregonstate.edu/downloads/7h149t91w |
| Lokalizacja wejścia dyfuzora przesuwa peak podciśnienia → dźwignia **balansu** UT | literatura + design discussion | **high** (kierunek) | j.w. |

### FST Lisboa / Técnico — aeromap (EU EV)

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| Na FST10e **yaw** najbardziej wrażliwy: **~16%** zmiany docisku w badanym zakresie; **roll ~9%** DF i **~12%** przesunięcia CoP; ride height **~10%** CD·A i **~20%** −CL·A między peakami; mapa **>100** punktów | abstract tezy | **high** na FST10e; **med** transfer | https://scholar.tecnico.ulisboa.pt/records/WjT08GaGU4ee77V1ZI_WgpbeDe_scfAseZd-?lang=en |

### Kirchberger / TU Wien EDGE 14 (EU EV)

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| UT generuje **~40%** docisku EDGE 14 — „most important” device w ich narracji | § Validation | **high** (ich auto) | https://doi.org/10.34726/hss.2023.115880 ; PDF https://repositum.tuwien.at/bitstream/20.500.12708/188917/1/Kirchberger%20Michael%20-%202023%20-%20CFD%20Simulation%20and%20Validation%20of%20a%20Formula%20Student...pdf |
| Mesh study (half-car): CLA stagnuje ~**5,1–5,2 m²**, CDA ~**1,7 m²** na najdrobniejszych siatkach; typowy design mesh base 33 mm: CLA **4,72**, CDA **1,57**; converged run CLA **−4,66**, CDA **1,51–1,57** | Tab. 2.1–2.3 | **high** (CLA/CDA = ×A) | j.w. |

### Inne (cornering modeling)

| Claim | Evidence | Confidence | Link |
|-------|----------|------------|------|
| NTNU (Revolve context): stały yaw ≠ prawdziwy cornering (rotating flow) — efekty momentów bywają **przeciwne** do fixed-yaw | thesis abstract | **high** (metoda) | http://hdl.handle.net/11250/2433712 |
| ASME JEF (Balasko/Zonta, 2025): w corneringu CLA spada **>20%** (mocniej przy małych R); możliwy **rearward** shift balansu / understeer z FW stall | abstract / guest PDF snippet | **med–high** (pełny PDF paywall) | https://doi.org/10.1115/1.4069995 |
| SAE 2017-01-5016 (under tray diffuser FS): best CFD case inlet **3°** / outlet **10°** / GC **30 mm** (L/D); słaby: 5°/16°/50 mm — **paywall abstract**, liczby z abstractu | DOI | **med** | https://doi.org/10.4271/2017-01-5016 |

### Werdykt tematu 2

Mamy **konkretne mapy/tabele** (Chalmers, Oregon, FST Lisboa, Staniszewski 2024). Wspólny obraz: **UT to duży udział DF i największa wrażliwość na yaw/attitude**; braking pitch potrafi bardziej rozwalić balans niż typowy FS corner; **nie zamrażać UT na samym δ=0**.

---

## 3) Opublikowane Cl/Cd/balans — pełne pakiety (tabela ze źródłami)

> **Uwaga metrologiczna:** Cx/Cz PUT (Fluent, Aref zespołu) ≠ CLA/CDA [m²] ≠ Cl/Cd ze stron teamów (często bez Aref / z DRS). **Nie mieszać w jednym wykresie bez wspólnego Aref.**

| Źródło / kontekst | Cl / Cz / CLA | Cd / Cx / CDA | Balans | Warunki | Link | Conf. |
|-------------------|---------------|---------------|--------|---------|------|-------|
| **PUT RWiter017** (kotwica) | Cz **−3,682** | Cx **1,229** | **≈61,6%** przód (`1/2+Cm/Cz`) | 15 m/s, half-car | [research-balance-shift.md](research-balance-shift.md) | **high** |
| **Nagłowski 2024** (PUT, inny model) | Cz **−4,071** | Cx **1,453** | **60,3%** przód | 15 m/s | [naglowski-2024-package.md](naglowski-2024-package.md) | **high** |
| **Staniszewski 2023** 3D pojazd | Cz **−2,036** | Cx **0,726** | nie podano | 15 m/s | [staniszewski-2023-wing.md](staniszewski-2023-wing.md) | **high** |
| **Jackson 2018** + RW DRS closed | CL_DF **1,15** | CD **1,21** | nie (DF głównie tył) | 26,8 m/s; A=1,18 m² | Jackson / Fields | **high** |
| **Jackson** DRS open | CL_DF **0,26** | CD **0,79** | — | A=0,99 m² | j.w. | **high** |
| **Chalmers CFS** small diffuser straight | CL **3,612** | CD **1,433** | **~50%** tył | 40 km/h | Chalmers PDF Tab. 4.1 | **high** |
| **Chalmers** 13° diffuser straight | CL **3,729** | CD **1,419** | 49,68% tył | 40 km/h | Tab. 4.3 | **high** |
| **Kirchberger EDGE14** | CLA **≈4,66…5,2 m²** | CDA **≈1,51…1,72 m²** | — | half-car StarCCM+; mesh study | reposiTUm DOI | **high** |
| **Rennstall Esslingen** Stallardo25 | CL\*A **4,9** | CD\*A **1,65** | nie znaleziono | cornering **50 km/h** (strona teamu) | https://www.rennstall-esslingen.com/stallardo25 | **high** |
| **PoliTO SC24** Andromeda (EV) | ClA ≈ **4,75** | CdA ≈ **1,45** | nie znaleziono | CFD + WT Dec 2023 (teza Cravero) | https://webthesis.biblio.polito.it/35911/1/tesi.pdf | **high** |
| **eForce CTU.25** (EV, **z DRS**) | Cl **−5,9** | Cd **2,02** | masa 52/48 (nie aero) | DF **320 kg @ 100 km/h**; DRS −**30%** drag | https://eforce.cvut.cz/ctu-25-en/ | **high** (strona); Aref **nie podany** |
| **Wordley & Saunders / Monash 2005** (FSAE WT) | — | CD **0,83** (baseline cytowany przez Jackson) | — | WT | SAE 2006-01-0806/0808 (abstract) | **med** (paywall pełny tekst) |
| **AMZ / Aachen / Delft / Tallinn / Joanneum 2024–25** | **nie znaleziono** publicznych Cl/Cd pakietu konkursowego | — | **nie znaleziono** % aero | — | [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md) | **high** (gap) |
| Maryland TR25 active aero (FSAE IC, **nie** EU EV) | CD **1,44 → 0,73** (−49%); CoP **78%→20%** front DF | — | active | AIAA 2026 abstract | https://doi.org/10.2514/6.2026-110799 | **med** (inna klasa; DRS-like) |

### MDPI CarMaker Part 2 (ART_X) — mapa Cd vs crosswind + DRS

Źródło: https://www.mdpi.com/2673-4591/79/1/77 (2024) — DRS off/on, kąty ±0…20°.

| Crosswind [°] | CD DRS off | CD DRS on |
|--------------:|----------:|----------:|
| 0 | **1,711** | **1,314** (~−25%) |
| ±5 | 1,528 | 1,173 |
| ±10 | 1,367 | 1,045 |
| ±20 | 1,190 | 0,913 |

(Przydatne jako **wzór mapy yaw**, nie jako target PUT — u nas DRS OUT.)

---

## Luki (honest gaps)

1. **Brak publikacji Δ(3-el → 4-el) na tym samym RW** z Cl/Cd/Fz i wspólnym Aref — H1 zostaje **hipotezą CAD/CFD**, nie „literaturą mówi +X%”.
2. Top EU (AMZ, Aachen, Delft, Tallinn, Joanneum) **nie publikują** Cl/Cd/balansu konkursowego — mamy tylko procesy + rzadkie CLA/CDA (Esslingen, Kirchberger, PoliTO, CTU).
3. Staniszewski 2024: **konkretne Cx(δ)/Cz(δ) tylko na wykresach** — w plain text brak tabeli punktowej (nie OCR-owano).
4. ASME cornering 2025: pełny PDF za paywallem — mamy snippet **>20%** CLA loss, nie pełną tabelę.
5. Quintanas: liczby **240 N / 58 N / 7 kg** z conclusion PDF (UPCommons); **V / Aref / czy izolowane RW vs full-car** nie wyciągnięte w tej sesji z pełnego tekstu → nie skalować na 017.
6. CTU.25 Cl/Cd **z DRS w pakiecie** — u nas DRS OUT; traktować jako górny rząd wielkości DF, nie setup do kopiowania.
7. Fan / powered GE: poza zakresem Spec (OUT) — Michalecki w KB.

---

## Co to znaczy dla PUT (H1 / H2 / balans / OUT)

**H1 — RW 4-el. kandydat.** Literatura **nie da Ci gotowego ΔCl**. Da motywację (UPC: więcej parametrów setupu + ekspozycja ostatniego flapu; Pretoria/McBeath: 4-el. osiągalne w boxie FSAE) i ostrzeżenia (Staniszewski: 2D≠3D coupling; masa ~7 kg u UPC; T8.3 sztywność). Gate: tabela na pakiecie 017 — Δbalans / ΔCx / ΔCz vs 3-el. baseline; Cx ≲ **1,23**, \|Cz\| ≥ **3,682**.

**H2 — UT.** To jest **najmocniej udokumentowana** dźwignia w tym researchu: Chalmers (13° + strakes + manewry), Oregon (yaw 5° / roll −6%), FST Lisboa (~16% DF od yaw), Staniszewski 2024 (δ-mapy + −2,7% proxy energii), Kirchberger (~40% DF). Szukaj **tylniejszego** docisku dyfuzora **bez** dokręcania nosa FW. Gate: mapa Cx/Cz vs δ (+ roll/RH jeśli budżet) przed zamrożeniem.

**Balans 61,6% → ~50%.** Żaden top team nie opublikował „róbcie 50% tak jak my”. Chalmers celuje ~**50/50** (nawet rear-biased narracyjnie). Nasze dźwignie: **H1 RW + H2 UT**, potem ewentualnie FW unload (H3), wąsy TBD (H4). Nie dokręcać samego FW.

**DRS OUT / fan OUT.** Jackson i MDPI/CTU pokazują, że open DRS zjada DF (u nas 019/020: \|Cz\| ~3,01 < 3,682). Fan — Michalecki. Nie projektować peak-DF przez te ścieżki.

**Kolejność pracy:** H1 → H2 → (H3) → H4; zawsze na **pełnym pakiecie** + przynajmniej **mapa vs δ**.

---

## Źródła użyte (checklist)

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

**Liczba źródeł z liczbami (Cl/Cd/Fz/CLA/%/N):** **≥ 16** (wiersze 1–16 powyżej + ASME snippet).  
**Źródła bez head-to-head 3vs4:** gap jawny.

