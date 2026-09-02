# Endurance / Efficiency — trade-offy aero (docisk, opór, energia, balans) dla PUT EV

**Status:** notatka badawcza do Spec, 2026-09-02 Europe/Warsaw  
**Język:** PL, ton koleżeński  
**Zasada:** liczby tylko z cytowanych źródeł; nie wymyślamy Cl/Cd ani Wh dla PUT. Braki = **nie znaleziono**.

**Kotwica zespołu (nie „literatura”):** `RW_iter017` @ 15 m/s — Cx **1,229**, Cz **−3,682**, Cm **−0,429**, balans ≈ **61,6%** przód; cel ~**50/50**; DRS ruchomy OUT; fan OUT; priorytet Endurance + Autocross (`TARGETS.md`).

Budujemy na:  
[staniszewski-2024-energy.md](staniszewski-2024-energy.md) · [research-aero-for-targets.md](research-aero-for-targets.md) · [claims-from-eu-fs-ev-top.md](claims-from-eu-fs-ev-top.md) · [research-fs-teams-practice.md](research-fs-teams-practice.md) · [ASSUMPTIONS-DRAFT.md](../ASSUMPTIONS-DRAFT.md) · [TARGETS.md](../TARGETS.md).

---

## 0. Punkty eventów — tylko tło scoringu (nie targety aero)

Z Kirchberger 2023 (Tab. 1.1, rules 2023 / FSG):

- Endurance = **250** pkt  
- Autocross = **100** pkt  
- Efficiency = **75** pkt  
- Accel = **50** pkt  
- Skidpad = **50** pkt  

Źródło: https://repositum.tuwien.at/bitstream/20.500.12708/188917/1/Kirchberger%20Michael%20-%202023%20-%20CFD%20Simulation%20and%20Validation%20of%20a%20Formula%20Student...pdf  

To mówi nam, że Endurance + Efficiency waży dużo w EV overall. Nie zamienia to Cx/Cz z `RW_iter017` na inne liczby. Claims z top EU: sam mocny AX bez ukończonego Endurance nie wygrywa sezonu (przykład Aachen FSA25: AX 100 pkt, Endurance 0 → overall słabo) — [claims-from-eu-fs-ev-top.md](claims-from-eu-fs-ev-top.md).

---

## 1. Co mówią prace o proxy energii, mapach kąta skrętu i masie podłogi

### 1.1 Staniszewski 2024 (PP, praca magisterska) — nasze lokalne źródło energii

Cel: charakterystyka aero w zakręcie (nie tylko na wprost), porównanie pełnego pakietu z FW+RW bez podłogi, model toru i proxy konsumpcji przez średnią ważoną siłę hamującą.

Metoda proxy (nie bateria):

- F(v) = Fx(v) + Crr · (mg + Fz(v))  
- energia wnioskowana ze stosunku średnich sił hamujących  
- **brak pomiaru Wh/kWh na torze**  

Liczby z tekstu pracy (każda na osobnej linii):

- Δm podłogi (szacunek) ≈ **10 kg**  
- F1 (bez UT, średnia ważona siła hamująca) = **290,319**  
- F2 (z UT, pełny pakiet) = **282,589**  
- F2/F1 = **0,973**  
- Δ proxy „energii” = **−2,7%** (mniejsza średnia siła hamująca z podłogą)  
- Cx pełnego pakietu niższy niż FW&RW dla δ **0°–10°**  
- Cx pełnego pakietu wyższy niż FW&RW dla δ **10°–20°**  
- \|Cz\| pełnego pakietu wyższe **dla każdego** δ vs FW&RW  
- max Cx i Cz pełnego pakietu przy δ = **0°**  
- przykładowe punkty Tab. 9: r **17,55 m** → v **13,77 m/s**; r **8,77** → **9,41**; r **5,85** → **7,59**; r **4,39** → **6,54**  

Wnioski, które przenosimy do Spec bez wymyślania Wh:

1. Charakterystyki w zakręcie nie da się wiarygodnie wyciągnąć z jednego case’u „na wprost” — potrzebna mapa Cx/Cz vs δśrd.  
2. UT&SW mocno reaguje na kierunek napływu; przy δ≠0 spada wkład podłogi, a FW/RW są względnie „płaskie”.  
3. Sam wykres Cx(δ) nie wybiera zwycięzcy (krzywe się przecinają ~10°) — trzeba złożyć udziały prostych i łuków.  
4. Na *tamtym* modelu toru pełny pakiet wygrywa proxy energii mimo +~10 kg.  
5. **−2,7% ≠ zmierzona energia baterii**; nie przenosimy tej liczby na inny tor bez przeliczenia udziałów r.

Lokalna notatka: [staniszewski-2024-energy.md](staniszewski-2024-energy.md). PDF: załącznik zespołu (ekstrakcja `pdftotext`).

### 1.2 Inne cytowane źródła (kierunki, nie liczby PUT)

**Kirchberger 2023 (TU Wien EDGE 14)** — wrażliwość laptime (ich tor / model):

- +**10%** DF → ok. **−1%** lap  
- wrażliwość masy ≈ **2×** wrażliwości DF  

CLA/CDA ich auta (nie Cx/Cz PUT; A≈**1,19 m²**, inlet **15 m/s**):

- CLA ≈ **4,66–5,2 m²**  
- CDA ≈ **1,51–1,72 m²**  
- UT generuje ok. **40%** DF (ich deklaracja)  

Źródło: https://repositum.tuwien.at/bitstream/20.500.12708/188917/1/Kirchberger%20Michael%20-%202023%20-%20CFD%20Simulation%20and%20Validation%20of%20a%20Formula%20Student...pdf  

**eMotorsports Cologne / SimScale** (blog zespołu — kierunek procesu, nie peer-review):

- rozwój startował od RW jako czynnika mocno wpływającego na zużycie energii  
- UT opisane jako „most efficient” (dużo DF, mało drag)  
- setup Accel RW: drag **64,7%** niższy niż high-DF (Autocross/Skidpad) — u nas DRS/ruchome klapy OUT, więc to tylko ostrzeżenie o skali trade-offu  
- rake UT **1°** → ok. **+15%** DF z undertraya (ich case)  

Źródło: https://www.simscale.com/blog/formula-student-aerodynamics/  

**Jackson 2018** (DRS na RW — literatura zewnętrzna; u nas ruchomy DRS OUT):

- DRS closed: CL_DF **1,15**, CD **1,21**  
- DRS open: CL **0,26**, CD **0,79**  
- Δ siły oporu open vs closed ≈ **−35%**  

Lokalna notatka: [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md).  

**Nagłowski 2024** (udziały Fz @ 15 m/s na *ich* pakiecie — kierunek, nie target 017):

- Fz_FW ≈ **−221 N** (~**39%**)  
- Fz_UT ≈ **−202 N** (~**36%**)  
- Fz_RW ≈ **−135 N** (~**24%**)  
- Fz_all ≈ **−561 N**  

Lokalna notatka: [naglowski-2024-package.md](naglowski-2024-package.md).  

**Claims top EU EV** (bez absolutnych Cl/Cd od większości teamów):

- po banach powered ground effect wygrywa pasywny high-DF (skrzydła + UT)  
- UT to silna dźwignia efektywności / dużego udziału DF  
- jedyna świeża publiczna para „siłowa” z tej rundy: Esslingen **CL·A = 4,9** / **CD·A = 1,65** @ 50 km/h cornering (to ×A, nie Cx/Cz PUT)  
- munichMotorsport / TUM: Efficiency FSG25 1. — pakiet realnie efektywny, ale Cl/Cd **nie znalezione**  

Szczegóły: [claims-from-eu-fs-ev-top.md](claims-from-eu-fs-ev-top.md), [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md).

---

## 2. Co z tego wynika dla Efficiency (high DF vs Cd) — bez liczb baterii PUT

Efficiency w scoringu EV nagradza niskie zużycie energii przy ukończonym Endurance. Nie mamy w KB:

- pojemności baterii PUT  
- Wh/okrążenie z telemetrii  
- Crr ani masy bolidu zamrożonych pod ten proxy  

Dlatego nie liczymy tu „ile Wh zaoszczędzimy”. Czytamy literaturę tak:

1. **Więcej docisku nie jest automatycznie wrogiem Efficiency**, jeśli skraca czas w zakręcie albo obniża średnią siłę hamującą na modelu toru. Staniszewski: pełny pakiet z UT ma wyższe \|Cz\| *i* niższe F_ham (−2,7% proxy) mimo +~10 kg.  
2. **Sam wysoki Cd na prostych boli**, zwłaszcza bez DRS. Cologne pokazuje, ile drag potrafi spaść przy low-AOA RW (−64,7% vs high-DF); Jackson pokazuje −35% drag przy open DRS kosztem DF. U nas obie ścieżki aktywne są OUT — zostaje pasywny kompromis Cx przy trzymanym \|Cz\| ≥ 3,682.  
3. **Cx(δ) przecinające się krzywe** oznaczają, że „lepszy Cx @0°” nie gwarantuje lepszego Efficiency na torze z dużą liczbą ciasnych łuków. Bez modelu toru wybór high-DF vs low-Cd jest zgadywaniem.  
4. **Masa aero ma drugą stronę:** Kirchberger — wrażliwość masy ~2× wrażliwości DF na ich laptime. Staniszewski mimo to pokazuje, że +~10 kg UT może się opłacić *jeśli* proxy F_ham spada. Decyzja Spec: każda dołożona masa UT musi przejść przez własny model toru, nie przez „bo literatura mówi −2,7%”.  
5. **Top EU** łączy ukończony Endurance z Efficiency (Tallinn Endurance, TUM Efficiency FSG25, Joanneum). Claims: publiczne Cl/Cd od większości mistrzów **nie znalezione** — nie kopiujemy cudzego L/D.

Praktycznie pod Efficiency przy DRS OUT:

- nie tnij \|Cz\| poniżej kotwicy 3,682 „żeby Cx wyglądało ładniej”, dopóki nie masz proxy F_ham albo telemetrii  
- nie dokładaj Cx powyżej ~1,23 bez zwrotu w modelu toru / lap  
- UT traktuj jako kandydat na zysk efektywności (kierunek Cologne + Staniszewski), ale z bramką yaw  

---

## 3. Kolejność rekomendacji dla Spec — kiedy brać więcej Cx za Cz, a kiedy nie

Guardrail z `TARGETS.md` / `research-aero-for-targets.md`:

- \|Cz\| ≥ **3,682**  
- Cx ≲ **1,23** (orientacyjnie, przy tym docisku)  
- balans **48–52%** przód  
- kolejka: **H1 RW → H2 UT → H3 FW unload tylko jeśli trzeba → H4 wąsy TBD**

### Kiedy **akceptować** wyższy Cx za zysk Cz (albo za balans tyłu)

1. **H1 — tylne skrzydło:** ΔCx jest mały, a zyskujesz \|Cz\| *i* cofasz CoP w stronę 50/50. To domyka Autocross i nie zabija Endurance, o ile Cx zostaje w okolicy 1,23.  
2. **H2 — podłoga:** model toru (jak Staniszewski) pokazuje niższe F_ham albo wyraźny zysk \|Cz\| w zakresie δ typowym dla AX/Endurance, mimo lekkiego wzrostu Cx przy niektórych δ. Masa UT pozostaje pod kontrolą (u nich ~10 kg — u nas policzyć własną).  
3. **Gdy Cx rośnie, ale \|Cz\|/Cx nie spada dramatycznie** i balans idzie we właściwą stronę — lepiej niż dokręcanie samego FW.  
4. **Robustność dyfuzora** (kierunek Chalmers: wybór 13° zamiast 19° mimo podobnego peak) — czasem lekko gorszy peak L/D, ale stabilniejszy cornering; to też „akceptowalny” trade pod Endurance.

### Kiedy **nie** brać więcej Cx za Cz

1. **Cx idzie w górę, a \|Cz\| spada poniżej 3,682** — odpada (guardrail Spec; patrz też DRS open / RW_iter019–020 w research-aero-for-targets: Cx↓ ale \|Cz\| poniżej kotwicy).  
2. **Zysk Cz jest tylko @ δ=0**, a mapa δ pokazuje spadek podłogi w zakręcie bez poprawy F_ham na modelu toru — nie zamrażaj.  
3. **Balans pcha się jeszcze bardziej na przód** (dokładanie FW / wąsów złe miejsce) — to psuje AX i nie pomaga Efficiency.  
4. **Masa aero rośnie, a proxy F_ham nie spada** na *waszym* modelu toru — Kirchberger przypomina, że masa boli mocniej niż DF pomaga, procentowo.  
5. **„Low drag jak Accel Cologne / DRS Jackson”** kosztem peak DF — przy priorytecie Endurance+AX i DRS OUT to nie jest ścieżka Spec peak.  
6. **Porównanie cudzych CLA/CDA (Esslingen, Kirchberger) 1:1 z Cx/Cz 017** bez wspólnego Aref — nie decyzja, tylko rząd wielkości.

### Krótka checklista przed „tak, bierzemy ten Cx”

1. Raport: Cx, Cz, Cm, balans % @ x=0,765 m.  
2. Przynajmniej kilka punktów δ (mapa), nie jeden case na wprost.  
3. Prosty model toru → F_ham (albo inny uzgodniony proxy) vs baseline.  
4. Masa delty vs kierunek Kirchberger (masa boli ~2× DF).  
5. Czy nadal \|Cz\| ≥ 3,682 i balans bliżej 50/50?

---

## 4. Luki — nie znaleziono / TBD

| Gap | Status |
|-----|--------|
| Wh/okrążenie / kWh Endurance dla PUT z telemetrii baterii | **nie znaleziono** (Staniszewski = tylko proxy F_ham) |
| Crr i masa bolidu zamrożone pod ten sam arkusz energii co 017 | **TBD zespołu** (`INDEX.md` / ASSUMPTIONS: otwarte) |
| Przeliczenie −2,7% na tor docelowy zawodów 2026 (udziały r) | **nie zrobione** — wymaga własnego modelu |
| Publiczne Cl/Cd / balans % od AMZ, Aachen, Delft, Tallinn, Joanneum 2024–25 | **nie znaleziono** ([claims-from-eu-fs-ev-top.md](claims-from-eu-fs-ev-top.md)) |
| Absolutne Cl/Cd munichMotorsport mimo Efficiency FSG25 1. | **nie znaleziono** |
| Liczby 4-elementowego RW vs energia Endurance | **nie znaleziono** (4-el. = hipoteza CAD) |
| Wspólny Aref Fluent PUT vs Esslingen CLA/CDA / Kirchberger | **TBD** — nie mieszać jednostek |
| Walidacja torowa proxy F_ham ↔ Wh | **nie znaleziono** w KB |
| Budżet energii / pojemność baterii PUT jako hard constraint aero | **otwarte** (INDEX) |

---

## 5. Claims skrót (claim | evidence | confidence)

| claim | evidence | conf. |
|-------|----------|-------|
| Pełny pakiet z UT ma wyższe \|Cz\| vs FW&RW dla każdego δ; Cx(δ) przecina się ~10° | Staniszewski 2024 | **high** |
| Proxy energii: F2/F1 = 0,973 → −2,7% mimo +~10 kg UT | Staniszewski 2024 s. 67–68 | **high** jako F_ham; **med** jako Wh |
| Bez mapy δ + modelu toru nie wybierzesz zwycięzcy po samym Cx@0° | Staniszewski 2024 | **high** (metoda) |
| Scoring: Endurance 250 / AX 100 / Efficiency 75 (FSG rules via Kirchberger) | Kirchberger Tab. 1.1 | **high** (scoring); nie jest targetem Cx/Cz |
| UT bywa najefektywniejszym generatorem DF (kierunek); ~40% DF u EDGE 14 | SimScale Cologne; Kirchberger | **high** kierunek; **med** % |
| Low-drag setup potrafi ściąć drag o dziesiątki % kosztem DF (DRS/klapy) — u nas OUT | Jackson −35%; Cologne Accel −64,7% | **high** kierunek; transfer na 017 **med** |
| Wrażliwość masy ~2× wrażliwości DF na lap (jeden zespół) | Kirchberger Fig. 1.1 | **med** |
| Akceptuj ΔCx za ΔCz gdy trzymasz \|Cz\|≥3,682, cofasz balans i F_ham nie rośnie | TARGETS + Staniszewski + research-aero-for-targets | **med–high** (proces Spec) |

---

## Źródła (URL / DOI / lokalne)

1. Staniszewski A. — *Analiza wpływu elementów aerodynamicznych pojazdu elektrycznego klasy Formuła Student na zużycie energii…*, PP 2024 — [staniszewski-2024-energy.md](staniszewski-2024-energy.md) (PDF załącznik zespołu).  
2. Kirchberger M. — *CFD Simulation and Validation of a Formula Student Car*, TU Wien 2023 — https://repositum.tuwien.at/bitstream/20.500.12708/188917/1/Kirchberger%20Michael%20-%202023%20-%20CFD%20Simulation%20and%20Validation%20of%20a%20Formula%20Student...pdf  
3. Pfeiffer N. / eMotorsports Cologne — *Formula Student Aerodynamics With CFD*, SimScale — https://www.simscale.com/blog/formula-student-aerodynamics/  
4. Jackson — CFD DRS RW — [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md)  
5. Nagłowski 2024 — [naglowski-2024-package.md](naglowski-2024-package.md)  
6. Claims top EU — [claims-from-eu-fs-ev-top.md](claims-from-eu-fs-ev-top.md) · [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md)  
7. Spec / targety — [TARGETS.md](../TARGETS.md) · [research-aero-for-targets.md](research-aero-for-targets.md) · [ASSUMPTIONS-DRAFT.md](../ASSUMPTIONS-DRAFT.md)  
8. Esslingen Stallardo25 (CLA/CDA orientacja) — https://www.rennstall-esslingen.com (via research-eu)  
9. Chalmers undertray (robustność kąta ekspansji) — https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download  

*Bez inventowanych Cl/Cd/Wh. Scoring 250/100/75 tylko jako tło punktów.*
