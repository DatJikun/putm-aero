# Rozwój i analiza tylnego skrzydła wieloprofilowego klasy Formula Student / Alex Staniszewski / 2023 / praca inżynierska

**Uczelnia:** Politechnika Poznańska, Wydział Inżynierii Lądowej i Transportu  
**Promotor:** dr inż. Łukasz Brodzik  
**Data:** Poznań, 01.02.2023  
**Źródło PDF:** załącznik (38 stron); ekstrakcja `pdftotext -layout`

## Cel pracy

Identyfikacja koncepcji rozwoju tylnego skrzydła wieloprofilowego bolidu FS oraz ocena wpływu zmian na charakterystykę przepływu. Cel badawczy: **poprawa rozkładu ciśnienia** na powierzchni ssącej (wyrównanie wzdłuż rozpiętości) oraz **zwiększenie generowanych sił aerodynamicznych**, z uwzględnieniem wykonawstwa (re-use form) i regulaminu zawodów.

## Metody (CAD/CFD/eksperyment)

- **Brak eksperymentu** (tunel / tor) — wyłącznie CFD.
- CAD / przygotowanie domeny: **Ansys SpaceClaim** (3D); 2D bez SpaceClaim.
- Siatka: **Fluent Meshing** (BOI + curvature refinement, warstwa przyścienna).
- Solver: **Ansys Fluent** — model turbulencji **Realizable k-ε**, near-wall: **Enhanced Wall Treatment**.
- Warunki: velocity inlet **15 m/s** (tekst, s. 17 PDF / oznacja „17”); y+ docelowo **30–300** (preferowane niższe); inicjalizacja hybrydowa + External-Aero Favorable Settings.
- Badania: (1) wstępna 3D skrzydło + uproszczony pojazd; (2) seria **2D** izolowanego skrzydła (kąty, overlap, gap); (3) weryfikacja **3D** na pojeździe; (4) koncepcja hybrydowa sekcji środkowej/zewnętrznej.
- Metryki: Cp na powierzchni; w 2D — Fz (docisk) i doskonałość d = Cz/Cx; w 3D — Cx, Cz, d oraz wizualny rozkład Cp.

## Kluczowe liczby (Cl, Cd, downforce, drag, balans, energia, prędkości) — TYLKO z tekstu

> Uwaga: w pracy używane są Cx, Cz (nie Cl/Cd). Wartości 2D dotyczą skrzydła **w odosobnieniu** (nie całego auta). Wartości 3D — cały pojazd w badanej konfiguracji pakietu.

| Kontekst | Wielkość | Wartość | Cytat / lokalizacja |
|---|---|---|---|
| CFD inlet | V∞ | **15 m/s** | „przyjmujemy wartość 15m/s” (s. 17) |
| y+ | zakres | **30–300** | „przedziale od 30 do 300” (s. 19) |
| Baseline 2D | Fx, Fz | **Fx=49,96 N**, **Fz=−397,61 N** | Tab. 3/4, iter000 „RW baseline: MP 7.5°” (s. 25–27) |
| 2D po −6,5° main | Fx, Fz | **Fx=27,83 N**, **Fz=−502,43 N** | iter001.5 (s. 25–27) |
| 2D overlap −30 mm | Fx, Fz | **Fx=27,11 N**, **Fz=−565,03 N** | iter003.5 — najwyższy \|Fz\| w tabeli 2D |
| 2D final gap +5/+10 mm | Fx, Fz | **Fx=26,98 N**, **Fz=−559,80 N** | iter004.5 (s. 25–27) |
| Cp środkowa sekcja | ΔCp | lokalnie **~−0,7**; spadek podciśnienia o **~0,2** względem boków | „wzrost ciśnienia do wartości około -0,7… współczynnika większego o 0,2” (s. 20) |
| 3D cały pojazd | Cx, Cz, d | iter000: **Cx=0,726**, **Cz=−2,036**, **d=−2,804** | tabela s. 32 |
| 3D iter001 (nowy rozkład) | Cx, Cz, d | **0,725 / −2,033 / −2,804** | s. 32 |
| 3D iter002 (skrócony 1. profil) | Cx, Cz, d | **0,721 / −2,034 / −2,821** | s. 32 — lekka poprawa d |
| Przekrój analizy disturbance | offset | **400 mm** od płaszczyzny symetrii | s. 22–25 |
| Baseline kąt main | α | **MP 7,5°** | Tab. 3/4 |

**Liczby tylko na rysunkach (brak w tekście):** pola prędkości/ciśnienia (Rys. 22–30), dokładne wartości d z wykresów trendu 2D, szczegółowe mapy Cp — **nie odczytywano z obrazów**.

## Konfiguracje i geometria (profile, kąty, liczba elementów, DRS itd.)

- Skrzydło **wieloelementowe / wieloprofilowe**: **3 profile** (główny + Plane 1 & 2 / dwa ostatnie elementy) — stała geometria wzdłuż rozpiętości w baseline (prosty płat).
- Parametry zmieniane w 2D (Rys. 21, Tab. 2):
  - kąt natarcia **profilu 1 (main)** krok **1,5°** (serie do −7,0° względem baseline),
  - kąty **profili 2&3** krok **2,0°**,
  - **overlap distance** krok **10 mm** (do −40 mm),
  - **gap distance** kroki **5–20 mm**.
- Baseline main: **7,5°**.
- 3D: (a) nowy rozkład szczelin na całej rozpiętości; (b) skrócenie 1. elementu tak, by LE pokrywała się z pierwotną lokalizacją (kompensacja wydłużenia cięciwy całego złożenia — TE ostatniego elementu traktowane jako nieprzesuwalny limit regulaminowy); (c) koncepcja **hybrydowa**: nowe odstępy w sekcji środkowej + pierwotny rozkład na zewnątrz (iter003, tylko wizualnie).
- **Lokalne skręcenie geometryczne** środkowej sekcji planowane jako odpowiedź na lokalną zmianę efektywnego kąta natarcia (zaburzenia od mocowań / nadwozia).
- **DRS / aktywna aerodynamika:** nie omawiane.
- Nazwy profili lotniczych (np. NACA/Selig) dla RW: **nie podane w tekście**.

## Wnioski projektowe istotne dla NOWEGO pakietu aero

1. **Nierównomierny Cp wzdłuż rozpiętości** RW wynika z lokalnej zmiany efektywnego kąta natarcia w środku (zaburzenia od mocowań / elementów przed skrzydłem) — nie tylko z tip vortices klasycznego skrzydła.
2. W 2D **obniżanie kąta main** (względem baseline 7,5°) jednocześnie **podnosi \|Fz\| i obniża Fx** aż do ~−6,5°; dalsze −7,0° już pogarsza Fz.
3. Zmiana kątów **tylnych elementów** (±2°) **nie jest korzystna** względem baseline po optymalizacji main.
4. **Zmniejszanie overlap** (do ok. −30 mm) mocno zwiększa docisk 2D; −40 mm już pogarsza Fz — istnieje optimum szczeliny/overlap.
5. Drobne **gap +5/+10 mm** utrzymuje wysoki docisk przy niskim oporze (iter004.5).
6. Przeniesienie geometrii 2D na 3D bez kompensacji pozycji względem body **psuje** spodziewany zysk (skrzydło wchodzi w region silnych zaburzeń przez wydłużenie cięciwy).
7. **Skrócenie 1. profilu** + utrzymanie LE w pierwotnym miejscu przywraca wyrównanie Cp w środku; koszt: lekka strata max podciśnienia na LE boków i słabszy „dumping” na TE 2. profilu w swobodnym przepływie.
8. **Hybryda środka/zewnątrz** (iter003) wizualnie łączy zalety — „koncepcja mająca potencjał” do dalszych badań.
9. Wyniki 3D Cx/Cz prawie niezmienne (różnice rzędu **0,00x**) — autor ostrzega, że mogą leżeć w **niepewności CFD**; pakiet „poświęca” wydajność RW na uszczelnienie przepływu pod elementem boczno-przypodłogowym.

## Ograniczenia / czego NIE wnioskować

- Nie wnioskować absolutnych N docisku całego auta z tabel **2D** (izolowane skrzydło; inna skala / brak interakcji z body).
- Nie traktować ΔCx/Cz 3D (~0,005) jako potwierdzonego „zysku torowego” — autor sam wskazuje możliwą niepewność numeryczną.
- Brak walidacji eksperymentalnej; jeden model turbulencji; V = 15 m/s (nie mapa prędkości toru).
- Brak DRS, balansu osi w tej pracy, energii EV, nazw profili.
- Map Cp/prędkości — interpretacja jakościowa z rysunków; nie ekstrahowano wartości pikseli.

## Claims (bullet list: claim | evidence | confidence high/med/low)

- Baseline 2D RW: Fx≈50 N, Fz≈−398 N przy MP 7,5° | Tab. 3/4 iter000 | **high**
- Obniżenie kąta main do −6,5° daje Fz≈−502 N i Fx≈28 N (2D) | Tab. 3/4 iter001.5 | **high**
- Najwyższy \|Fz\| 2D w tabeli: overlap −30 mm → Fz≈−565 N | Tab. 3/4 iter003.5 | **high**
- Na pojeździe 3D Cx≈0,72, Cz≈−2,03, d≈−2,80; iteracje zmieniają to marginalnie | tabela s. 32 | **high**
- Nierównomierność Cp w środku ≈ Δ0,2 vs boki; przyczyna: lokalna zmiana efektywnego α | tekst s. 20 + analizaa wektorów s. 23 | **high**
- Skrócenie 1. elementu + nowy gap/overlap wyrównuje Cp w środku 3D | opis iter002 s. 31 | **med** (jakościowo z rys.; siły prawie bez zmian)
- Hybryda środka/zewnątrz jest obiecująca | opis iter003 s. 33 | **med** (brak tabeli sił)
- Zysk 2D przenosi się 1:1 na lap time / cały pakiet | brak danych torowych | **low** (nie wnioskować)
