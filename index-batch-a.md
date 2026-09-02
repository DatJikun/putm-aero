# FS Aero KB — index batch A

Trzy ekstrakty wiedzy z prac dyplomowych PUT Motorsport (Formula Student), stan: 2026-09-01.

## Źródła

1. **[staniszewski-2023-wing.md](sources/staniszewski-2023-wing.md)** — Alex Staniszewski, inżynierska 2023, tylne skrzydło wieloprofilowe.
   CFD 2D/3D (Fluent, Realizable k-ε, 15 m/s) optymalizuje kąty, overlap i gap trzech elementów RW oraz adresuje nierównomierny Cp w środku rozpiętości.
   Najlepsze 2D podnoszą |Fz| z ok. **398 N** do ok. **560–565 N** na izolowanym skrzydle.
   Na pojeździe Cx/Cz (ok. **0,72** / **−2,03**) zmieniają się tylko marginalnie.

2. **[staniszewski-2024-energy.md](sources/staniszewski-2024-energy.md)** — Alex Staniszewski, magisterska 2024, wpływ aero na zużycie energii EV FS.
   Mapy Cx/Cz vs kąt skrętu + model toru pokazują, że podłoga jest wrażliwa na δ≠0.
   Pełny pakiet vs FW&RW daje ok. **2,7%** niższą średnią siłę hamującą (proxy energii) mimo ok. **+10 kg** masy UT.

3. **[naglowski-2024-package.md](sources/naglowski-2024-package.md)** — Kacper Nagłowski, inżynierska 2024, modyfikacje pakietu (wąsy Selig S1223).
   Seria CFD @15 m/s: baseline Cz = **−4,071** / Fz = **−561 N**.
   Najlepsza iter111.4 osiąga Fz = **−565 N** przy Cx = **1,480** i balansie ok. **57%** przód.
   Wąsy zwiększają docisk auta mimo własnej nośnej i cofają balans, chroniąc RW / wspierając UT.

## Ścieżki plików (w tym repo)

- `sources/staniszewski-2023-wing.md`
- `sources/staniszewski-2024-energy.md`
- `sources/naglowski-2024-package.md`
- `index-batch-a.md`
