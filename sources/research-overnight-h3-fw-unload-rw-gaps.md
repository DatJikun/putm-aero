# Overnight research: H3 odciążenie FW + reguły gap/overlap RW

**Status:** notatka z researchu nocnego (2026-09-01 → rano 2026-09-02 Europe/Warsaw)  
**Język:** PL, zdania czytelne  
**Zasada:** tylko publiczne paper/teza + ekstrakty już w KB. **Bez wymyślonych Cl/Cd dla RWiter017.** Liczby N / % poniżej pochodzą z **innych** aut / izolowanych skrzydeł i służą jako kontekst, nie jako targety PUT.

**Kotwica Spec (zamrożona):** `RW_iter017`

- Cx = **1,229**
- |Cz| = **3,682**
- Cm = **−0,429**
- balans ≈ **61,6%** przód → cel ~**50/50** (gap ≈ **12 pp**)
- Aref half ≈ **0,50 m²**; V CFD = **15 m/s**
- **DRS ruchomy OUT**; **fan OUT**
- kolejność: **H1 RW → H2 floor → H3 FW unload** (H3 tylko gdy H1+H2 nie domykają balansu)
- eventy **Endurance + Autocross**
- RW default **3-el.**; opcjonalne porównanie **4-el.**

Powiązane lokalnie: [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md), [research-balance-shift.md](research-balance-shift.md), [research-overnight-rw-multi-element.md](research-overnight-rw-multi-element.md), [staniszewski-2023-wing.md](staniszewski-2023-wing.md), [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md), [naglowski-2024-package.md](naglowski-2024-package.md).

---

## 1. H3 — odciążenie przedniego skrzydła (cofanie balansu)

### 1.1 Mechanizm (bez liczb własnych)

H3 to **zmniejszenie docisku z przodu** (kąt / klapa / lokalne elementy FW), żeby zejść z front-bias ~61,6% w stronę ~50%. Spec uruchamia H3 **dopiero po** H1 i H2. Nie dokręcamy FW „dla peak DF” jako pierwszej dźwigni cofania balansu — to pcha CoP jeszcze bardziej na przód.

Literatura FS / motorsport powtarza ten sam kierunek:

1. **Najpierw max tył, potem dopasuj przód do balansu.** Racecar Engineering (Hatton / Pfeiffer, 2017): RW ogranicza total DF (brudny napływ za kierowcą / roll hoop, wysoki montaż). Zespół najpierw wyciska max z RW, potem projektuje FW tak, by **równać** DF tyłu. Łatwo zrobić „huge” FW i zniszczyć balans.  
   URL: <https://www.racecar-engineering.com/articles/tech-explained-formula-student-aerodynamics/3/>

2. **Flapy FW/RW jako dźwignia balansu, nie tylko peak DF.** Craig & Passmore (Loughborough, SAE 2014-01-0596): flapy na obu skrzydłach służą do dopasowania aero balance do rozkładu masy; przy wybranym setupie udział DF na przedniej osi regulowany w zakresie **45–60%**.  
   DOI/PDF kontekst: SAE 2014-01-0596 (SemanticsScholar mirror użyty w sesji).

3. **Baseline często lekko front-biased + regulacja kątem klapy.** Pamnani et al. (IJRASET 2020): cel projektowy to aero balance blisko CG; wybrano lekki front bias **56%** przód, regulowany **kątami flapów** pod feedback kierowcy. Heave: przy spadku ride height DF rośnie i balans **idzie do przodu** (±~5% w ich mapie) — czyli odciążenie FW / wyższy nos działa w przeciwną stronę.  
   DOI: <https://doi.org/10.22214/ijraset.2020.32700> · PDF: <https://www.ijraset.com/fileserve.php?FID=32700>

4. **CoP reaguje na kąt całego FW i baffles.** EngProc / MDPI (2025) — *Aerodynamic Design and Simulation… Front Wing* (abstrakt + fragmenty HTML w indeksie wyszukiwania; pełny PDF w tej sesji zablokowany przez CDN):
   - bez skrzydła CoP ~**87,6%** od przedniej osi;
   - FW w default → CoP ~**66%**;
   - pełny kąt FW **−2°** → CoP ~**60%**;
   - dalsze baffles → ~**58%**;
   - poniżej ~**58%** dalsze **−2°** psuje RW / venturi (autorzy zatrzymują się);
   - izolowane FW @ **54 km/h**: DF = **195 N**, Fl/Fd = **11,76**;
   - pakiet z FW: +**38%** total DF vs bez skrzydeł.  
   DOI: <https://doi.org/10.3390/engproc2025113062> · HTML: <https://www.mdpi.com/2673-4591/113/1/62>  
   **Uwaga:** te CoP idą **do przodu** przy dokręcaniu FW — dla nas H3 to **odwrotny** ruch (odciążenie → CoP do tyłu). Liczby pokazują **czułość** dźwigni, nie przepisujemy ich na 017.

### 1.2 Opublikowane siły FW w Newtonach (inne auta — kontekst)

Zapisujemy w osobnych liniach, jak w Spec checklistach. **Nie** przenosić 1:1 na RWiter017.

**Nagłowski 2024 (PUT, już w KB)** — cały pakiet @ **15 m/s**:

- Fz_all = **−561 N** (baseline iter000)
- Fz_fw = **−221 N**
- Fz_rw = **−135 N**
- Fz_ut = **−202 N**
- udział FW ≈ **39%** Fz_all
- balans baseline = **60,3%** przód

Źródło lokalne: [naglowski-2024-package.md](naglowski-2024-package.md) (Tab. 5.3). To jest najbliższy nam rząd wielkości przy tym samym V CFD.

**Hokkanen / KTH Formula Student DeV18 (2024)** — full-car CFD, różne kąty **wewnętrznych** elementów FW (ujemny kąt = odciążenie względem najagresywniejszego):

| Konfiguracja FW | DF total [N] | DF FW [N] | Drag total [N] |
|-----------------|-------------:|----------:|---------------:|
| DeV17 (stary) | 344 | **32** | 134 |
| DeV17.5 | 398 | **88** | 126 |
| DeV18 @ **0°** | 410 | **106** | 134 |
| DeV18 @ **−5°** | 408 | **104** | 134 |
| DeV18 @ **−10°** | 416 | **104** | 136 |
| DeV18 @ **−15°** | 400 | **100** | 134 |

PDF: <https://www.diva-portal.org/smash/get/diva2:1881327/FULLTEXT01.pdf> · URN: <http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-349722>

Wniosek z tabeli KTH (ich słowa): regulacja kąta wewnętrznych elementów daje **tylko lekkie** przesunięcie CoP; autor wprost pisze, że adjustability trzeba dalej rozwijać, bo różnice są małe. Dla H3 u nas: oczekuj **kilku pp** balansu na krok kąta, nie magicznych 12 pp z samego FW — stąd kolejność H1→H2 najpierw.

**Chaiyanupong & Khajorntraidet (JRAME 2024)** — **izolowane 2D** double-element FW (S1223), nie full car:

- gap = **2,5%** C; overlap = **5%** C
- optimum: main **3°**, flap **30°**
- Cl ≈ **4,84**; DF FW = **884,3 N**; Cd ≈ **0,347**; drag = **62,9 N**  
  (warunki ich domeny / V — **nie** kopiować na 017)

DOI: <https://doi.org/10.14456/jrame.2024.3> · PDF: <https://ph01.tci-thaijo.org/index.php/jrame/article/download/251410/171556/944189>

**EngProc 2025** (patrz wyżej):

- FW = **195 N** @ 54 km/h (izolowany system skrzydeł w cytowanym fragmencie)

**FW = 588 N:** w tej sesji **nie znaleziono** takiego opublikowanego wyniku (ani w KB, ani w przeszukanych paperach). Nie inventujemy.

### 1.3 Co to znaczy dla Spec (H3)

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Odciążenie FW cofa balans (mniej % przodu) | fizyka + Pamnani 56% flap-tunable; EngProc CoP vs kąt (kierunek odwrotny przy unload) | **high** (kierunek) |
| FW jest dużą dźwignią siły u PUT (~39% Fz) | Nagłowski Tab. 5.3: FW = −221 N | **high** (ich auto); udział na 017 = **TBD** |
| Samo −Δα wewnętrznych elementów bywa słabą dźwignią CoP | KTH Tab. 1: DF FW 106→100 N przy 0°…−15° | **med** (inny samochód) |
| H3 kosztuje \|Cz\| — twardy kill poniżej 3,682 | Spec guardrail + levers H3 | **high** (decyzja Spec) |
| Najpierw max RW, potem FW pod balans | Racecar Engineering / Pfeiffer | **high** (praktyka FS) |

Kill H3 (z levers): \|Cz\| < 3,682 **lub** H1+H2 już w 48–52% → nie ruszaj FW.

---

## 2. Multi-element RW — gap / overlap / AOA / slot (tylko opublikowane liczby)

### 2.1 McBeath (cytowany w FS) — zakresy startowe

Publiczne cytowania (Jackson, Hokkanen/KTH, Craig) powtarzają McBeath *Competition Car Aerodynamics / Downforce*:

| Parametr | Zakres (cyt.) | Źródło cytujące |
|----------|---------------|-----------------|
| Slot gap | **1–4%** cięciwy poprzedniego elementu | Jackson 2018; Craig 2014 |
| Overlap | **1–6%** cięciwy | Jackson 2018 |
| Overlap + gap (wariant KTH lit.) | overlap **1–4%**, gap **1–2%** + **convergent slot** ważniejszy niż dokładny % | Hokkanen 2024 §2.2.4 (cyt. McBeath) |
| Flap 1 AOA | **25–30°** | Jackson (McBeath) |
| Flap 2 AOA | **30–70°** | Jackson (McBeath) |
| McBeath „rekomendowany” gap (Craig) | **2%** | Craig & Passmore 2014 |

Jackson DOI: <https://doi.org/10.5920/fields.2018.02> · lokalny ekstrakt: [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md)

### 2.2 Jackson 2018 — konkretna geometria 3-el. E423

- chord max **860 mm**, span **920 mm**
- main **540 mm**; Flap1 & Flap2 po **180 mm**
- overlap = **26,25 mm**; gap = **20 mm**
- Study 4 (wybrane): Flap1 **28°**, Flap2 **60°**, overall AOA ≈ **22,81°** (stall ~**25°**)
- Na ich pojeździe (DRS closed): CL_DF = **1,15**, CD = **1,21** — **nie** kopiować na 017

### 2.3 Staniszewski 2023 (PUT) — kroki i optimum 2D izolowanego RW

Lokalny ekstrakt: [staniszewski-2023-wing.md](staniszewski-2023-wing.md)

- 3 profile; baseline main **7,5°**
- kroki: main **1,5°**; profile 2&3 **2,0°**; overlap **10 mm**; gap **5–20 mm**
- 2D baseline: Fx = **49,96 N**, Fz = **−397,61 N**
- po −6,5° main: Fx = **27,83 N**, Fz = **−502,43 N**
- overlap **−30 mm**: Fx = **27,11 N**, Fz = **−565,03 N** (max \|Fz\| w tabeli)
- gap **+5 / +10 mm** (iter004.5): Fx = **26,98 N**, Fz = **−559,80 N**
- na **całym pojeździe** Cx/Cz prawie stoją (~**0,72 / −2,03**) — coupling body↔RW; **nie** wklejać 2D 1:1 na 017

### 2.4 Craig & Passmore 2014 — wrażliwość gap/overlap (2D CFD + WT)

- peak lift przy overlap **1,2–2%** chord i gap ≈ **1,6%**
- overlap **2,6%** → obniżony lift
- finalny wybór konstrukcyjny: gap **2%** + overlap **1,5%** (żeby ugięcie nie zamykało szczeliny; span full-scale **1,2 m**)
- flap AOA testowane **10 / 12 / 14°** (dual-element NACA 9418; inny reżim niż high-DF 3-el. Jackson)

SAE 2014-01-0596.

### 2.5 Apostolidis et al. (Aristotle Racing / BETA CAE) — gap FW, reguła jakościowa też dla RW

- zmniejszanie gap ↑ DF aż BL się **zlejają** → ryzyko stall na przednim elemencie;
- za duży gap → utrata „flap effect”;
- dla **FW**: przy gap **> 25 mm** efekt klapy zanika; zbyt mały gap = confluent BL ogranicza DF.  
  PDF: <https://www.beta-cae.com/events/c7pdf/4C_1_APOSTOLIDIS.pdf>

### 2.6 Inne opublikowane punkty (AOA / elementy)

- **MECDC 2014** (skrzydło 3-el. FS, abstrakt/search): slot gap **3,6%** chord poprzedniego; overlap **0,75%**; main **4°**; flaps **25° / 30°**; Cl = **2,81**, Cd = **0,81** (ich skrzydło). DOI: <https://doi.org/10.2478/mecdc-2014-0005> (pełny PDF w sesji: 406).
- **AI-assisted CFD / IJFT 2025** (abstrakt): FW AOA z **4,5° / 28,0° / 56,0°** → **5,5° / 33,0° / 59,5°**; RW z **9,5° / 40,0°** → **12,2° / 41,9°**; deklarowane +**14,8%** DF FW i +**28,4%** DF RW — **inny samochód**, nie target PUT. DOI: <https://doi.org/10.1016/j.ijft.2025.101440>
- **LUT 202x** (Metropolia HPF026): parametric flap angles + slot gaps wokół fixed mainplane — abstrakt bez tabeli liczb gap w publicznym handle; pełne liczby **not found** w tej sesji. Handle: <https://lutpub.lut.fi/handle/10024/171732>
- **Peterson (Oregon State 2014)** — *CFD and Wind Tunnel Determination of Rear Wing Slot Gaps*: publicznie dostępny tylko abstrakt (proprietary) → konkretne mm/gap **not found**. URL: <https://ir.library.oregonstate.edu/concern/honors_college_theses/sn00b080r>

### 2.7 Mini-tabela „co wolno wkleić do CAD start”

| Start CAD (orientacja) | Liczba | Skąd |
|------------------------|--------|------|
| Gap | **1–4%c** (cel praktyczny ~**2%c**) | McBeath / Jackson / Craig |
| Overlap | **1–6%c** (praktyka Craig **1,5%c**; peak CFD Craig ~**1,2–2%c**) | McBeath / Craig |
| Flap1 / Flap2 AOA high-DF 3-el. | **~28° / ~60°** (overall ~**23°**, stall ~**25°**) | Jackson Study 4 |
| PUT 2D overlap sweet spot | ok. **−30 mm** vs ich baseline | Staniszewski 2023 |
| PUT 2D gap fine-tune | **+5…+10 mm** | Staniszewski 2023 |
| Convergent slot | ważniejsze niż ślepy % | Hokkanen / McBeath |
| Ugięcie / T8.3 | nie schodzić w „paper-thin” gap | Craig + regulamin sztywności |

---

## 3. Checklist CFD na jutro rano (Spec)

Cel serii: |Cz| ≥ **3,682**, Cx ≲ **1,23**, balans z ~**61,6%** → **48–52%** przód. Metryka: moment @ **x = 0,765 m**, Lref **1,53 m**, half-car, **15 m/s**.

**Kolejność sweepów (nie mieszać wszystkiego naraz):**

1. **H1 — RW na pakiecie 017 (najpierw)**  
   - Start od geometrii 3-el. blisko McBeath/Jackson (gap ~2%c, overlap ~1–2%c, AOA flapów w stronę Study 4 **bez** wchodzenia w stall ~25° overall).  
   - Sweep **1:** kąty (main ↓ jak Staniszewski; flaps trzymaj blisko baseline po pierwszym kroku).  
   - Sweep **2:** overlap w stronę −30 mm (orientacja PUT 2D), potem drobny gap +5/+10 mm.  
   - Każdy case: Cx, Cz, Cm, **balans %**, Fz_rw / Fz_fw / Fz_ut jeśli Fluent je oddaje.  
   - Gate: Δbalans ≥ ~2 pp **i** guardrale DF/drag; inaczej kill / zmień kierunek.

2. **Opcja 4-el. (1 case porównawczy)**  
   - Tylko jeśli 3-el. H1 siedzi w T8. Bez obietnicy Δ z literatury (w KB brak liczb 4-el. z Cl/Cd dla naszego auta).

3. **H2 — floor / dyfuzor**  
   - 1 case mocniejszego tyłu UT bez ruszania nosa FW.  
   - δ = 0° najpierw; **zanim zamrozisz:** mini-mapa δ (0 / ~5–10 / ~15°) — patrz overnight UT/yaw.

4. **H3 — FW unload (tylko jeśli po H1+H2 balans nadal >~52% przód)**  
   - 1–2 warianty: −Δα całego FW **albo** mniej agresywny ostatni element / klapa FW.  
   - Mierz osobno: **Fz_fw [N]**, Fz_rw, Fz_ut, balans %, |Cz|, Cx.  
   - Kill natychmiast gdy |Cz| < 3,682.  
   - Nie oczekuj 12 pp z samego FW (lekcja KTH: małe Δ przy −α wewnętrznych).

5. **Log obowiązkowy per run**  
   - nazwa iteracji, co zmieniono (mm / °), Cx, Cz, Cm, balans %, Fz komponentów, krótka nota Cp/stall (jakościowo).  
   - Nie mieszać DRS/fan (OUT). Wąsy = TBD, nie w tej serii.

---

## 4. Gaps — czego **nie** znaleziono

| Brak | Status |
|------|--------|
| Opublikowane **FW = 588 N** (ani bliski wariant pod H3 unload) | **not found** |
| Pełny PDF EngProc 2025 (MDPI CDN Access Denied w tej sesji) — liczby CoP/195 N z abstraktu/snippetów indeksu | częściowo; PDF **not fetched** |
| Tabela Δbalans [pp] vs −Δα FW dla auta podobnego do 017 przy V=15 m/s | **not found** |
| Publikowane Cl/Cd **RWiter017** / PUT 2026 po H3 | nie istnieją publicznie — **nie inventować** |
| Pełne mm slot gap z tezy Peterson (Oregon State) | proprietary / abstrakt only |
| Pełna tabela gap/overlap z LUT Metropolia HPF026 | **not found** w publicznym abstrakcie |
| MECDC 2014 full PDF (406 w fetch) | liczby ze snippeta wyszukiwania; PDF **not fetched** |
| IJFT 2025 full text (timeout) | tylko abstrakt DOI |
| Bezpośredni paper „unload FW by X° → −Y pp balance @ FS Endurance” z raw siłami | **not found**; najbliższe: Pamnani (flap-tunable 56%), Craig (45–60% front), KTH (małe Δ przy −α), EngProc (CoP vs +α) |
| Walidacja tunelowa gap RW dla geometrii Staniszewskiego | brak w pracy 2023 |

---

## 5. Claims (skrót)

| claim | evidence | confidence |
|-------|----------|------------|
| H3 = odciążenie FW po H1/H2; kierunek balans ↓ przód | Spec levers + Racecar Eng. + Pamnani | **high** |
| FW u Nagłowskiego ≈ −221 N / ~39% Fz @ 15 m/s | Tab. 5.3 | **high** (ich auto) |
| KTH: FW DF 106 / 104 / 104 / 100 N przy 0/−5/−10/−15° | Tab. 1 Hokkanen | **high** (ich auto); transfer na 017 **low–med** |
| EngProc: FW 195 N @ 54 km/h; CoP 87→58% przy dokręcaniu FW | DOI engproc2025113062 snippets | **med** (PDF nie pobrany) |
| McBeath gap 1–4%c / overlap 1–6%c; Jackson 20 mm / 26,25 mm; flaps 28°/60° | Jackson 2018 | **high** |
| Staniszewski: overlap −30 mm → Fz 2D −565 N; gap +5/+10 OK | Tab. 3/4 | **high** (2D izolowane) |
| Craig: gap 2% + overlap 1,5%; peak CFD ~1,6% gap / 1,2–2% overlap | SAE 2014-01-0596 | **high** |
| Apostolidis: FW gap >25 mm gubi flap effect | BETA PDF | **med–high** (jakość wykresu; brak surowych N w tekście) |
| FW=588 N | — | **not found** |

---

**Koniec notatki.** Nie robić git push z tej sesji. Mirror: `/workspace/fs-aero-kb/sources/research-overnight-h3-fw-unload-rw-gaps.md`.
