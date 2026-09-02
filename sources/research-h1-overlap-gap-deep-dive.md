# Pogłębienie H1 — overlap / gap / AOA (seria 2D)

**Status:** notatka badawcza, 2026-09-02 (Europe/Warsaw)  
**Dla kogo:** Spec + CFD#1, **po** otwarciu bramki medium+ (gdy szum Cl spadnie wyraźnie poniżej ~8%).  
**Zasada:** liczby tylko z cytowanych źródeł w KB. Nie wpuszczamy Cl/Cd 2D na kartę RWiter017 ani do `TARGETS.md`.

Budujemy na:  
[checklist-h1-2d-rw-gap-aoa.md](checklist-h1-2d-rw-gap-aoa.md) · [research-overnight-h3-fw-unload-rw-gaps.md](research-overnight-h3-fw-unload-rw-gaps.md) · [staniszewski-2023-wing.md](staniszewski-2023-wing.md) · [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md) · [sanity-cfd1-2d-rw-vs-lit.md](sanity-cfd1-2d-rw-vs-lit.md).

---

## 1. Po co ta notatka

Kąty main na medium dały czytelny sygnał głównie na **Cd** (A1/A1b/A1c w dół; A2/A2b kill). |ΔCl| było mniejsze niż szum siatki (~8% Cl medium→fine). Zanim wrócimy do decyzji CAD, potrzebujemy:

1. stabilniejszej siatki (medium+),  
2. potem sweepu **overlap → gap** z sensownymi krokami z literatury,  
3. jasnych killi (stall / wybuch Cd).

---

## 2. Zakresy startowe (opublikowane)

### McBeath (cyt. Jackson / Craig / checklista)

- gap: **1–4%** cięciwy poprzedniego elementu  
- overlap: **1–6%** cięciwy  
- praktyka Craig: gap ≈ **2%** c, overlap ≈ **1,5%** c  
- Flap1 AOA high-DF: ok. **25–30°**  
- Flap2 AOA: ok. **30–70°**

### Jackson 2018 (E423, 3 el.)

- gap = **20 mm**  
- overlap = **26,25 mm**  
- Flap1 / Flap2 = **28° / 60°**  
- overall AOA ≈ **22,81°** (stall ~**25°**)

### Staniszewski 2023 (2D izolowane RW, V = 15 m/s)

Kroki:

- main: **1,5°**  
- profile 2 i 3: **2,0°**  
- overlap: **10 mm**  
- gap: **5–20 mm**

Wybrane punkty sił 2D:

- overlap **−30 mm**:  
  - Fx = **27,11 N**  
  - Fz = **−565,03 N**  
- gap **+5 / +10 mm** (iter004.5):  
  - Fx = **26,98 N**  
  - Fz = **−559,80 N**  
- przy overlap **−40 mm** Fz już spada — jest optimum, nie monotonia.

### Baseline CFD#1 (kontekst, nie target)

- kąty **8° / 20° / 32°**, S1223  
- gap main→f1 ≈ **3,5%** c (w paśmie McBeath)  
- gap f1→f2 ≈ **5,1%** c (lekko powyżej 4%)  
- overlap f1→f2 ≈ **6,5%** c (lekko powyżej 6%)

---

## 3. Kolejność sweepu po otwarciu bramki

Trzymać checklistę H1, ale z twardym filtrem szumu:

1. **Ustabilizuj siatkę** — |ΔCl| medium→medium+ wyraźnie poniżej ~8% (cel roboczy Spec: szum ≪ krok serii).  
2. **Overlap** (±10 mm względem baseline CFD#1), jeden przepis siatki.  
3. **Gap** (+5 mm, potem +10 mm).  
4. Dopiero wtedy ewentualnie doprecyzowanie kątów wokół najlepszego overlap/gap.  
5. Opcjonalnie **jedno** porównanie 4-el. — nie default.

Nie wracać do drobnych kroków main (1°) na niestabilnej siatce: A1c pokazał plateau Cd przy main 1° vs 3,5°.

---

## 4. Jaki ΔCl jest „prawdziwy”

Z sanity-checku zespołu:

- skok Cl medium→fine ≈ **8%** — to był szum / problem numeryczny (fine Cd ≈ 0,10 odpuszczone).  
- A1/A1b/A1c: |ΔCl| ≈ **1–4%** — **poniżej** tego szumu → Spec nie zatwierdza CAD.  
- A2b: ΔCd ≈ **+52%** przy |ΔCl| małym — czytelny kill (stall path), zgodny z ostrzeżeniem Jacksona przed pchaniem AOA w stall.

**Reguła robocza pod decyzję kąta/overlap/gap:**

- decyzja CAD tylko gdy |ΔCl| (albo jasny trend na ≥2 punktach) jest **wyraźnie większy** niż aktualny szum meshu, **albo** gdy Cd daje jednoznaczny kill/zysk przy stabilnym Cl;  
- sam kierunek „jak Staniszewski” bez przebicia szumu = diagnostyka, nie CAD.

Literatura nie podaje „magicznego %” na Waszą siatkę — podaje kierunki i rzędy. Próg ~8% to **Wasz** pomiar GCI, nie liczba z paperów.

---

## 5. Kill criteria (seria 2D)

Zabij wariant (nie idzie do CAD), gdy:

- Cd rośnie ostro bez zysku |Cl| (wzorzec A2 / A2b),  
- overall AOA / klapy wchodzą w rejon stall (~25° u Jacksona — u Was inne profile, ale ten sam ostrzegacz),  
- overlap poniżej sensownego minimum (u Staniszewskiego **−40 mm** już gorsze Fz),  
- gap wychodzi daleko poza 1–4% c i |Cl| spada (utrata „flap effect” — Apostolidis / overnight H3),  
- |Cz| na aucie później < **3,682** vs RWiter017 (kill Spec na pakiet — osobna karta, nie 2D).

---

## 6. Checklista Spec po medium+

1. Zapisz |ΔCl| i |ΔCd| medium→medium+ oraz y+.  
2. Jeśli szum Cl nadal ~8%: **nie** otwieraj decyzji CAD; dogęszczaj slot/LE–TE, nie globalny fine izotropowy.  
3. Jeśli szum spadnie: uruchom O1/O2 (overlap ±10 mm), potem G1/G2 (gap +5/+10 mm) na **tej samej** siatce.  
4. Raportuj Δ vs baseline 2D, nie absolutów na RWiter017.  
5. Po stabilnym 3-el.: najwyżej jedno porównanie 4-el.

---

## 7. Czego nie znaleziono

- Head-to-head tabeli ΔCl/ΔCd 3 vs 4 el. na tym samym aucie.  
- Publicznej mapy overlap/gap dla geometrii RWiter017.  
- Uniwersalnego progu „ΔCl > X% = decyzja CAD” w paperach FS.  
- Pełnych tabel Peterson (OSU slot gaps) — tylko abstrakt / proprietary.

---

## 8. Werdykt krótki

Overlap/gap to właściwy **następny** dźwignia H1 po kątach, ale **dopiero** gdy medium+ zejdzie ze szumu Cl. Do tego czasu trzymamy się diagnostyki i killi Cd; literaturalny kierunek (Staniszewski / McBeath / Jackson) jest jasny, a absolutów 2D nadal nie mieszamy z kartą auta.
