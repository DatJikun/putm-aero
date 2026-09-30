# Formula Student Rules 2027 — T8 aero (claims z cytatami + diff vs 2026 v1.1)

**Źródło:** *Formula Student Rules 2027 — Aerodynamics Extract* (EN), stopka: „Source: Formula Student Rules 2027 Version 1.0, uploaded by the user.”  
**PDF:** `team/rules-2027-aero-extract.pdf` · **dump tekstowy:** `team/rules-2027-aero-extract.txt`  
**Poprzedni sezon (do porównania):** [fs-rules-2026-t8.md](fs-rules-2026-t8.md) · `team/rules-raw.txt`  
**Loophole'y / szare strefy 2027:** [rules-2027-aero-loopholes.md](rules-2027-aero-loopholes.md)  
**Boxy w CAD (STEP):** [`team/cad-boxes/`](../team/cad-boxes/README.md)

Tu tylko **cytaty, claims i różnice**. Decyzje projektu = Spec / lead, nie ten plik.

---

## ⚠️ Status źródła

| Fakt | Pewność |
|------|---------|
| Plik to **wyciąg** (ReportLab, autor anonimowy, utworzony 2026-09-30), **nie** oficjalny PDF FS | **high** (metadane PDF) |
| Brak rysunków (Fig. 3, Fig. 5, figura envelope T 8), brak changelogu, brak numeru strony oryginału poza „Original rules: pp. …” | **high** |
| Brak w wyciągu: **T 11.11.1** (wentylatory 500 W), **T 11.12.3** („box defined in T 8.2”), **T 9** (CGS/HPHS), T 2.3.3 (vent holes), T 1.1.16 | **high** — brak w wyciągu **≠** usunięte z regulaminu |
| IN 1.5.1 w wyciągu kończy się na „(De-)Coupling of actuators…” — w 2026 lista ma jeszcze 2 punkty (sensor covers, LV batteries) + zdanie o innych modyfikacjach | **high** — prawdopodobnie przycięte, nie zmienione |

**Przed zamrożeniem CAD/CFD na 2027:** potwierdzić każdy wiersz „ZMIANA” poniżej w **pełnym oficjalnym PDF 2027** (+ Fig. 5 i figura T 8) i Rules Q&A.

---

## Diff 2026 v1.1 → 2027 (wyciąg)

| Reguła | 2026 v1.1 | 2027 | Status |
|--------|-----------|------|--------|
| **T 2.1.3** keep-out kół — zasięg boczny | od *outside plane* do *inboard plane* koła | *„extends laterally outward from the inboard plane of the wheel/tire assembly **indefinitely**”* | **ZMIANA** (ostrzej) |
| **T 2.1.3** keep-out przy tylnych kołach — wysokość | brak limitu wysokości | *„…at the rear tires extends up to **700 mm** above the ground”* | **ZMIANA** |
| **T 2.1.3** dodatkowa strefa | — | od góry tylnej opony do **700 mm**, **150 mm inboard** od inboard plane tylnej opony; wzdłużnie w granicach strefy 75 mm tylnej opony | **NOWE** |
| **T 2.1.4** variable keep-out | — | przed płaszczyzną przez *leading edge* przednich opon: 2 niezależne, nieprzecinające się prostopadłościany **75 × 250 mm × ∞**, jedna ściana na ziemi, równoległe do osi auta, nie outboard od przednich opon (Fig. 5) | **NOWE** |
| **T 8.2.1** strefa przednia | przed **HR**: <500 mm; przed **osią** i outboard od most inboard front tire: <250 mm | przed płaszczyzną przez **leading edge przednich opon**: <**350 mm** (cała szerokość) | **ZMIANA** |
| **T 8.2.1** strefa środkowa | (mieściła się w „przed HR <500 mm”) | *„All other”* (między LE przednich opon a HR): poniżej płaszczyzny przez **górne punkty opon** (przód+tył, strona bliższa urządzeniu) | **ZMIANA** (ostrzej) |
| **T 8.2.1** za HR | <1,1 m | <**1100 mm** | bez zmian |
| **T 8.2.2** nisko | <500 mm i za **osią** → do płaszczyzny most outboard przód+tył | **poniżej góry opon** i za **LE przednich opon** → to samo | **ZMIANA** (próg + granica) |
| **T 8.2.2** pas pośredni | (część „>500 mm”) → nie outboard od **most inboard** tylnej opony | **góra tylnych opon … 700 mm** → min. **150 mm inboard** od most inboard tylnej opony | **ZMIANA** (ostrzej) |
| **T 8.2.2** wysoko | >500 mm → nie outboard od **most inboard** tylnej opony | **700 … 1100 mm** → nie outboard od **most outboard** tylnego koła/opony | **ZMIANA** (dużo luźniej) |
| T 8.2.3 długość | 250 mm za / 700 mm przed | 250 mm za / 700 mm przed | bez zmian |
| T 8.2.4 warunek pomiaru | koła prosto, any suspension setup, z/bez kierowcy | to samo | bez zmian |
| T 8.1.1 definicja | aero device / mounting | to samo | bez zmian |
| T 8.3.1–2 sztywność | 200 N / 225 cm² ≤10 mm; 50 N ≤25 mm | to samo | bez zmian |
| T 1.1.2, T 1.1.18 | bodywork / surface envelope | to samo | bez zmian |
| T 2.1.2, T 2.2.1–2, T 2.3.2, T 2.3.4, T 2.4.1 | 30 mm GC, zakaz skirtów, concave, R38, R3/R1 | to samo | bez zmian |
| T 3.19.4, T 3.20.1–2 | IA + non-crushable, attachment za AIP | to samo | bez zmian |
| A 6.6.8 | 2 osoby przy FW przy pchaniu | to samo | bez zmian |
| IN 1.5.1 | kąty winglet'ów po Tech OK, pozycja urządzenia nie | to samo (lista przycięta) | bez zmian |

---

## Claims (claim | cytat / dowód | confidence)

| claim | evidence | confidence |
|-------|----------|------------|
| Aero przed płaszczyzną przez LE przednich opon: **< 350 mm** od ziemi, bez podziału inboard/outboard | T 8.2.1 b1 | **high** (wyciąg) |
| Aero za płaszczyzną HR (front face support, bez padów, most rearward): **< 1100 mm** | T 8.2.1 b2 | **high** |
| Pozostałe aero (między LE przednich opon a HR): poniżej *virtual horizontal plane* przez górne punkty obu opon po stronie bliższej urządzeniu | T 8.2.1 b3 | **high** (tekst); geometria płaszczyzny przy różnych OD przód/tył = **TBD** |
| Aero poniżej góry opon i za LE przednich opon: nie szersze niż pionowa płaszczyzna styczna do most outboard przód i tył | T 8.2.2 b1 | **high** |
| Aero między górą tylnych opon a 700 mm: min. **150 mm inboard** od most inboard tylnej opony | T 8.2.2 b2 | **high** |
| Aero 700–1100 mm: do **most outboard** punktu tylnego koła/opony (pełna szerokość auta) | T 8.2.2 b3 | **high** |
| Keep-out kół ±75 mm (side view) biegnie od inboard plane koła **na zewnątrz bez końca**; przy tylnych kołach do 700 mm | T 2.1.3 b2 | **high** |
| Dodatkowy keep-out: góra tylnej opony → 700 mm, 150 mm inboard od inboard plane tylnej opony, wzdłużnie w strefie 75 mm | T 2.1.3 b3 | **high** |
| Przed LE przednich opon: 2 prostopadłościany 75 × 250 mm × ∞ na ziemi, nie outboard od przednich opon; żadna część auta nie może w nie wejść | T 2.1.4 | **high** (tekst); **który wymiar to wysokość** i **kto wybiera położenie** = **TBD** (Fig. 5 brak) |
| Długość: max 250 mm za tylnymi oponami, max 700 mm przed przednimi | T 8.2.3 | **high** |
| Sztywność, GC 30 mm, zakaz kontaktu z torem, promienie krawędzi — jak w 2026 | T 8.3, T 2.2, T 2.4.1 | **high** |
| Szerokość aero **przed** LE przednich opon nie jest ograniczona w T 8.2.2 (tylko T 2.1.3 / T 2.1.4 / T 8.2.3) | T 8.2.2 b1 obejmuje tylko *„further rearward than a vertical plane through the leading edge of the front tire”* | **high** (cisza w wyciągu); całość = **TBD** (pełny PDF) |
| Wentylatory ≤500 W, DRS/active aero | **brak w wyciągu** — nie wnioskujemy | **low** (brak danych) |

---

## Cytaty kluczowe (z wyciągu)

**T 8.2.1** — *„All aerodynamic devices forward of a vertical plane through the leading edge of the front tires must be lower than 350 mm from the ground.”* · *„All aerodynamic devices rearward of a vertical plane through the rearmost portion of the front face of the driver head restraint support, excluding any padding, set to its most rearward position must be lower than 1100 mm from the ground.”* · *„All other aerodynamic devices must be lower than the virtual horizontal plane defined by the topmost points of the two tires on the left or right side of the vehicle, whichever side is closer to the device.”*

**T 8.2.2** — *„All aerodynamic devices lower than the topmost points of the tires and further rearward than a vertical plane through the leading edge of the front tire, must not be wider than a vertical plane touching the most outboard point of the front and rear wheel/tire.”* · *„All aerodynamic devices between the top edge of the rear tires and 700 mm above the ground, must not be wider than 150 mm inboard of the most inboard point of each rear tire.”* · *„All aerodynamic devices between 700 mm and 1100 mm above the ground, must not extend outboard of the most outboard point of the rear wheel/tire.”*

**T 2.1.3** — *„This keep-out zone extends laterally outward from the inboard plane of the wheel/tire assembly indefinitely. The keep-out-zone at the rear tires extends up to 700 mm above the ground.”* · *„An additional keep-out-zone extends from the top of the rear tire to 700 mm above the ground and 150 mm inboard from the inboard plane of the rear tire. It is bounded longitudinally by the 75 mm keep-out-zone of the rear tire.”*

**T 2.1.4** — *„No part of the vehicle forward of the vertical plane through the leading edge of the front tires must enter the variable keep-out zone, see Figure 5. It is defined by two independent, non-intersecting, cuboids of 75 mm × 250 mm × infinite length. One infinite-length face must rest on the ground, and the infinite-length edges must be parallel to the vehicle longitudinal axis. The cuboids must not extend outboard of the front tires.”*

---

## Implikacje jako fakty z tekstu (bez decyzji Spec)

- **RW:** część 700–1100 mm może sięgać do **zewnętrznej** krawędzi tylnych opon (2026: do wewnętrznej). Część między górą tylnej opony a 700 mm jest **węższa** niż w 2026 (−150 mm na stronę). Endplate na pełnej szerokości nie może więc zejść poniżej 700 mm (oprócz okna za strefą keep-out opony — patrz loophole'y).
- **Strefa za HR wysoko (700–1100 mm) jest pełnej szerokości także przed tylnymi oponami** — nie tylko nad/za nimi.
- **FW:** centrum 500 → **350 mm**; outboard 250 → **350 mm**; granica strefy przesunięta z osi na **LE przednich opon**. Elementy FW za LE przednich opon (inboard) podlegają limitowi „góra opon”.
- **Środek auta (sidepody, SW, lotki boczne, wysokie części UT) między LE przednich opon a HR:** limit wysokości = **góra opon** (w 2026: 500 mm). Liczba mm = z CAD (OD opon), nie z PDF.
- **Keep-out kół:** nic (także outboard) w pasie ±75 mm przed/za oponą → wąsy / lotki „obok koła” / szerokie endplate'y FW w tym pasie = nielegalne.
- **T 2.1.4:** pod FW / nosem muszą zostać dwa wolne „kanały” 75 × 250 mm. Orientacja i sposób ustawienia (zespół czy Tech) = **pytanie nr 1 do Q&A** — w najgorszym wariancie wymusza ≥75 mm prześwitu FW na prawie całej szerokości.
- Brak wymiarów naszego auta w repo (OD opon, track, pozycja HR, obecna rozpiętość RW / wysokość SW) → przeliczenie boxów w mm = **pomiar z CAD**.
