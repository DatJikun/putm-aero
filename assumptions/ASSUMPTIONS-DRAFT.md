# Szkic założeń — pakiet aero FS (DRAFT)

**Status:** DRAFT do review Spec / lead (Mikołaj).
**Baza:** wyłącznie ekstrakty w `sources/` oraz indeksy batch A/B (2026-09-01).
**Zasada:** nie inventujemy liczb zespołu. Brakujące dane = **TBD**.
**Pewność:** **H** = bezpośrednio z tabel / tekstu źródła · **M** = interpretacja autora / proxy · **L** = przeniesienie między bolidami / torami.

> Uwaga: ten DRAFT powstał wcześniej niż zamrożenia w INDEX / TARGETS (baseline `RW_iter017`, balans 48–52%, DRS OUT, fan OUT).
> Przy konflikcie wygrywa Spec w `TARGETS.md`.

---

## 1. Cel pakietu (co optymalizujemy: eventy / energia / lap)

Propozycja celu nadrzędnego (do decyzji lead):

| Priorytet | Kryterium | Uzasadnienie ze źródeł | Pewność |
|-----------|-----------|------------------------|---------|
| P1 | **Lap / cornering** — max użyteczny docisk przy akceptowalnym oporze i balansie | Jackson: RW closed → +3,1% cornering @ R=13 m (**H**); Nagłowski optymalizuje max \|Fz\| + balans (**H**) | H (kierunek) |
| P2 | **Energia Endurance (EV)** — min. średnia siła hamująca na modelu toru | Staniszewski 2024: pełny pakiet vs FW&RW → **−2,7%** proxy energii mimo +~10 kg UT (**H** jako F_ham; **M** jako Wh) | H/M |
| P3 | **Accel / proste** — niski drag przy wysokiej V lub DRS open | Jackson: DRS open −35% siły oporu vs closed; +15,7% potencjał accel @25 m/s; Vmax +18,2% vs fixed high-DF (**H**) | H (Jackson); u nas DRS = **OUT** (Spec) |

**Założenie robocze:** pakiet projektujemy pod **ważoną funkcję** (lap + energia), nie pod sam peak Cz przy δ = 0.
Staniszewski 2024 pokazuje, że Cx(δ) pełnego pakietu i FW&RW przecinają się ok. 10° — bez modelu toru nie da się wybrać zwycięzcy po samym Cx (**H**).

**TBD zespołu:** wagi eventów (Autocross / Endurance / Accel / Skidpad), masa bolidu, Crr, pojemność baterii, tor docelowy.

---

## 2. Zakres elementów (IN / OUT / TBD)

| Element | Status | Uzasadnienie | Źródło | Pewność |
|---------|--------|--------------|--------|---------|
| **RW wieloelementowe (3×)** | **IN** | Rdzeń pakietu we wszystkich pracach PUT; 2D Staniszewski: \|Fz\| izolowanego RW ~398→~560–565 N po AOA/overlap/gap; Jackson: E423 3-el. + AOA ~23° przed stall | Staniszewski 2023; Jackson 2018 | H |
| **FW** | **IN** | Dominujący udział Fz_przód u Nagłowskiego (baseline Fz_fw ≈ −221 N z −561 N all); balans front-biased wymaga FW | Nagłowski 2024; Staniszewski 2024 | H |
| **Undertray (UT) / dyfuzor** | **IN** | Baseline Nagłowski: Fz_ut ≈ −202 N; Staniszewski 2024: UT&SW → wyższe \|Cz\| dla każdego δ + −2,7% F_ham mimo +~10 kg | Nagłowski; Staniszewski 2024 | H |
| **Sidepods / sekcje boczne (SW)** | **IN** (z UT) | W Staniszewski 2024 traktowane łącznie jako UT&SW; Nagłowski: side wing w pakiecie; wpływ na uszczelnienie / strugi do RW | Staniszewski 2024; Nagłowski | M (rozdzielczość SW vs UT w źródłach ograniczona) |
| **Wąsy / VG (Selig S1223)** | **IN (kandydat)** w szkicu; Spec = **TBD** | iter111.4: Fz_all −565 N vs −561 N baseline, Cx 1,480, balans 57,3%; wąsy same dają Fz>0, ale chronią RW / wspierają UT | Nagłowski 2024 | H (Δ sił); M (rekomendacja „pozytywne dla rozwoju”) |
| **DRS (ruchome klapy RW)** | w szkicu **TBD**; Spec = **OUT** | Jackson: closed CL_DF=1,15 / CD=1,21; open CL=0,26 / CD=0,79; −35% drag, +18,2% Vmax vs fixed high-DF. W pracach PUT brak DRS. | Jackson 2018 | H (efekt na ich bolidzie); L (przeniesienie na nasz) |
| **Fan / active suction** | **OUT** (na start) | Michalecki: na profilowanej podłodze PM08 \|Cz\| gorszy o ~30%+ (baza −2,036 → best z fan ~−1,36); best płaska+kurtyny+kanał iter107 Cz=−1,589 nadal < bazy. Autor: wyniki nie uzasadniają wdrożenia na zoptymalizowanym UT | Michalecki 2024 | H |
| **Fan + redesign płaskiej podłogi** | **OUT / park** | Potencjał tylko po zmianie architektury UT (płaska + kanały + lokalizacja fan do tyłu); poza zakresem „nowego pakietu” na obecnym undertrayu | Michalecki §6 | M |
| **Proces RP/FDM (model skali)** | **IN (proces)** | Nie element aero, ale gate przed formami: model 1:10 (~15 h / 8 os.) łapie zawieszenie, ramę, fotel, kolizje napędu | Strojny 2015 | H (proces); brak liczb aero |

**Uwaga coupling:** Staniszewski 2023 — przeniesienie optimum 2D RW na 3D bez kompensacji względem body **psuje** zysk.
Pakiet „poświęca” wydajność RW na uszczelnienie przepływu pod elementem boczno-przypodłogowym (**H**/M).
Elementy projektować **jako pakiet**, nie izolowanie.

> Aktualizacja Spec (2026-09-01): ruchomy DRS = **OUT**, wąsy = **TBD**, rozważamy RW **4-el.** — patrz `TARGETS.md`.
> Wiersze powyżej zostawiamy jako historyczny szkic ze źródeł.

---

## 3. Targety mierzalne (propozycje z widełkami + źródło)

Warunek odniesienia w pracach PUT: **V = 15 m/s**, steady RANS k-ε / Realizable k-ε (**H**).
Jackson: inlet **26,8 m/s** — inne skalowanie (**H**).

| Metryka | Propozycja widełek | Źródło / komentarz | Pewność | Status |
|---------|-------------------|--------------------|---------|--------|
| Cz (pełny pakiet, δ=0) | **cel roboczy −3,5 … −4,2** (kierunek Nagłowski); nie mieszać z Cz≈−2,0 z innego modelu (Staniszewski 3D) | Nagłowski baseline −4,071 / iter111.4 −4,100 @15 m/s; Staniszewski 2023 pojazd ~−2,03 = **inny** pakiet/model | H (liczby źródeł); **L** jako target naszego auta bez własnego baseline | **nadpisane Spec:** kotwica Cz = **−3,682** |
| Cx (pełny pakiet, δ=0) | **orientacyjnie 1,45–1,50** przy wysokim DF (Nagłowski); DRS open ~0,8 jeśli wdrożymy | Nagłowski Cx 1,453→1,480; Jackson DRS open CD=0,79 | H | **nadpisane Spec:** Cx ≈ **1,23** |
| Efektywność \|Cz\|/Cx | **nie pogarszać baseline o >~2%** bez świadomej decyzji | Nagłowski: baseline −2,802 vs iter111.4 −2,770 | H | cel jakościowy |
| Balans aero przód | w szkicu **55–60%**; Spec = **48–52%** | Nagłowski Tab. 5.2 vs decyzja lead 2026-09-01 | H (Nagłowski); Spec = decyzja | **Spec wygrywa** |
| Fz @15 m/s (all) | **≥ baseline zespołu**; literaturowo rząd −560…−565 N (Nagłowski) | Tab. 5.3 | H dla ich modelu | **TBD** nasze N |
| Δ energii (proxy F_ham) | **pełny pakiet ≤ konfiguracja bez UT** na modelu toru (kierunek −2–3%) | Staniszewski 2024: −2,7% | H (proxy); M (Wh) | wymaga własnego modelu toru |
| Cornering / accel (jeśli DRS) | Jackson: +3,1% @R=13 m; +15,7% accel @25 m/s; −35% drag open | Jackson | H ich; L nasze | DRS = OUT → nie ścieżka Spec |
| CFD process | mapa **Cx,Cz vs δ** (min. punkty jak Tab. 9: r≈17,6…4,4 m) + model toru | Staniszewski 2024 | H (metoda) | **IN procesu** |
| Walidacja | FSAESim/tor lub WT — Jackson ~97% zgodności accel 75 m (5,31 vs 5,49 s) | Jackson | M | **TBD** plan walidacji |

**Nie używać** tabel 2D izolowanego RW (Staniszewski: Fz≈−398…−565 N) jako targetów całego auta (**H** ostrzeżenie autora).

> Aktualizacja Spec: kotwica to `RW_iter017` (Cx **1,229** / Cz **−3,682**), balans **48–52%** przód, Aref half ≈ **0,50 m²**.
> Widełki literaturowe powyżej = kontekst, nie hard target.

---

## 4. Trade-offy (docisk vs opór vs masa vs energia vs balans)

1. **Docisk ↑ ↔ opór ↑** — Jackson: CL_DF 0,21→1,15 przy CD 0,71→1,21; DRS open odzyskuje CD≈0,79 kosztem docisku (**H**).
2. **Wąsy: docisk auta ↑ ↔ efektywność L/D ↓ ↔ balans do tyłu** — Nagłowski: +~4 N Fz_all, Cx↑, Cz/Cx gorsze (−2,802→−2,770), balans 60,3%→57,3%; wąsy same nośne (+5…+13 N) (**H**).
3. **Podłoga: masa ↑ (~+10 kg) ↔ energia ↓ (proxy)** — Staniszewski 2024: mimo +~10 kg pełny pakiet ma −2,7% F_ham na *tym* torze (**H**/M); na innym torze trzeba przeliczyć udziały r (**H** ograniczenie).
4. **Podłoga peak @δ=0 ↔ utrata w zakręcie** — UT&SW silnie wrażliwe na napływ; FW/RW „płaskie” vs δ (**H**). Projekt pod peak prostej może przegrywać Endurance.
5. **RW 2D optimum ↔ 3D na body** — wydłużenie cięciwy wchodzi w disturbed flow; trzeba skrócić 1. element / hybrydę środka (**H**/M).
6. **Wysoki montaż RW ↔ disturbed flow za kierowcą / roll hoop** — Jackson: montować RW jak najwyżej (**M** rekomendacja).
7. **Fan na profilowanym UT ↔ zysk docisku** — konflikt architektury; proste wstawienie psuje pakiet (~−30% |Cz|) (**H**).
8. **AOA blisko stall ↔ „ładne” liczby CFD** — Jackson stall ~25°, wybrane ~22,8°; nie pchać AOA do stall (**H**).

---

## 5. Ograniczenia CFD / procesowe wyciągnięte z prac

| Temat | Wymaganie / ostrzeżenie | Źródło |
|-------|-------------------------|--------|
| **Mesh / y+** | Realizable/standard k-ε; y+ typowo **30–300** (PUT); Jackson mesh independence ~0,9–1,7 M elementów | Staniszewski 2023; Michalecki; Jackson |
| **V_ref** | PUT konsekwentnie **15 m/s** — porównywalność wewnętrzna OK; nie mieszać z Jackson 26,8 m/s bez przeliczenia | wszystkie PUT |
| **Yaw / δ / coupling** | **Obowiązkowa** siatka punktów vs δśrd — ekstrapolacja z δ=0 niewiarygodna; half-car+symetria OK na wprost, w zakręcie Staniszewski używa pełnej logiki skrętu (Anty-Ackerman) | Staniszewski 2024 |
| **Package coupling** | Optymalizacja izolowanego RW ≠ wynik na pojeździe; FW↔wąsy↔UT↔RW sprzężone (wąs blisko FW kradnie powietrze) | Staniszewski 2023; Nagłowski |
| **Steady RANS** | Brak walidacji WT/tor w pracach PUT; Jackson: walidacja CD vs Monash (~86%) + FSAESim vs tor (~97%) — tylko orientacja | wszystkie |
| **MRF fan** | Steady+MRF; brak mocy napędu fan, masy, debris (Chaparral) | Michalecki |
| **Koła** | Nagłowski: ω=72,9 rad/s @15 m/s; literatura w pracy: koła mogą ciąć DF ~11% (Piechna) — kontekst, nie własny wynik | Nagłowski |
| **RP przed formami** | Model skali FDM przed zamrożeniem geometrii aero/body | Strojny |
| **Metryka energii** | F_ham = Fx + Crr·(mg+Fz) — **nie** Wh z baterii; wymaga Crr, m, modelu toru | Staniszewski 2024 |

---

## 6. Otwarte decyzje do Mikołaja

Część punktów zamknięta w Spec 2026-09-01 (DRS OUT, fan OUT, baseline RW_iter017, balans 48–52%).
Lista zostaje jako ślad decyzji DRAFT.

1. **DRS:** Spec = **OUT**. Czy kiedykolwiek wracamy do pasywnego low-drag (019/020) jako osobnej gałęzi?
2. **Fan:** ostateczne OUT na ten sezon? Potwierdzamy brak ścieżki „fan na obecnym profilowanym UT”.
3. **Wąsy S1223:** w baseline nowego pakietu czy opcjonalny add-on? Akceptujemy lekki spadek L/D i cofnięcie balansu (~60→57% u Nagłowskiego) za +kilka N DF?
4. **Funkcja celu: wagi eventów** — jak ważymy Autocross / Endurance (energia) / Acceleration / Skidpad?
5. **Baseline liczbowy zespołu** — zamknięty: Cx **1,229**, Cz **−3,682**, Cm **−0,429**, Aref half **0,50 m²**. Nadal TBD: masa, Crr, tor docelowy, CG.
6. **Target balans aero %** — Spec: **48–52%** przód (nie 55–60% jak Nagłowski).
7. **Czy mapa CFD vs δ + model toru jest gate’em przed zamrożeniem geometrii UT?** (rekomendacja Staniszewski 2024)
8. **RW: profil i liczba elementów** — kontynuacja 3-el. PUT, plus jeden case 4-el.; nazwy profili RW w Staniszewski 2023 **nie podane**.
9. **Plan walidacji:** tylko CFD, czy CFD + FSAESim/tor / (opcjonalnie) WT?
10. **RP 1:10 przed formami aero** — czy wstawiamy w harmonogram (Strojny)?

---

## 7. Co NIE wynika z tych źródeł

- **Absolutne targety Cx/Cz/Fz naszego nowego bolidu** z samej literatury — liczby Nagłowski vs Staniszewski dotyczą różnych modeli/pakietów; nie da się ich uśrednić w jeden „target FS”. Kotwica zespołu to RWiter017.
- **Zmierzona energia Wh/okrążenie** — tylko proxy F_ham (−2,7%); brak telemetrii baterii.
- **Lap time delta** z ΔFz rzędu kilku niutonów (wąsy) — Nagłowski ostrzega przed ekstrapolacją bez modelu dynamicznego.
- **Zysk 2D RW → lap** — Staniszewski: low confidence; 3D na aucie niemal bez zmian Cx/Cz.
- **Legalność / punktacja DRS i fan** w aktualnym regulaminie FS — Jackson/Michalecki wspominają kontekst, ale to nie binding rules check (patrz `fs-rules-2026-t8.md`).
- **Moc, masa, reliability, bezpieczeństwo fan** — Michalecki: brak.
- **Optymalne kąty FW, liczba elementów FW, geometria dyfuzora szczegółowa** — nie rozwinięte poza obecnością komponentów.
- **Nazwy profili RW PUT** — Staniszewski 2023 nie podaje NACA/Selig dla RW.
- **Koszt / czas / wytrzymałość FDM** — Strojny bez liczb; zero danych aero.
- **Uniwersalność −2,7% energii** na inny tor — wymaga przeliczenia udziałów r.
- **Porównanie bezpośrednie PM08 Cz≈−2 vs pakiet Nagłowski Cz≈−4** jako „postęp sezonu” — różne setupy CFD/geometrie; nie wnioskować rankingu.

---

*Koniec DRAFT. Kolejne kroki po review: trzymać Spec w TARGETS jako źródło prawdy; szkic powyżej = ślad literatury i otwartych TBD.*
