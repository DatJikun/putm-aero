# Cele pakietu aerodynamicznego

To jest nasza karta założeń. Pisana tak, żeby dało się ją przeczytać rano bez odszyfrowywania skrótów.

**Stan:** ustalone z Mikołajem (wrzesień 2026)  
**Aktualny bolid / punkt odniesienia:** iteracja **RWiter017**

---

## W jednym akapicie

Chcemy **jak największy docisk** przy **możliwie małym oporze**, z balansem blisko **pół na pół**. Najważniejsze są **Endurance** i **Autocross**. Ruchomego DRS nie robimy (tylko układ nieruchomy). Wentylatora spod podłogi nie robimy. Najpierw pracujemy nad **tylnym skrzydłem**, potem nad **podłogą**.

---

## Liczby z RWiter017 (nasz punkt startu)

Policzone u Was we Fluencie przy **15 m/s**, na połowie auta.

| Co | Wartość | Po ludzku |
|----|---------|-----------|
| Opór (Cx) | **1,229** | Im niżej, tym lepiej — byle nie zabić docisku |
| Docisk (Cz) | **−3,682** | Ujemne = docisk; im większa wartość bezwzględna, tym więcej docisku |
| Moment (Cm) | **−0,429** | Do balansu / środka ciśnienia |
| Stosunek docisk/opór | ok. **3,0** | \|Cz\| / Cx |
| Balans na przód | ok. **61,6%** | Z arkusza (z Cm i Cz). Do pół na pół brakuje ok. **12 punktów** — trzeba **cofnąć** docisk (tył / podłoga), nie dokładać samego przodu |

Powierzchnia odniesienia (**Aref**): na połowie auta bierzemy **0,50 m²** (u Was bywa 0,49–0,51). Na cały bolid to ok. **1,0 m²**. Tę samą Aref musi mieć OpenFOAM, inaczej Cx/Cz się „nie zgadzają” mimo tych samych sił.

Długość odniesienia: **1,53 m**. Moment liczymy względem **x = 0,765 m**.

Wariant `RW_iter017.2` (lekko inne Cx/Cz) to tylko sprawdzenie skryptu — **nie** zamienia punktu startu.

`Baseline002` to stary miks części, **nie** aktualny bolid.

---

## Czego nie wpuszczamy do karty

Smoke OpenFOAM na rzadkiej lub dziurawej siatce (ok. 312k komórek, Cd≈1,22 / Cl≈−1,72) to tylko check setupu.
Nie nadpisuje Cx/Cz z RWiter017.
Cudzych absolutnych Cl/Cd z innych teamów też nie wpuszczamy jako naszych targetów.

---

## Cele liczbowe (czego pilnujemy)

1. **Docisk** nie gorszy niż teraz: wartość bezwzględna Cz co najmniej **3,682**.
2. **Opór** możliwie niski; orientacyjnie Cx około **1,23** lub lepiej przy tym docisku.
3. **Balans** w stronę **48–52%** na przód (dziś ~62%).
4. Wszystkie porównania CFD przy **15 m/s** i **Aref = 0,50 m²** na half-car.

---

## Co jest w pakiecie, a czego nie

| Element | Decyzja |
|---------|---------|
| Tylne skrzydło | Robimy. Rozważamy wersję **na 4 elementy** (hipoteza — w publicznych rankingach nie ma na to twardych liczb). |
| Przednie skrzydło | Robimy. |
| Podłoga (i sekcje boczne) | Robimy. |
| Wąsy przy skrzydłach | Jeszcze nie wiadomo — profil dopiero pod konkretne miejsce na aucie. |
| Ruchomy DRS | **Nie.** Tylko pasywny układ. |
| Wentylator spod podłogi | **Nie.** |

---

## Kolejność pracy (zatwierdzona)

1. **Tylne skrzydło** — więcej docisku z tyłu / lepszy pakiet (w tym wariant 4-elementowy).
2. **Podłoga** — druga dźwignia; zanim zamrozicie kształt, policzcie też jazdę w zakręcie (nie tylko na wprost) i złóżcie to na prosty model toru Endurance. Podłoga lubi tracić docisk przy kącie.
3. Odciążenie przodu — **tylko gdy trzeba**.
4. Wąsy — później, jeśli w ogóle.
5. DRS i wentylator — poza grą.

---

## Jak sprawdzamy, że to działa

1. CFD (Fluent u Was; OpenFOAM u CFD#1 do porównania — jak będzie czysty model połowy ze SpaceClaim).  
2. Symulacja toru / pojazdu.  
3. Tor: nitki, ewentualnie wizualizacja przepływu.

Opcjonalnie przed formami: mały wydruk bolidu w skali 1:10 — łapie kolizje ramy i zawieszenia, **nie** liczby aero.

---

## Co mówi literatura topowych EV w Europie (bez wymyślania)

- Po zakazach „powered ground effect” wygrywa **pasywny** duży docisk — spójne z naszym „bez DRS i bez fana”.
- **Podłoga** to ważna dźwignia efektywności (obok tylnego skrzydła).
- Publiczny rząd wielkości z Esslingen: ok. **4,9 / 1,65** (CLA/CDA) — tylko orientacja, **nie** nasz target (inne definicje powierzchni).
- Skrzydła wieloelementowe są standardem; **4 elementy** to nasza hipoteza, nie fakt z rankingów.
- Sam Autocross bez Endurance nie wystarczy — stąd bramka „zakręt + model toru”.

- AMZ / FaSTTUBe / Running Snail: proces i Δ% bez absolutnych Cl/Cd — szczegóły w `SPEC-FROM-OVERNIGHT.md` i `sources/research-amz-berlin-snails-aero.md`.

Szczegóły i cytaty: folder `sources/` w tym repo.

---

## Regulamin (skrót)

Pełne cytaty: `sources/fs-rules-2026-t8.md`.

Urządzenia aero muszą mieścić się w boxach z regulaminu 2026. DRS w tekście T8 nie jest wprost zakazany, ale **u nas i tak go nie robimy**. Wentylatory mają limit mocy w regulaminie — **u nas i tak ich nie ma w pakiecie**.

---

## Co dopisał nocny research (bez zmiany liczb)

- **3 elementy** tylnego skrzydła = domyślna ścieżka; **4 elementy** = jeden case porównawczy, nie gotowy target.
- **Podłoga:** projekt pod prostą **i** zakręt (minimum jeden–dwa kąty), nie tylko peak na wprost.
- Pełniejsze spięcie: `SPEC-FROM-OVERNIGHT.md`.

## Co jeszcze wiszą

1. Ostateczna decyzja o wąsach (po doborze profilu).  
2. Mapa / zdjęcie funkcji celu od Mikołaja (obiecał wrzucić).  
3. Eksport ze SpaceClaim (szczelny, na pół) pod OpenFOAM — to blokuje CFD#1, nie tę kartę.

---

*Bez nowych liczb względem ustaleń z 1.09.2026 — tylko czytelniejszy zapis.*
