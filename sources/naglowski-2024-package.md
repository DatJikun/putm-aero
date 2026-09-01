# Analiza modyfikacji pakietu aerodynamicznego bolidu klasy Formuła Student / Kacper Nagłowski / 2024 / praca inżynierska

**Uczelnia:** Politechnika Poznańska, Wydział Inżynierii Lądowej i Transportu  
**Promotor:** dr inż. Jerzy Kupiec  
**Data:** Poznań, 2024  
**Źródło PDF:** załącznik (56 stron); ekstrakcja `pdftotext -layout`

## Cel pracy

Zbadać wpływ **generatorów wirów strumieniowych („wąsów”)** o profilu **Selig S1223** na pakiet aero bolidu FS: docisk, opór, efektywność Cz/Cx i **balans**, w zależności od **położenia, wielkości i liczby** generatorów — oraz wskazać konfigurację optymalną.

## Metody (CAD/CFD/eksperyment)

- **Tylko CFD 3D** (brak eksperymentu).
- CAD: **SolidWorks**; domena: **ANSYS SpaceClaim**; solver/post: **Fluent** + **CFD-Post**.
- Steady, pressure-based, absolute velocity; powietrze **ρ=1,225 kg/m³**, μ=1,7894×10⁻⁵ kg/(m·s); model turbulencji **k-ε** (RANS).
- Inlet/outlet / ground: **15 m/s**; koła: **72,9 rad/s** (R≈0,20574 m); wentylator chłodzenia: **510 rad/s**; **2000** iteracji.
- Metryki: Cm, Cx, Cz, balans przód [%], efektywność = Cz/Cx; siły Fz/Fx całego auta i komponentów (FW, RW, UT, whiskers).

## Kluczowe liczby (Cl, Cd, downforce, drag, balans, energia, prędkości) — TYLKO z tekstu

Warunki: **V = 15 m/s**.

### Tabela 5.2 — współczynniki (s. 31)

| iter | Cm | Cx | Cz | Balans przód [%] | Efektywność Cz/Cx |
|---|---|---|---|---|---|
| iter000 (baseline) | −0,418 | **1,453** | **−4,071** | **60,3** | **−2,802** |
| iter094 | −0,316 | 1,482 | −4,086 | 55,7 | −2,757 |
| iter100 | −0,240 | 1,498 | −4,084 | 55,9 | −2,726 |
| iter102 | −0,244 | 1,482 | −4,064 | 56,0 | −2,742 |
| iter103 | −0,194 | 1,500 | −4,076 | 54,8 | −2,717 |
| iter110 | −0,316 | 1,482 | −4,090 | 57,7 | −2,760 |
| iter111 | −0,270 | 1,480 | −4,064 | 56,6 | −2,746 |
| **iter111.4** | −0,298 | **1,480** | **−4,100** | **57,3** | **−2,770** |

### Tabela 5.3 — siły [N] (s. 32)

| iter | Fz_all | Fx_all | Fz przód | Fz tył | Fz_fw | Fz_rw | Fz_ut | Fz_whiskers |
|---|---|---|---|---|---|---|---|---|
| iter000 | **−561,00** | **199,84** | −338,03 | −222,94 | −221,05 | −135,21 | −201,88 | — |
| iter094 | −562,88 | 204,04 | −325,10 | −238,00 | −216,38 | −141,64 | −207,76 | 5,40 |
| iter100 | −562,72 | 206,36 | −314,49 | −248,34 | −213,02 | −148,00 | −212,04 | 10,08 |
| iter102 | −560,02 | 204,32 | −313,61 | −246,41 | −214,64 | −150,30 | −207,44 | 10,54 |
| iter103 | −561,62 | 206,67 | −307,60 | −254,13 | −212,50 | −154,52 | −208,98 | 11,58 |
| iter110 | −563,74 | 204,16 | −325,38 | −238,28 | −217,60 | −145,64 | −205,38 | 6,22 |
| iter111 | −560,18 | 204,01 | −317,24 | −242,83 | −217,36 | −150,22 | −205,64 | 11,60 |
| **iter111.4** | **−565,16** | **203,91** | −323,58 | −241,45 | −220,04 | −145,62 | −209,86 | **12,92** |

Dodatkowe z tekstu interpretacji:
- iter094 vs baseline: ΔFz RW **+6,4 N**, UT **+6,6 N** (s. 35).
- iter111.4: „najwyższa siła docisku… **565,16 N** przy **15 m/s**” oraz najniższy opór wśród wariantów **z** wąsami (s. 50).
- Literatura w pracy: opór aero dominuje powyżej ~**65–80 km/h**; koła mogą redukować docisk o ~**11%** (Piechna) — kontekst teoretyczny, nie wynik własnej CFD.

**Tylko na rysunkach:** mapy Cp / CpT, porównania energii w przekrojach (Rys. 5.9–5.44) — wartości punktowe poza tabelami nie odczytywano.

## Konfiguracje i geometria (profile, kąty, liczba elementów, DRS itd.)

- Profil wąsa: **Selig S1223**.
- Start (iter094): cięciwa **100 mm**, szerokość **183 mm**, **α = 10°**; położenie względem styku przedniego koła — Rys. 5.1.
- **iter100:** cięciwa **216 mm** (to samo miejsce).
- **iter102:** drugi generator, szerokość **200 mm**.
- **iter103:** oba generatory **+50 mm do przodu** vs iter102.
- **iter110:** przesunięcie vs iter094 o **86 mm w górę** i **142 mm do tyłu**.
- **iter111:** iter110 + dolny płat jak w iter102.
- **iter111.4:** dolny płat **−50 mm** (w dół) vs iter111 → **wybrana jako najlepsza** pod kątem docisku i oporu wśród badanych.
- Balans: wzór (5.1) z Cz i Cm; uproszczenie — CG dokładnie między osiami.
- **DRS:** brak. Szczegółowa liczba elementów FW/RW / kąty skrzydeł bazowego pakietu: nie rozwijane poza obecnością FW, RW, UT, side wing, whiskers.

## Wnioski projektowe istotne dla NOWEGO pakietu aero

1. Wąsy **S1223** mogą **zwiększyć docisk całego auta**, mimo że **same generują siłę nośną** (Fz_whiskers &gt; 0).
2. Blisko FW: wąs **kradnie** powietrze / podnosi ciśnienie pod FW → spadek Fz_fw i **cofnięcie balansu**.
3. Nad górnym wahaczem: wir **blokuje „brudne” powietrze** na RW → wzrost skuteczności RW.
4. Pozytywny wpływ też na **UT**; netto balans przesuwa się do tyłu, ale nadal **front-biased** (~55–60% przód).
5. Montaż między wahaczami może **rozbić wir** za mocowaniem FW i odzyskać wysokoenergetyczną strugę wzdłuż sidepodów — otwiera miejsce na kolejne urządzenia.
6. **iter111.4** (dolny płat niżej): max \|Fz_all\| (**565 N @ 15 m/s**), niski Fx wśród wariantów z wąsami, efektywność **−2,770** (nadal nieco gorsza niż baseline **−2,802**).
7. Warto kontynuować rozwój wąsów jako elementu pakietu PUT Motorsport, ale **trade-off efektywności vs docisk/balans** trzeba świadomie wybierać pod konkurencję.

## Ograniczenia / czego NIE wnioskować

- Brak walidacji tor/tunel; jeden V=15 m/s; steady RANS k-ε.
- Efektywność baseline (−2,802) nadal lepsza niż iter111.4 (−2,770) — „optymalne” dotyczy głównie **max docisku / niskiego Fx wśród wariantów z wąsami**, nie absolutnego L/D.
- Nie ekstrapolować Δ~4 N docisku na duże zmiany lap time bez modelu dynamicznego.
- Fz_whiskers dodatnie — nie traktować wąsa jako samodzielnego generatora docisku.
- Map CpT tylko jakościowo.

## Claims (bullet list: claim | evidence | confidence high/med/low)

- Baseline @15 m/s: Cx=1,453, Cz=−4,071, balans 60,3%, Fz=−561 N, Fx=200 N | Tab. 5.2–5.3 | **high**
- iter111.4 daje najwyższy \|Fz\| w serii: −565,16 N przy Cx=1,480, balans 57,3% | Tab. 5.2–5.3 + s. 50 | **high**
- Wąsy same w sobie dają Fz &gt; 0 (nośną), np. +5,4…+12,9 N | Tab. 5.3 | **high**
- iter094: +6,4 N na RW i +6,6 N na UT vs baseline, kosztem FW i wzrostu Fx | s. 35 | **high**
- Wąsy przesuwają balans do tyłu, ale przód nadal dominuje | Podsumowanie s. 55 + tabele | **high**
- Wąsy nad wahaczem chronią RW przed brudnym powietrzem | Podsumowanie s. 55 | **med** (interpretacja CFD)
- Stosowanie wąsów jest „pozytywne dla dalszego rozwoju” pakietu | s. 55 | **med** (rekomendacja projektowa)
