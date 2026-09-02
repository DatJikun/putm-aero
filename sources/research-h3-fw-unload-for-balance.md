# H3 — odciążenie przedniego skrzydła po H1+H2 (cofanie balansu)

**Status:** notatka dla Spec + CFD (2026-09-02 Europe/Warsaw)  
**Język:** PL, pełne zdania  
**Zasada:** liczby tylko z cytowanych źródeł lokalnych i opublikowanych. Nie inventujemy Cl/Cd. Nie przepisujemy Cl/Cd cudzych aut na kartę `RW_iter017`.

**Kotwica pakietu (zamrożona):**  
Cx = **1,229**  
|Cz| = **3,682**  
Cm = **−0,429**  
balans ≈ **61,6%** przód → cel ~**50/50** (gap ≈ **12 pp**)  
Aref half ≈ **0,50 m²**  
V CFD = **15 m/s**  
metryka: moment @ **x = 0,765 m**, Lref **1,53 m**, half-car  
DRS ruchomy **OUT**, fan **OUT**  
kolejność: **H1 RW → H2 floor → H3 FW unload**  
eventy: **Endurance + Autocross**

**Źródła cytowane:**  
[research-overnight-h3-fw-unload-rw-gaps.md](research-overnight-h3-fw-unload-rw-gaps.md) · [research-balance-shift.md](research-balance-shift.md) · [naglowski-2024-package.md](naglowski-2024-package.md) · [sanity-cfd1-2d-rw-vs-lit.md](sanity-cfd1-2d-rw-vs-lit.md) · [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md) · [research-h2-undertray-balance-levers.md](research-h2-undertray-balance-levers.md)

Mirror: `/workspace/putm-aero/sources/research-h3-fw-unload-for-balance.md`

---

## 1. Co robi H3 i kiedy wchodzi

H3 to **zmniejszenie docisku z przodu**: kąt całego FW, mniej agresywna klapa / ostatni element, albo lokalne odciążenie. Cel jest jeden — zejść z front-bias ~61,6% w stronę 48–52% przód.

Spec uruchamia H3 **dopiero po** H1 (więcej tyłu z RW) i H2 (więcej tyłu z dyfuzora / UT). Gap do 50/50 to ok. **12 pp**. Samo FW rzadko domyka taki dystans bez utraty |Cz|. KTH pokazuje małe Δ przy −α wewnętrznych elementów; stąd kolejność H1→H2 najpierw.

H3 kosztuje |Cz|. Twardy kill: |Cz| **< 3,682** przy jakimkolwiek kroku odciążenia.

Sanity note CFD#1 dotyczy **2D RW** (H1), nie FW. Traktujemy ją tylko jako przypomnienie: nie mieszamy Cl/Cd izolowanego skrzydła z kartą całego auta 017 i nie wpisujemy cudzych Cl/Cd do TARGETS.

---

## 2. Mechanizm (kierunek, bez liczb własnych)

Mniej Fz na FW → mniejszy udział przodu → CoP / balans idzie **do tyłu**. To jest ruch odwrotny do „dokręcania FW dla peak DF”, które pcha CoP jeszcze bardziej na przód.

Literatura FS powtarza ten sam kierunek pracy:

1. **Najpierw max tył, potem dopasuj przód do balansu.** Racecar Engineering (Hatton / Pfeiffer, 2017): RW ogranicza total DF (brudny napływ za kierowcą / roll hoop). Zespół najpierw wyciska max z RW, potem projektuje FW tak, by **równać** DF tyłu. Łatwo zrobić „huge” FW i zniszczyć balans.  
   URL: <https://www.racecar-engineering.com/articles/tech-explained-formula-student-aerodynamics/3/>

2. **Flapy FW/RW jako dźwignia balansu.** Craig & Passmore (Loughborough, SAE 2014-01-0596): flapy na obu skrzydłach dopasowują aero balance do rozkładu masy; przy wybranym setupie udział DF na przedniej osi regulowany w zakresie **45–60%**.

3. **Baseline często lekko front-biased + regulacja kątem klapy.** Pamnani et al. (IJRASET 2020): cel to aero balance blisko CG; wybrano lekki front bias **56%** przód, regulowany kątami flapów. Przy spadku ride height DF rośnie i balans **idzie do przodu** (±~5% w ich mapie) — odciążenie FW / wyższy nos działa w przeciwną stronę.  
   DOI: <https://doi.org/10.22214/ijraset.2020.32700>

4. **CoP reaguje na kąt FW.** EngProc / MDPI 2025 (*Aerodynamic Design… Front Wing*):
   - bez skrzydła CoP ~**87,6%** od przedniej osi  
   - FW default → CoP ~**66%**  
   - pełny kąt FW **−2°** → CoP ~**60%**  
   - dalsze baffles → ~**58%**  
   - poniżej ~**58%** dalsze **−2°** psuje RW / venturi (autorzy się zatrzymują)  
   DOI: <https://doi.org/10.3390/engproc2025113062>  
   Te CoP idą **do przodu** przy dokręcaniu FW. Dla nas H3 to **odwrotny** ruch (odciążenie → CoP do tyłu). Liczby pokazują czułość dźwigni, nie przepisujemy ich na 017.

U Nagłowskiego 2024 FW ≈ **39%** Fz_all — duża dźwignia w obie strony. Na 017 udział FW = **TBD** (brak CSV sił komponentów w kotwicy).

---

## 3. Opublikowane siły FW w Newtonach (cudze auta — osobne linie)

**Nie** przenosić 1:1 na RWiter017. Zapis jak w Spec checklistach: jedna wielkość na linię.

### 3.1 Nagłowski 2024 (PUT) — cały pakiet @ **15 m/s**

To jest najbliższy nam rząd wielkości przy tym samym V CFD. Źródło lokalne: [naglowski-2024-package.md](naglowski-2024-package.md) (Tab. 5.3).

- Fz_all = **−561 N** (baseline iter000)  
- Fz_fw = **−221 N**  
- Fz_rw = **−135 N**  
- Fz_ut = **−202 N**  
- udział FW ≈ **39%** Fz_all  
- balans baseline = **60,3%** przód  
- Fx_all = **199,84 N**  
- Cx baseline = **1,453**  
- Cz baseline = **−4,071**  

Uwaga: to **inne** auto niż RWiter017 (Cx/Cz 017 = 1,229 / −3,682). Nie mieszać absolutów.

### 3.2 Hokkanen / KTH Formula Student DeV18 (2024) — full-car CFD

Różne kąty **wewnętrznych** elementów FW (ujemny kąt = odciążenie względem najagresywniejszego). PDF: <https://www.diva-portal.org/smash/get/diva2:1881327/FULLTEXT01.pdf>

- DeV17 (stary): DF total = **344 N**; DF FW = **32 N**; Drag = **134 N**  
- DeV17.5: DF total = **398 N**; DF FW = **88 N**; Drag = **126 N**  
- DeV18 @ **0°**: DF total = **410 N**; DF FW = **106 N**; Drag = **134 N**  
- DeV18 @ **−5°**: DF total = **408 N**; DF FW = **104 N**; Drag = **134 N**  
- DeV18 @ **−10°**: DF total = **416 N**; DF FW = **104 N**; Drag = **136 N**  
- DeV18 @ **−15°**: DF total = **400 N**; DF FW = **100 N**; Drag = **134 N**  

Wniosek autora: regulacja kąta wewnętrznych elementów daje **tylko lekkie** przesunięcie CoP. Dla H3 u nas: oczekuj **kilku pp** balansu na krok kąta, nie magicznych 12 pp z samego FW.

### 3.3 EngProc 2025

- FW = **195 N** @ **54 km/h** (izolowany system skrzydeł w cytowanym fragmencie)  
- Fl/Fd = **11,76**  
- pakiet z FW: +**38%** total DF vs bez skrzydeł  

Pełny PDF MDPI w sesji overnight był zablokowany przez CDN; liczby z abstraktu / snippety indeksu.

### 3.4 Chaiyanupong & Khajorntraidet (JRAME 2024) — izolowane 2D double-element FW (S1223)

To **nie** jest full car. Warunki ich domeny / V — **nie** kopiować na 017.

- gap = **2,5%** C  
- overlap = **5%** C  
- optimum: main **3°**, flap **30°**  
- Cl ≈ **4,84**  
- DF FW = **884,3 N**  
- Cd ≈ **0,347**  
- drag = **62,9 N**  

DOI: <https://doi.org/10.14456/jrame.2024.3>

### 3.5 FW = 588 N

W researchu overnight i w tej notatce: **nie znaleziono** takiego opublikowanego wyniku. Nie inventujemy.

---

## 4. Kiedy NIE odciążać FW jako pierwszej dźwigni

Nie uruchamiaj H3 w tych sytuacjach:

1. **H1 jeszcze nie domknięty.** Najpierw więcej tyłu z RW na pakiecie 017 (kąty / overlap / gap). Sanity CFD#1 i checklista H1 mówią: serie 2D dają kierunek Δ, ale decyzja balansu pada na aucie.

2. **H2 jeszcze nie zrobiony (albo nie zabity).** Najpierw mocniejszy / bardziej tylny dyfuzor–UT **bez** ruszania nosa FW. Gate: mini-mapa Cx/Cz vs δ przed zamrożeniem.

3. **H1+H2 już dają 48–52% przód.** Wtedy H3 = OUT. Nie ruszaj FW „na zapas”.

4. **Cel to dogonić peak DF dokręceniem FW.** To pcha balans jeszcze bardziej na przód i jest odwrotnością H3. Patrz [research-balance-shift.md](research-balance-shift.md) §5.

5. **|Cz| już siedzi na granicy 3,682.** Odciążenie FW prawie zawsze obniża |Cz|. Kill natychmiast przy zejściu poniżej kotwicy.

6. **Oczekujesz 12 pp z samego −Δα FW.** KTH: DF FW 106→100 N przy 0°…−15° — małe Δ CoP. Najpierw H1+H2 domykają większość gapu; H3 to drobna korekta.

7. **Mieszasz DRS / fan / wąsy w tym samym case.** DRS OUT, fan OUT. Wąsy = H4 / TBD, nie ta seria.

Praktyka FS (Racecar Engineering / Pfeiffer): max RW → potem FW pod balans. Nasza kolejność H1→H2→H3 to ten sam schemat.

---

## 5. Oczekiwany kierunek na 017 (gdy H3 włączone)

| Wielkość | Kierunek |
|----------|----------|
| Balans przód | **↓** |
| \|Cz\| | **↓ ryzyko** (łatwo stracić peak DF) |
| Cx | **↓ lub ≈** (mniej AOA FW) |
| Fz_fw | **↓** (to jest cel lokalny H3) |
| Fz_rw / Fz_ut | mogą lekko spaść przez coupling — mierzyć osobno |

Guardrale sukcesu serii (nie tylko H3): |Cz| ≥ **3,682**, Cx ≲ **1,23**, balans **48–52%** przód.

---

## 6. Checklist pomiarów CFD (H3)

Cel serii po H1+H2: domknąć resztę gapu do 48–52% **bez** zejścia |Cz| poniżej 3,682.

**Warunek startu H3:** po H1+H2 balans nadal **>~52%** przód **i** |Cz| ≥ 3,682.

**Warianty (1–2 case’y, nie wszystko naraz):**

1. −Δα całego FW względem bazy po H1+H2  
2. **albo** mniej agresywny ostatni element / klapa FW (bez zmiany całego kąta main, jeśli CAD tak pozwala)

**Na każdym runie zapisz osobno:**

- nazwa iteracji i baza (po H1 / po H1+H2)  
- co zmieniono (mm / °)  
- Cx  
- Cz / |Cz|  
- Cm  
- balans % @ x = **0,765 m**  
- **Fz_fw [N]**  
- Fz_rw [N]  
- Fz_ut [N]  
- Fz_all [N] (jeśli Fluent oddaje)  
- krótka nota Cp / stall na FW (jakościowo)  
- V = **15 m/s**, half-car, te same BC co kotwica  

**Kill natychmiast gdy:**

- |Cz| **< 3,682**  
- Δbalans nieosiągalne bez łamania guardrala DF → wróć do H1/H2 (więcej tyłu), nie pogłębiaj H3  
- H1+H2 już w 48–52% → nie uruchamiaj H3  

**Nie oczekuj** 12 pp z samego FW. Lekcja KTH: małe Δ przy −α wewnętrznych.

**Nie mieszać** DRS / fan. Wąsy = TBD, nie w tej serii.

T8 przy FW: wysokość / outboard (T 8.2.1); keep-out kół (T 2.1.3); IA / attachment za AIP przy długim nosie (T 3.20). Yaw: FW mniej wrażliwe niż UT (Staniszewski 2024) — odciążenie FW jest bezpieczniejsze yawowo niż agresywny UT, ale kosztuje |Cz|.

---

## 7. Gaps — czego nie znaleziono

| Brak | Status |
|------|--------|
| Opublikowane **FW = 588 N** (ani bliski wariant pod H3 unload) | **nie znaleziono** |
| Tabela Δbalans [pp] vs −Δα FW dla auta podobnego do 017 przy V = 15 m/s | **nie znaleziono** |
| Publikowane Cl/Cd **RWiter017** / PUT 2026 po H3 | nie istnieją publicznie — **nie inventować** |
| Udział Fz_fw / Fz_rw / Fz_ut na kotwicy 017 (CSV Fluent) | **brak w postpro** — tylko Cm/Cz → ~61,6% |
| Pełny PDF EngProc 2025 (MDPI CDN Access Denied w sesji overnight) | częściowo; PDF **nie pobrany** |
| Bezpośredni paper „unload FW by X° → −Y pp balance @ FS Endurance” z raw siłami | **nie znaleziono**; najbliższe: Pamnani (flap-tunable 56%), Craig (45–60% front), KTH (małe Δ przy −α), EngProc (CoP vs +α) |
| Mapа yaw δ dla odciążonego FW na 017 | **nie znaleziono** |

---

## 8. Claims (skrót)

| claim | evidence | confidence |
|-------|----------|------------|
| H3 = odciążenie FW **po** H1+H2; kierunek balans ↓ przód | Spec levers + Racecar Eng. + Pamnani + overnight H3 | **high** |
| Balans 017 ≈ **61,6%** przód; gap ~**12 pp** do 50/50 | Cm/Cz RWiter017 + research-balance-shift | **high** (roboczo); **med** vs pełny raport Fluent |
| FW u Nagłowskiego ≈ **−221 N** / ~**39%** Fz @ 15 m/s | Tab. 5.3 | **high** (ich auto); udział na 017 = **TBD** |
| KTH: FW DF **106 / 104 / 104 / 100 N** przy 0/−5/−10/−15°; małe Δ CoP | Tab. 1 Hokkanen | **high** (ich auto); transfer na 017 **low–med** |
| EngProc: FW **195 N** @ 54 km/h; CoP 87→58% przy dokręcaniu FW | DOI engproc2025113062 snippets | **med** (PDF nie pobrany) |
| JRAME 2024 izolowane 2D: DF FW **884,3 N**, Cl≈**4,84** | DOI jrame.2024.3 | **high** (ich 2D); **nie** target 017 |
| Najpierw max RW (+UT), potem FW pod balans | Racecar Engineering / Pfeiffer; Spec H1→H2→H3 | **high** (praktyka FS) |
| H3 kill: \|Cz\| < 3,682 **lub** H1+H2 już w 48–52% | Spec / levers H3 | **high** (decyzja Spec) |
| FW = **588 N** | — | **nie znaleziono** |

---

**Koniec notatki.** Nie robić git push z tej sesji.
