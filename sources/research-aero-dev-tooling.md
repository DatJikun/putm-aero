# Research: organizacja rozwoju pakietu aero (tooling / workflow) — EU FS EV

**Status:** notatka claims-based pod PUT Motorsport FS Aero (2026-09-01)  
**Język:** PL  
**Zakres:** **project management + engineering workflow** — jak silne teamy EU (oraz jawne case’y FSAE z tym samym stackiem) śledzą iteracje CFD, robią handoff CAD→CFD i stawiają bramki decyzyjne. **Bez** liczb Cl/Cd jako targetów (te są w innych notatkach KB).  
**Zasada:** tylko to, co widać w publicznych źródłach (blogi teamów / partnerów, tezy, GitHub, Notion/Confluence publiczne, FSG handbook jako kontekst deadline’ów). Brak źródła = **not found** — bez inventowania metryk ani „tak robi AMZ”.

**Kotwica kontekstu PUT (nie tooling zewnętrzny):** Excel `team/putm-aero-sim-log.xlsx` + CSV w `team/` + KB `putm-aero` + pipeline SolidWorks STEP → SpaceClaim → Fluent (`team/workflow.txt`, [team-fluent-workflow.md](team-fluent-workflow.md)). Baseline bolidu: `RW_iter017`.  
Powiązane: [claims-from-eu-fs-ev-top.md](claims-from-eu-fs-ev-top.md) (wzmianka: brak przeglądu Monday/Sheets), [research-fs-teams-practice.md](research-fs-teams-practice.md), [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md).

---

## 1. Summary for Spec / Aero Pack

Silne teamy EU FS **nie publikują** (w otwartych źródłach tej sesji) pełnych boardów Monday/Jira/Notion z logiem CFD. To, co jest widoczne publicznie, to głównie:

1. **Centralny log iteracji** (arkusz / server DB) — wiersz = run; kolumny = hipoteza, geometria bazowa, Cx/Cz/Cm, status. Monash wprost opisuje *run tracking spreadsheet*; Duke FSAE — *master spreadsheet* z zakładkami Full Car / FW / RW / Floor. PUT już to ma (`putm-aero-sim-log.xlsx`: ZADANIA, DASHBOARD, FW/UT/RW/Baseline + Szczegóły).
2. **Standaryzacja handoffu CAD→CFD** — named selections / zone names, Share Topology, half-car + BOI, skrypty meshing/solving/post. eForce Prague zbudował GUI na **PyFluent** + kolejkę; Tampere / Missouri S&T — template STAR-CCM+ + auto post; wielu używa Fluent/SpaceClaim jak PUT.
3. **Bramki decyzyjne wewnętrzne** (nie FSG): kolejność pakietu (np. Cologne RW→FW→UT), dowód lap-time / mapy przed „nową bazą”, freeze pod manufakturę / EDR. FSG narzuca **deadline’y dokumentów** (EDR/DSS itd.), nie datę freeze aero.
4. **Wersjonowanie wiedzy** przy rotacji członków — paper Vehicles/MDPI (case’y kilku teamów FS) wskazuje Git + formalizację wariantów jako odpowiedź na utratę wiedzy; to nie jest „wdrożyć PLM jutro”, tylko sygnał problemu.

**Wniosek dla PUT:** Excel + putm-aero jako **kanon na teraz** jest zgodne z tym, co top/mid teamy pokazują publicznie. Luka nie leży w „braku Jiry”, tylko w **powiązaniu** (ID iteracji ↔ folder OneDrive ↔ baseline CAD ↔ gate) i w **powtarzalności** setupu (skrypty już są — je utwardzić przed nowymi narzędziami).

---

## 2. Jak śledzą iteracje CFD (publiczne przykłady)

| claim | evidence | confidence |
|-------|----------|------------|
| Monash Motorsport: każdy run trafia do **run tracking spreadsheet**; dane na serwerze MMS; standardowy post-report do porównania z baseline | Blog Monash *CFD Workflow*: „run’s information is inputted into our run tracking spreadsheet… history of all statistical information and iterations” — https://www.monashmotorsport.com/blog/cfd-workflow | **high** (opis procesu); szczegóły kolumn **not found** w blogu |
| Monash: >**1300** runów w jednym sezonie designu po automatyzacji postpro | ten sam blog | **high** (ich deklaracja); nie używać jako target PUT |
| Duke FSAE: **master spreadsheet** z tabami per typ sim (Full Car, RW, FW, Floor); osobny szablon dokumentu na opis zmian + obrazki | https://www.dukefsae.com/single-post/aerodynamics-update-summer-2022-iterative-design-and-cfd | **high** (proces); liczby Cl w tym poście nie są przedmiotem tej notatki |
| Missouri S&T Racing: Design Manager (STAR-CCM+) zbiera metryki do tabeli; Python „output file supplement” pod **iteration logs**; średnia z ostatnich ~150 iteracji monitorów | Teza *Aerodynamic Design Workflow Optimization for FSAE…* — https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=9267&context=masters_theses | **high** (opis tooling); FSAE USA — transfer procesu **med** |
| Tampere FS: przejście SimScale/OpenFOAM → STAR-CCM+ template; setup \<**2 min**; auto-export dziesiątek widoków; −**\>90%** active user time / \>**100 h**/sezon | Theseus thesis abstract — http://theseus.fi/handle/10024/892896 | **high** (abstract); pełna tabela kolumn logu **not found** |
| eForce Prague: custom GUI **PyFluent**, default settings, **queue**/batch, swap tylko zmienionych części zamiast całego auta | Ansys blog 2026-04-23 — https://www.ansys.com/blog/how-eforce-prague-formula-engineers-success-with-simulation | **high** (partner case EU EV) |
| eForce: GPU skróciło runtime CFD z ~**7 h** do ~**2 h** (deklaracja teamu w blogu) | ten sam Ansys blog | **high** jako ich pomiar; nie generalizować |
| Publiczne boardy **Monday / Jira / Notion** z logiem aero top EU (AMZ, Delft, Aachen, Tallinn…): | **not found** w tej sesji (spójne z [claims-from-eu-fs-ev-top.md](claims-from-eu-fs-ev-top.md)) | **high** (jako gap) |
| Northeastern Electric Racing (NER): publiczny Confluence — standard nazw sim `[Straightline/Cornering/Braking]Sim_X`, named selections / BOI | https://nerdocs.atlassian.net/wiki/spaces/NER/pages/1178140684/CFD+Pre+Post+Process+Standards | **med** (FSAE USA, ale jawny standard procesu) |
| Industry-style zone naming (przykład Bramble, nie team FS): `zone-description-side` (np. `rr-wh-rim-lhs`, `fw-…`, `uf-…`) | https://bramblecfd.com/cfd-tutorials/naming-conventions/ | **med** (wzorzec nazewnictwa; nie „tak robi top EU”) |
| Digital engineering / Git dla wariantów (zawieszenie, nie aero per se) w kilku teamach FS — odpowiedź na rotację i utratę wiedzy | MDPI *Vehicles* 2026, DOI https://doi.org/10.3390/vehicles8020043 | **high** (problem + Git); **low** jako „wdrożyć PLM aero” |

**Wniosek roboczy:** kanoniczny „log iteracji” w FS to nadal **arkusz + folder wyników**, czasem z auto-wpisem po skrypcie. Pełny PLM/PDM aero **nie** jest widoczny w otwartych źródłach jako warunek bycia top.

---

## 3. Handoff CAD → CFD (SpaceClaim/Fluent vs OpenFOAM)

### 3.1 Wzorzec Fluent / SpaceClaim (bliski PUT)

| claim | evidence | confidence |
|-------|----------|------------|
| Typowy łańcuch: CAD (SolidWorks) → cleanup / enclosure / named selections (SpaceClaim) → Fluent Meshing → Fluent Solution → CFD-Post / ParaView | PUT `team/workflow.txt`; blog Asad Soomro (FSAE) https://www.asadsoomro.com/formula%20sae/3d%20cfd/aerodynamics/2024/04/20/CFD-Workflow.html; Oscar Gerber LinkedIn (SW→Fluent→ParaView + Python/HPC) | **high** |
| Named selections w SpaceClaim **napędzają** BC i sizing (inlet/outlet/symmetry/wall; BOI osobno, bez Share Topology na BOI) | Ansys watertight blog; VSC Fluent pointers; PUT workflow (`surface_fw`, `domain_inlet`, `boi_lvl-*`) | **high** |
| PUT: STEP z SolidWorks zawiera model + refy (BOI/curvature) + domain; SpaceClaim: half-car, Share Topology, grupy powierzchni; Fluent Meshing poly-hexcore; V=**15 m/s**, Lref=**1,53 m**, moment @ **x=0,765 m** | workflow.txt + [team-fluent-workflow.md](team-fluent-workflow.md) | **high** |
| PUT ma już skrypty: `meshing.wft`, `solving.jou`, `postpro-cfdpost.txt` | `team/fluent-scripts/` | **high** |
| eForce: automatyzacja PyFluent usuwa ręczne „upload + assign zones”; później partial geometry swap + cornering/attitude bez pełnego przebudowania modelu | Ansys eForce blog | **high** (kierunek mature Fluent team) |
| Oscar Gerber: named selections w SolidWorks (Ansys plugin) → PMDB → jeden skrypt Python na HPC (mesh+solve+post) | LinkedIn post (workflow opisany) https://www.linkedin.com/posts/oscar-gerber-86425a258_cfd-automation-for-fsaeformula-student-aerodynamics-activity-7410712318231142400-C__2 | **med** (post LinkedIn; brak peer-review) |

### 3.2 OpenFOAM / SimScale

| claim | evidence | confidence |
|-------|----------|------------|
| Cologne (eMotorsports): rozwój pakietu na **SimScale** (OpenFOAM w chmurze) po preselekcji 2D w STAR-CCM+; ~**40 000** core-hours / sezon (deklaracja bloga) | https://www.simscale.com/blog/formula-student-aerodynamics/ | **high** (proces); core-hours = ich liczba |
| Tampere: stary model SimScale/OF wymagał za dużo ręcznego setupu → migracja do STAR-CCM+ template | Theseus abstract | **high** |
| OpenFOAM: sztywna struktura case’a + snappyHexMesh / function objects `forceCoeffs` — dobry do reprodukowalności folderów, słabszy UX bez własnych skryptów | publiczne tutoriałe OF (np. NTNU HPC airfoil); nie „top EU standard” | **med** (ogólna praktyka OF) |

### 3.3 Naming i baseline (praktyka widoczna)

| claim | evidence | confidence |
|-------|----------|------------|
| Stałe nazwy stref / BOI / typów runów ułatwiają automatyzację i porównania | NER Confluence; Bramble zone names; PUT `boi_lvl-1…8`, `curvature_lvl-*`, `surface_fw` | **high** (kierunek) |
| Nazwa sim powinna kodować **typ analizy + wersję assembly** (np. `StraightlineSim_X`) | NER | **med** |
| PUT już nazywa iteracje `FWiter###` / `RWiter###` / `UTiter###` + kolumna **Model Bazowy** w Excelu | CSV `team/*-iters-*.csv`, arkusz sim-log | **high** |
| Baseline = jawna kotwica w logu (nie „ostatni plik na dysku”) | Monash: porównanie do baseline w standard report; PUT: `RW_iter017` w INDEX/TARGETS | **high** |

**Uwaga:** publiczne źródła **nie** podają jednego uniwersalnego schematu nazw top EU — rekomendacja to **utrwalić własny** schemat PUT (już bliski Monash/Duke), nie kopiować Bramble 1:1.

---

## 4. Decision gates (freeze, balans, „nowa baza”)

| claim | evidence | confidence |
|-------|----------|------------|
| Cologne: kolejność rozwoju **RW → FW → UT** (RW jako główny generator oporu/energii; FW balans+prowadzenie; UT „most efficient”) | SimScale blog Pfeiffer | **med** (jeden dobrze opisany case; Hogea/WashU startuje od UT — kolejność **nie** uniwersalna; zob. research-fs-teams-practice) |
| Cologne: nowa geometria staje się bazą dopiero gdy **lap-time sim** pokazuje poprawę (po korekcie masy itd.) | SimScale blog | **high** (metoda gate) |
| Mapy aero / attitude (RH, rake, yaw, steer) zamiast jednego punktu @δ=0 — praktyka dojrzałych teamów | Monash Hendy; Dynamis/SimScale w research-eu; Staniszewski 2024 u PUT | **high** (metoda) |
| FSG **nie** narzuca daty freeze aero; narzuca deadline’y SES/EDR/DSS/VSV itd. | FSG Competition Handbook 2024/2025 (tabele deadline’ów) — np. https://www.formulastudent.de/fileadmin/user_upload/all/2024/important_docs/FSG24_Competition_Handbook_v1.1.pdf | **high** |
| Wewnętrzny „design freeze” przed manufakturą / testami to decyzja teamu (porady zewnętrzne np. Amatum — nie oficjalne FSG) | https://amatum.com/formula-student-germany-2025-deadlines/ | **low–med** (blog doradczy) |
| PUT Spec (zamrożone w INDEX): cel balansu ~**50/50** (roboczo 48–52% przód); DRS ruchomy OUT; fan OUT; priorytet Endurance+AX; kandydat RW 4-el. | INDEX.md / TARGETS.md | **high** (intent zespołu) |
| Gate yaw / mapa UT przed zamrożeniem podłogi — rekomendacja procesowa z research-fs-teams-practice (nie liczba z top EU) | research-fs-teams-practice §4 | **high** (proces KB) |

**Bramki proponowane pod PUT (jako proces, nie metryki Cl):**

1. **Gate A — Baseline lock:** `RW_iter017` (lub następca) oznaczony w Excelu + wiersz w KB; każdy run ma `Model Bazowy`.  
2. **Gate B — Balance target:** decyzja „idziemy dalej” tylko jeśli hipoteza ma plan wpływu na balans (~61,6% → ~50/50) *albo* jest jawnie oznaczona jako eksploracja poza targetem.  
3. **Gate C — UT freeze:** przed kompozytem/formami — minimum: nominal + wybrane punkty yaw/RH (mapa), nie tylko δ=0.  
4. **Gate D — Package freeze:** data wewnętrzna pod laminację / EDR; po niej tylko delta z uzasadnieniem w Excelu (kolumna Wniosek).

---

## 5. Co PUT już ma vs luki

### 5.1 Mamy (canon kandydat)

| Element | Gdzie | Uwagi |
|---------|-------|-------|
| Log iteracji CFD | `team/putm-aero-sim-log.xlsx` (ZADANIA, DASHBOARD, FW/UT/RW/Baseline + Szczegóły, Chłodzenie) | Kolumny m.in. Nazwa, Osoba, Opis, Hipoteza, Wniosek, Data, Model Bazowy, Gotowe?, Cm/Cx/Cz, efektywność, CoP |
| Eksporty CSV pod KB | `team/fw-iters-*.csv`, `rw-iters-*.csv`, `ut-iters-with-balance-*.csv` | Służą claims / INDEX |
| Pipeline Fluent udokumentowany | `team/workflow.txt`, [team-fluent-workflow.md](team-fluent-workflow.md) | STEP → SpaceClaim half-car → Meshing → Solution → CFD-Post |
| Skrypty powtarzalności | `team/fluent-scripts/` (`.wft`, `.jou`, postpro) | Fundament pod lekką automatyzację |
| Baza wiedzy + baseline | `putm-aero` INDEX/TARGETS/sources | Kotwica `RW_iter017`; decyzje Spec spisane |
| Artefakty runów | OneDrive (postpro JPG); lokalnie np. `team/rwiter017/` (cx/cz/cm rfile, cfdpost zip) | INDEX: postpro OneDrive często **bez CSV sił** → kotwica z arkusza |

### 5.2 Luki (bez inventowania „tak mają top”)

| Gap | Status | Ryzyko |
|-----|--------|--------|
| Publiczny opis Monday/Jira/Notion u top EU EV | **not found** | Nie kopiować narzędzia „bo top” |
| Trwały link **Excel ID ↔ folder OneDrive/case ↔ plik STEP/scdoc** | częściowy (nazwy iteracji) | Orphan postpro; trudny audit |
| CSV sił z Fluent w tym samym miejscu co JPG postpro | często brak (INDEX) | Drift Excel ↔ Fluent |
| Formalne **decision gates** datowane w KB (UT freeze, package freeze) | decyzje Spec są; kalendarz gate’ów **nie** spisany jako tooling note | Slip manufaktury |
| Jednolity README nazewnictwa named selections / BOI | jest w workflow.txt; brak krótkiej karty „do onboarding” | Błędy BC u nowych osób |
| Auto-wpis do Excela po solve | **not found** u PUT | Ręczny wpis = opóźnienia / pominięcia |
| PLM/PDM (SolidWorks PDM, 3DX…) jako system aero | **not found** w publicznych źródłach top EU jako wymóg | Wysokie tarcie vs zysk przy małym teamie |
| Pełna automatyzacja PyFluent-class | eForce ma; PUT ma journals — stopień niżej | OK na teraz |

---

## 6. Rekomendacje dla PUT (low friction first)

**Zasada:** Excel + putm-aero = **kanon**. Nowe narzędzie tylko jeśli zmniejsza tarcie wpisu / handoffu / onboarding — nie „bo Jira”.

### Pięć actionable recommendations

1. **Zostaw Excel `putm-aero-sim-log.xlsx` + KB `putm-aero` jako single source of truth.** Każdy run CFD **musi** mieć wiersz zanim uznamy go za „Done” (status Gotowe?). CSV w `team/` odświeżać przy zamrażaniu claims. Nie migruj do Notion/Jira w sezonie bez właściciela procesu.  
   *Źródło wzorca:* Monash + Duke (arkusz jako historia).

2. **Dodaj w Excelu 2–3 kolumny ścieżek (niski koszt):** `path_cad` (STEP/scdoc), `path_case` (OneDrive/folder Fluent), `path_post` (JPG/CSV). Wymagaj tego przy statusie Done. To zamyka lukę „JPG bez CSV” bez nowego SaaS.  
   *Źródło wzorca:* Monash (server + spreadsheet); Missouri S&T (iteration log = skondensowane monitory).

3. **Utrwal kartę nazewnictwa (1 strona w `sources/` lub `team/README-cfd-naming.md`):** named selections z workflow (`surface_*`, `domain_*`, `boi_lvl-*`, `curvature_lvl-*`), konwencja `FWiter/RWiter/UTiter`, reguła „Model Bazowy = ID wiersza baseline”. Nowy członek odpala meshing dopiero po checklist.  
   *Źródło wzorca:* NER Confluence standards; Ansys named-entity practice; własny workflow.txt.

4. **Spisz decision gates w INDEX/TARGETS z datami wewnętrznymi:** Gate Balance (hipotezy pod ~50/50), Gate UT freeze (mapa nominal+yaw/RH), Gate Package freeze (pod laminację/EDR). Po freeze — tylko delty z wypełnionym „Wniosek”. FSG deadline’y (EDR/DSS) traktuj jako hard external, nie jako zamiennik gate aero.  
   *Źródło wzorca:* Cologne (lap-time przed nową bazą); FSG handbook (external deadlines).

5. **Automatyzuj najpierw to, co już macie — journals/WFT → jeden „Run card”**, zanim PyFluent/GUI.** Minimalny krok: po `solving.jou` eksport Cx/Cz/Cm (średnia z ostatnich N iteracji) do CSV o nazwie = ID wiersza Excela; ręczny paste 3 liczb albo prosty skrypt Python. Pełne GUI eForce-class / kolejka GPU = **opcjonalny next** gdy Excel+ścieżki+gates działają 4+ tygodnie bez wyjątków.  
   *Źródło wzorca:* eForce PyFluent (dojrzały etap); Oscar Gerber / Tampere (template + skrypt); PUT już ma `.jou`/`.wft`.

**Opcjonalne next tools (kolejność tarcia rosnąco — nie startować od góry listy):**

| Priorytet | Narzędzie | Kiedy warto | Kiedy nie |
|-----------|-----------|-------------|-----------|
| 0 (teraz) | Excel + putm-aero + OneDrive paths | zawsze | — |
| 1 | Utrwalone journals + CSV force dump | po rekomendacji 5 | jeśli nikt nie utrzymuje skryptów |
| 2 | Lekki board zadań (Notion/GitHub Projects) **tylko** na zadania „kto robi którą hipotezę” — **nie** na metryki CFD | gdy ZADANIA w Excelu się dusi | gdy zastąpi log Cx/Cz |
| 3 | PyFluent GUI / queue | gdy >1 osoba dziennie odpala te same setupy | w środku sezonu bez ownera |
| 4 | SolidWorks PDM / pełny PLM | gdy CAD chaos między subteamami | jako „rozwiązanie logu CFD” |

---

## 7. Limity (czego nie wnioskować)

1. Brak publicznego Jira u AMZ ≠ „AMZ nie planuje” — tylko **not found**.  
2. \>1300 runów Monash / 7h→2h eForce to **ich** infrastruktura, nie KPI PUT.  
3. Paper Vehicles/Git dotyczy głównie wariantów zawieszenia — nie wklejać jako „mamy wdrożyć graph-based PLM aero”.  
4. Kolejność RW→FW→UT (Cologne) vs UT-first (Hogea) pokazuje, że gate’y są **lokalne** — PUT trzyma się Spec (balans, Endurance+AX, DRS/fan OUT).  
5. Ta notatka **nie** zmienia Cx/Cz/balansu baseline.

---

## Źródła (URL / DOI)

1. Monash Motorsport — *CFD Workflow* — https://www.monashmotorsport.com/blog/cfd-workflow  
2. Duke FSAE — *Aerodynamics Update Summer 2022* — https://www.dukefsae.com/single-post/aerodynamics-update-summer-2022-iterative-design-and-cfd  
3. Ansys — *How eForce Prague Formula Engineers Success With Simulation* (2026-04-23) — https://www.ansys.com/blog/how-eforce-prague-formula-engineers-success-with-simulation  
4. Pfeiffer / SimScale — *Formula Student Aerodynamics* (eMotorsports Cologne) — https://www.simscale.com/blog/formula-student-aerodynamics/  
5. Tampere FS thesis abstract (STAR-CCM+ automation) — http://theseus.fi/handle/10024/892896  
6. Missouri S&T — *Aerodynamic Design Workflow Optimization for FSAE…* — https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=9267&context=masters_theses  
7. MDPI Vehicles — *Managing Design Variants in Formula Student…* — https://doi.org/10.3390/vehicles8020043  
8. NER Confluence — *CFD Pre/Post Process Standards* — https://nerdocs.atlassian.net/wiki/spaces/NER/pages/1178140684/CFD+Pre+Post+Process+Standards  
9. Asad Soomro — *CFD Workflow* (SpaceClaim/Fluent FSAE) — https://www.asadsoomro.com/formula%20sae/3d%20cfd/aerodynamics/2024/04/20/CFD-Workflow.html  
10. Bramble — *Naming Conventions in CFD* — https://bramblecfd.com/cfd-tutorials/naming-conventions/  
11. Ansys — watertight geometry / named entities — https://ansys.synopsys.com/blog/watertight-cfd-geometry-ansys-fluent  
12. Oscar Gerber — CFD automation LinkedIn — https://www.linkedin.com/posts/oscar-gerber-86425a258_cfd-automation-for-fsaeformula-student-aerodynamics-activity-7410712318231142400-C__2  
13. FSG Competition Handbook 2024 v1.1 (deadlines) — https://www.formulastudent.de/fileadmin/user_upload/all/2024/important_docs/FSG24_Competition_Handbook_v1.1.pdf  
14. PUT wewnętrzne: `team/workflow.txt`, `team/putm-aero-sim-log.xlsx`, `team/fluent-scripts/`, [team-fluent-workflow.md](team-fluent-workflow.md), INDEX.md  

---

## Changelog

- 2026-09-01 — pierwsza wersja (Aero Pack / tooling research); uzupełnia lukę z claims-from-eu-fs-ev-top („brak przeglądu Monday/Sheets”).
