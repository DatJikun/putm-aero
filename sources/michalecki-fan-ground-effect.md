# Analiza generowania efektu przypowierzchniowego za pomocą wentylatora / Jakub Michalecki / 2024 / praca dyplomowa inżynierska (Politechnika Poznańska, Inżynieria Lotnicza; promotor: dr inż. Przemysław Grzymisławski)

## Cel pracy
Zwiększenie współczynnika docisku bolidu klasy Formula Student poprzez wentylator odsysający powietrze spod podłogi (efekt przypowierzchniowy / „fan car”). Praca bada koncepcję na modelu CAD bolidu PM08 (PUT Motorsport) i wytycza dalszą ścieżkę rozwoju rozwiązania.

## Metody
- CAD: SolidWorks; CFD: pakiet Ansys (SpaceClaim → Fluent Meshing → Fluent Solution).
- Turbulencja: realizable k-ε, enhanced wall treatment; solver pressure-based, steady, absolute velocity.
- Obrót wentylatora: MRF (Multiple Reference Frame); prędkość obrotowa domeny wentylatora **510 rad/s**.
- Domenа: połowa bolidu + symmetry; inlet velocity **15 m/s**; limit iteracji **2000**; BOI (Box of Influence) z elementami od 0,256 m do 0,0005 m na powierzchni wentylatora.
- y+ docelowo w zakresie **30–300** (opisano jako wystarczający dla przyjętego modelu warstwy przyściennej).
- Serie: (A) aktualna geometria podłogi PM08 — iter000–004; (B) płaska podłoga ± kurtyny boczne — iter100–107.
- Geometria wentylatora: kopia wentylatora z układu chłodzenia bolidu.

## Kluczowe liczby — tylko z tekstu
| Iteracja | Opis (skrót) | Cx | Cz | −Cz/Cx |
|---|---|---:|---:|---:|
| iter000 | PM08 bazowa (profilowana podłoga) | 0,726 | −2,036 | 2,804 |
| iter001 | Wentylator ⊥ nawierzchni | 0,749 | −1,357 | 1,812 |
| iter002 | Kanał, wentylator ∥ nawierzchni | 0,673 | −1,296 | 1,926 |
| iter003 | Kanał + wentylator pod kątem | 0,681 | −1,301 | 1,910 |
| iter004 | iter001 + kanał wzdłuż podłogi | 0,678 | −1,359 | 2,004 |
| iter100 | Płaska podłoga | 0,696 | −1,471 | 2,114 |
| iter101 | Płaska + kurtyny | 0,692 | −1,408 | 2,035 |
| iter102 | Płaska, wentylator ⊥ | 0,699 | −1,509 | 2,159 |
| iter103 | Płaska+kurtyny, wentylator ⊥ | 0,695 | −1,422 | 2,046 |
| iter104 | iter102 + kanał wzdłuż podłogi | 0,688 | −1,523 | 2,214 |
| iter105 | iter103 + kanał wzdłuż podłogi | 0,688 | −1,55 | 2,253 |
| iter106 | Płaska, kanał, wentylator ∥ | 0,697 | −1,558 | 2,235 |
| iter107 | Płaska+kurtyny, kanał, wentylator ∥ | 0,696 | −1,589 | 2,283 |

- Na profilowanej podłodze najlepszy Cz z wentylatorem jest o **ok. 30% gorszy** od bazowego Cz = −2,036.
- Najlepszy wynik w badaniu: **iter107** (Cz = −1,589; −Cz/Cx = 2,283) — nadal słabszy niż PM08 bazowa.
- Kontekst historyczny w tekście (nie wyniki własne): McMurtry Spéirling — producent twierdzi **2 t docisku** z wentylatorów przy masie pojazdu **ok. 1 t**; AMZ Racing 0–100 km/h w **0,956 s** (2023) z aktywną aerodynamiką.
- Warunki brzegowe: V_in = **15 m/s**; ω_fan = **510 rad/s**.

## Geometria / konfiguracje
1. **Podłoga profilowana (PM08)** — kształt profilu lotniczego, zoptymalizowana z resztą pakietu; większość docisku na spodzie.
2. **Płaska podłoga** — bez zmiany przekroju kanału; usunięte boczne skrzydła na podłodze; wariant z kurtynami uszczelniającymi na krańcach.
3. **Wentylator**:
   - prostopadle do nawierzchni (otwór w podłodze);
   - w kanale kołowym równolegle do nawierzchni;
   - w kanale pod kątem;
   - + kanał wzdłuż przepływu na górnej części podłogi.
4. Inspiracja płaskiej podłogi: bolid AMZ Racing (rekord przyspieszenia).

## Wnioski dla nowego pakietu aero FS
- Proste wstawienie wentylatora w **już zoptymalizowaną** podłogę FS **psuje docisk** (zaburzenie pakietu) — nie łączyć na siłę z silnie wyprofilowanym undertrayem bez redesignu.
- Na **płaskiej** podłodze wentylator **zwiększa** |Cz|; kanały wokół wentylatora działają wyraźnie lepiej niż sam otwór z wentylatorem.
- Kurtyny boczne mają **potencjał**, ale w niektórych konfiguracjach obniżają docisk w okolicy dyfuzora — wymaga osobnej optymalizacji.
- Za wlotem wentylatora ciśnienie ≈ otoczenia → obszar „martwy” dla docisku; warto przesunąć wentylator **bardziej do tyłu**.
- Obecne wyniki **nie uzasadniają** wdrożenia na PM08; dalsze badania: lokalizacja/geometria wentylatora, RPM, kanały, geometria podłogi, V = 0 (docisk stacjonarny).
- Aktywna aero / fan nie jest zabroniona w FS (wg autora), ale osobne zmiany konstrukcyjne mogą wykluczyć bolid z zawodów.

## Ograniczenia
- Tylko CFD steady + MRF; brak walidacji torowej/tunelowej własnych wyników.
- Mała liczba konfiguracji względem przestrzeni projektowej; wentylator = kopia z chłodzenia (nie dedykowany aero).
- Half-car + symmetry; y+ w szerokim zakresie 30–300.
- Brak badań mocy napędu wentylatora, masy, awaryjności, bezpieczeństwa (piasek/kamienie — historycznie problem Chaparral 2J).
- Żadna iteracja nie pobiła bazowego Cz PM08; wnioski o „niemożliwości” na aktualnej geometrii są hipotezą z ograniczonej serii.

## Claims (claim | evidence | confidence)
| claim | evidence | confidence |
|---|---|---|
| Wentylator na profilowanej podłodze PM08 obniża \|Cz\| o ~30%+ vs baza | Tabela 5.5: baza Cz=−2,036; najlepszy z wentylatorem Cz=−1,359 (iter004) | high |
| Najlepsza konfiguracja w badaniu: płaska + kurtyny + kanał + wentylator ∥ (iter107) | Tabela 5.10: Cz=−1,589, −Cz/Cx=2,283 | high |
| Sam wentylator bez kanałów daje najsłabsze efekty na płaskiej podłodze | Sekcja 5.5: „Zastosowanie samego wentylatora dało zdecydowanie najsłabsze efekty” | high |
| Za wlotem wentylatora obszar nie generuje docisku (p≈otoczenia) | Opis rozkładu Cp w 5.5 | medium |
| Obecne wyniki nie uzasadniają zastosowania wentylatora na PM08 | Podsumowanie §6 | high |
| Kurtyny mają potencjał rozwojowy, ale mogą obniżać docisk dyfuzora | 5.4.3 / 5.5 | medium |
| MRF + steady + realizable k-ε + V=15 m/s + ω=510 rad/s | Tabela 4.2 / §4.2 | high |
