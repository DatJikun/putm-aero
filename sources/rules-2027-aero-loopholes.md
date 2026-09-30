# Regulamin 2027 — szare strefy, dźwignie i loophole'y aero

**Dokument roboczy dla PUTM Aero.**  
Źródło: wyciąg *Formula Student Rules 2027 — Aerodynamics Extract* (`team/rules-2027-aero-extract.pdf`, dump `.txt`). Claims i diff vs 2026: [fs-rules-2027-t8.md](fs-rules-2027-t8.md). Wersja 2026: [rules-aero-boxes-loopholes.md](rules-aero-boxes-loopholes.md).  
**Nie jest to zachęta do łamania ducha przepisów** — poniżej luki / niejasności *w tekście* i dźwignie, które nowy envelope otwiera, z oceną ryzyka Scrutineering.

**Flagi pewności / ryzyka:**  
- **H** = wprost z tekstu wyciągu  
- **M** = wynika z połączenia kilku reguł / wymaga interpretacji  
- **L** = spekulacja — nie opierać decyzji projektu

**Zastrzeżenie źródła:** wyciąg nie jest oficjalnym PDF, nie ma rysunków (Fig. 5, figura T 8) ani części rozdziałów (T 9, T 11.11, T 11.12, T 1.1.16, T 4). Każdy punkt z ryzykiem **M** trzeba potwierdzić w pełnym PDF 2027 i w Rules Q&A **przed** zamrożeniem CAD.

---

## 0. Mapa envelope 2027 (żeby luki były widać)

Płaszczyzny: **A** = pionowa przez leading edge przednich opon; **HR** = pionowa przez front face head restraint support (most rearward, bez padów).

| Strefa (side view) | Wysokość | Szerokość | Dodatkowo |
|--------------------|----------|-----------|-----------|
| przed **A** (max 700 mm przed oponą) | < 350 mm | **brak limitu w T 8.2.2** | T 2.1.3 keep-out 75 mm przed oponą (outboard bez końca); T 2.1.4 dwa prostopadłościany 75×250 |
| **A → HR** | < płaszczyzna przez górne punkty opon | do zewn. płaszczyzny opon | keep-out ±75 mm wokół opon, outboard bez końca |
| za **HR**, poniżej góry opon | < góra opon | do zewn. płaszczyzny opon | keep-out tylnej opony do 700 mm |
| za **HR**, góra tylnej opony → 700 mm | — | ≤ wewn. punkt tylnej opony **−150 mm** | dodatkowy keep-out (tylko w pasie ±75 mm wokół tylnej opony) |
| za **HR**, 700 → 1100 mm | < 1100 mm | do **zewn.** punktu tylnej opony | keep-out tylnej opony **kończy się na 700 mm** |
| wszystko | max 250 mm za tylnymi oponami | — | any suspension setup, z/bez kierowcy (T 8.2.4) |

Przekrój za HR (widok z tyłu, połowa auta, oś symetrii po lewej):

```
wys.
1100 ┌──────────────────────────────────────────┐
     │  AERO DOZWOLONE do ZEWN. krawędzi opony  │   (T 8.2.2 b3)
 700 ├───────────────────────┬──────────────────┤
     │ aero do (wewn.        │ ZAKAZ aero       │   (T 8.2.2 b2)
     │ opony − 150 mm)       │ (150 mm + opona) │   + keep-out T 2.1.3 w pasie ±75 mm opony
góra ├───────────────────────┴──────┬───────────┤
opony│ aero do zewn. płaszczyzny    │  OPONA    │   (T 8.2.2 b1)
     │ opon (keep-out ±75 mm opony) │           │
   0 └──────────────────────────────┴───────────┘
     oś auta          wewn. kraw. −150 │ wewn. │ zewn.
```

---

## A. Dźwignie o dużej wartości dla naszych celów (max DF, balans → 50/50, Endurance)

### A1. RW na pełną szerokość w pasie 700–1100 mm — **H** (to nie luka, to nowa reguła)
- **Reguła:** T 8.2.2 b3 + T 2.1.3 (keep-out tylnej opony tylko do 700 mm).
- **Co daje:** górne elementy RW mogą sięgać do **zewnętrznej** krawędzi tylnych opon, także **nad** oponami. Rozpiętość rośnie o ~2 szerokości opony względem 2026 (liczba w mm = z CAD).
- **Dla nas:** najprostsza droga do cofnięcia balansu z ~61,6% bez zdejmowania DF z przodu. H1 trzeba przeliczyć na nowy box: pionowa „wysokość stosu” elementów na pełnej szerokości to **700–1100 mm**, a część poniżej 700 mm musi być węższa.
- **Ryzyko Scrutineering:** **niskie** (tekst jednoznaczny). Ryzyka techniczne: sztywność T 8.3 przy większej rozpiętości, masa, wir krawędziowy nad oponą (sprawdzić CFD, także w yaw).
- **Uwaga compliance:** obecny RW (RWiter017) ma endplate'y na wewnętrznej krawędzi tylnej opony. Jeśli schodzą poniżej 700 mm, **w 2027 prawdopodobnie nie przejdą** (pas 150 mm inboard) — **sprawdzić w CAD**. **M**

### A2. Endplate / mocowania RW przez „zakazany” pas (góra opony → 700 mm) — **M**
- **Reguły:** T 8.2.2 b2, T 8.1.1 (mounting ≠ aero, *„unless it is intentionally designed to be one”*), T 2.1.3 b3 (dodatkowy keep-out *„bounded longitudinally by the 75 mm keep-out-zone of the rear tire”*).
- **Luka:** pas 150 mm inboard od opony obowiązuje w T 8.2.2 **tylko aero devices**, a keep-out T 2.1.3 (dla *każdej* części) obowiązuje tylko wzdłużnie w strefie ±75 mm wokół tylnej opony. Zostaje **okno ok. 175 mm** wzdłużnie: od (tył opony + 75 mm) do (tył opony + 250 mm). Tam **nieaerodynamiczne** mocowanie może przejść przez pas na pełnej szerokości.
- **Wariant „split endplate”:** dolna płyta na pełnej szerokości **poniżej góry opony** (legalna: T 8.2.2 b1) + górna płyta 700–1100 mm, połączone w oknie 175 mm cienkimi, okrągłymi/strukturalnymi łącznikami. Aero ciągłego endplate'u nie da, ale mocowanie wtedy jest zewnętrzne, a środek RW zostaje wolny.
- **Typowa interpretacja sędziów:** płaski „słup” wyglądający jak endplate = aero device → nielegalny w pasie. Rura / pręt / cięgno o przekroju strukturalnym = mounting.
- **Ryzyko:** **średnie** dla okrągłych łączników; **wysokie** dla płaskich profili. Bezpieczna alternatywa: swan-neck / pylony centralne w obrębie (wewn. opony −150 mm), endplate'y tylko 700–1100 mm.

### A3. Wysoka powierzchnia na pełnej szerokości tuż za HR (przed tylną osią) — **M**
- **Reguły:** T 8.2.1 b2 (<1100 mm za HR — bez ograniczenia „za tylnymi oponami”), T 8.2.2 b3.
- **Luka:** strefa 700–1100 mm na pełnej szerokości zaczyna się od płaszczyzny **HR**, nie od tylnej osi. Tekst dopuszcza drugą wysoką powierzchnię (np. nad sidepodami / za zagłówkiem) albo mocno wysunięty do przodu RW, sięgający nad tylne opony.
- **Dla balansu:** DF przyłożony w okolicy 50% rozstawu osi „ciągnie” balans w stronę 50/50 bez zmiany FW; RW za osią daje więcej tyłu na jednostkę DF. Do sprawdzenia CFD jako **1 case** (położenie x górnego elementu), nie jako default.
- **Niewiadome:** rollover protection envelope (T 1.1.16), wymogi wyjścia kierowcy / widoczności, montaż do main hoop — **nie ma ich w wyciągu**. Ryzyko: **średnie**; możliwe pytania Tech o bezpieczeństwo przy dachowaniu.

### A4. Położenie płaszczyzny HR jako zmienna projektowa — **M**
- **Reguła:** T 8.2.1 — granica 1100 mm liczona od HR support *„set to its most rearward position”*.
- **Luka / dźwignia:** im bardziej do przodu HR support (i im mniejszy zakres regulacji do tyłu), tym dłuższa strefa 1100 mm / pełnej szerokości. Zyskuje się miejsce wzdłużne dla RW (A1/A3).
- **Ograniczenia:** ergonomia i szablony kierowcy (rozdział T 4, spoza wyciągu). Decyzja razem z Chassis/Ergo. Ryzyko: **niskie**, jeśli HR spełnia swoje reguły; pomiar na Tech.

### A5. Średnica opon ustala dwie granice — **H** (sprzężenie, nie luka)
- **Reguły:** T 8.2.1 b3 (środek auta < góra opon), T 8.2.2 b1–b2 (próg „góra tylnych opon”).
- **Efekt:** większe OD tylnej opony → wyższy limit środka auta **i** węższy pas zakazany (od góry opony do 700 mm) → więcej objętości na pełnej szerokości nisko za HR. Wybór opon/felg to decyzja VD, ale aero powinno znać ten koszt/zysk.
- **Ryzyko:** brak (fizyka reguły).

---

## B. Front / FW

### B1. Skok wysokości za płaszczyzną A (LE przednich opon) — **H**
- **Reguły:** T 8.2.1 b1 (<350 mm przed A) vs b3 (za A: < góra opon); T 2.1.3 blokuje strefę outboard przy oponie.
- **Dźwignia:** elementy FW / turning vanes / flapy **inboard** od przednich opon, które sięgają za płaszczyznę A, mogą być wyższe niż 350 mm (do góry opon). Przydatne do sterowania outwash / wake opony → korzyść dla UT/RW, nie do dokładania DF z przodu.
- **Ryzyko:** **niskie** (tekst jasny); pomiar położenia A przy kołach prosto (T 8.2.4).

### B2. FW outboard: 250 → 350 mm — **H**
- W 2026 outboard przed osią było <250 mm; w 2027 cała strefa przed A <350 mm. Wyższe endplate'y / kaskady outboard do sterowania wake przedniej opony.
- **Pułapka:** keep-out T 2.1.3 biegnie teraz outboard **bez końca** — nic w pasie 75 mm przed przednią oponą, także daleko na zewnątrz. Endplate'y FW szersze niż opona muszą kończyć się > 75 mm przed oponą. Ryzyko compliance: **wysokie**, jeśli obecny FW ma tam elementy.

### B3. Szerokość FW przed płaszczyzną A nieograniczona w T 8.2.2 — **M**
- **Reguła:** T 8.2.2 b1 dotyczy tylko aero *„further rearward than a vertical plane through the leading edge of the front tire”*. Przed A szerokość ograniczają tylko keep-out 75 mm (T 2.1.3), T 2.1.4 i długość 700 mm (T 8.2.3).
- **Wartość dla nas:** **niska** — więcej DF z przodu działa przeciw celowi balansu; szerokie FW = pachołki, uszkodzenia. Ważne jako wiedza, że inni mogą to zrobić.
- **Ryzyko:** **średnie** — pełny PDF może mieć limit, którego wyciąg nie ma; sędziowie mogą powołać się na ducha przepisów.

### B4. T 2.1.4 variable keep-out — interpretacja decyduje o FW — **M** (pytanie nr 1 do Q&A)
- **Tekst:** dwa niezależne prostopadłościany 75 × 250 mm × ∞, na ziemi, równoległe do osi, nie outboard od przednich opon; *„No part of the vehicle forward of the vertical plane through the leading edge of the front tires must enter…”*.
- **Niejasne:** (1) który wymiar to wysokość — 75 czy 250 mm (Fig. 5 brak); (2) **kto wybiera położenie** („variable”): zespół czy Tech.
- **Scenariusze:**
  - Zespół wybiera położenie → projektujemy FW z dwoma „tunelami” tam, gdzie i tak jest wysoko (np. pod nosem / przy przejściu mainplane → nos). Koszt DF mały.
  - Tech wybiera dowolnie → warunek musi być spełniony dla **każdego** położenia, czyli w praktyce (przy wysokości 75 mm) FW i nos ≥ 75 mm nad ziemią na prawie całej szerokości inboard od zewn. krawędzi opon. Duża strata ground effect FW.
- **Luka w tekście:** reguła dotyczy tylko części **przed** płaszczyzną A. Niskie elementy za A (splitter / T-tray pod nosem między kołami, dolne części FW sięgające za LE opon) obowiązuje tylko GC 30 mm (T 2.2.1). **M**
- **Ryzyko:** decyzja FW sezonu 2027 zależy od odpowiedzi Q&A — **nie zamrażać FW przed nią**.

---

## C. Środek auta (A → HR)

### C1. Sidepod / kanały chłodzenia vs „aero device” — **M**, ryzyko wysokie
- **Reguły:** T 8.1.1 (aero = struktura *„increasing the downforce … and/or lowering its drag”*), T 1.1.2 (bodywork = outermost surface / fairings / covers), T 8.2.1 b3.
- **Luka:** limit „góra opon” dotyczy **aero devices**. Kanał chłodnicy / obudowa zaprojektowana pod chłodzenie to bodywork, więc tekst nie ogranicza jej wysokości w środku auta.
- **Pułapka w drugą stronę:** definicja obejmuje też urządzenia **zmniejszające opór** — owiewka wyraźnie „pod opór” powyżej góry opon może zostać uznana za aero device → nielegalna.
- **Typowa interpretacja:** jeśli kształt wyraźnie generuje DF (profil, dyfuzor, lotka) → aero. Ryzyko: **wysokie** przy agresywnych kształtach; mieć dokumentację funkcji chłodzenia.

### C2. „Horizontal plane” przez górne punkty dwóch opon — **M**
- **Reguła:** T 8.2.1 b3 — *„virtual horizontal plane defined by the topmost points of the two tires on the left or right side … whichever side is closer”*.
- **Niejasne:** jeśli góra przedniej i tylnej opony jest na różnej wysokości (inne OD, ciśnienie, ugięcie), dwa punkty nie wyznaczają płaszczyzny **poziomej**. Który punkt?
- **Rekomendacja:** projektować pod **niższy** z dwóch; interpretacja „wyższy” = ryzyko **wysokie**. Zapytać w Q&A, jeśli planujemy różne opony przód/tył.

### C3. Obecne SW / lotki boczne — ryzyko compliance — **M**
- W 2026 limit środka to 500 mm; w 2027 to góra opon (zwykle niżej). Lotki SW z iteracji UT/FW („dwie lotki SW”, „lotka obok koła” — FWiter001) trzeba sprawdzić w CAD pod: (1) wysokość < góra opon, (2) keep-out ±75 mm wokół opon **outboard bez końca**.

---

## D. Bez zmian względem 2026, ale ważne przy nowym envelope

### D1. Pasywne ugięcie / „pasywny DRS” (testy 019/020) — **M**
- **Reguły:** T 8.3.1–2 (tylko przypadki 200 N / 50 N), T 8.2.4, T 2.2.2.
- Ugięcie pod realnym obciążeniem aero nie jest wprost limitowane poza testami T 8.3. Szerszy RW (A1) = większe siły → większe ugięcie. Warunek: envelope spełniony w każdym stanie i zero kontaktu z torem.
- **Ryzyko:** **średnie** (sędziowie mogą obciążyć ręcznie inaczej niż zakładamy). Wentylatory i DRS aktywny: **brak w wyciągu** — nie wnioskujemy.

### D2. Zmiana kątów flapów między eventami (IN 1.5.1) — **M**
- *„Adjustment of winglet angles, but not the position of the complete aerodynamic device”* — setup Autocross (max DF) vs Endurance (mniej oporu) bez DRS. „Winglet” nie jest zdefiniowany; praktyka FS: flapy RW/FW z regulowanym kątem. Ryzyko **niskie–średnie** — pozycje zaprezentować na Tech.

### D3. Szerokość przy camberze / ugięciu opony — **H**/**M**
- Pas 150 mm liczony od *„most inboard point of each rear tire”*. Przy ujemnym camberze górna część opony jest bardziej inboard → pas się przesuwa. T 8.2.4 = najgorszy setup. Projektować z zapasem, mierzyć przy max camberze.

---

## E. Pytania do Rules Q&A / pełnego PDF (w kolejności wagi)

1. **T 2.1.4:** orientacja prostopadłościanów (75 czy 250 mm wysokości) i kto wybiera ich położenie (zespół / Tech). → decyduje o GC FW.
2. **T 8.1.1 vs T 8.2.2 b2:** czy strukturalne łączniki endplate'u RW w pasie „góra opony – 700 mm” za strefą keep-out opony są mounting, czy aero (A2).
3. **T 8.2.1 b3:** definicja płaszczyzny przy różnej wysokości góry opon przód/tył (C2).
4. **T 8.2.2:** czy aero przed płaszczyzną A ma jakikolwiek limit szerokości poza T 2.1.3/T 2.1.4 (B3).
5. Wysokie powierzchnie 700–1100 mm tuż za HR: wymogi rollover envelope / wyjścia kierowcy (A3).
6. Czy T 11.11.1 (wentylatory 500 W) i brak zakazu DRS nadal obowiązują (u nas i tak OUT; wiedza o konkurencji).

---

## F. Priorytety dla PUTM (propozycja Źródeł — decyzja = Spec)

| # | Co | Dlaczego | Ryzyko |
|---|----|----------|--------|
| 1 | Przeliczyć box RW 2027 w CAD (pełna szerokość 700–1100 mm, pas −150 mm) i sprawdzić compliance RWiter017 | największa zmiana, bezpośrednio pod balans | niskie |
| 2 | Wysłać Q&A dla T 2.1.4 zanim ruszy FW 2027 | może wymusić ≥75 mm GC FW | — |
| 3 | Case CFD: RW pełnej szerokości (3-el.) vs obecny span, ten sam profil | Δ Cz tył / balans / Cx | niskie |
| 4 | Sprawdzić SW / lotki boczne / FW pod nowy keep-out i „góra opon” | compliance | wysokie, jeśli nie sprawdzimy |
| 5 | Opcjonalnie: split endplate (A2) i wysunięty górny element (A3) jako osobne case'y | dodatkowy DF tył / balans | średnie |

*Koniec briefu. Źródło: wyciąg FS Rules 2027 (nieoficjalny). Nie wymyślano wymiarów spoza tekstu — liczby w mm dla naszego auta = z CAD.*
