# Analiza wpływu elementów aerodynamicznych pojazdu elektrycznego klasy Formuła Student na zużycie energii podczas przejazdu na torze / Alex Staniszewski / 2024 / praca magisterska

**Uczelnia:** Politechnika Poznańska, Wydział Inżynierii Środowiska i Energetyki  
**Promotor:** dr inż. Przemysław Grzymisławski  
**Data:** Poznań, 30.10.2024  
**Źródło PDF:** załącznik (74 strony); ekstrakcja `pdftotext -layout`

## Cel pracy

Sporządzenie charakterystyki aero bolidu EV FS **w zakręcie** (nie tylko na wprost), porównanie **pełnego pakietu** z konfiguracją **FW+RW** (bez podłogi/sekcji bocznych), zbudowanie **matematycznego modelu toru** i oszacowanie zmiany **konsumpcji energii** przez wskaźnik średniej ważonej **siły hamującej** (opór aero + opór toczny), przy założeniu proporcjonalności energii do tej siły.

## Metody (CAD/CFD/eksperyment)

- **CFD 3D** (Ansys Fluent) serii punktów przy różnych **średnich kątach skrętu δśrd** / promieniach zakrętu; odbicie lustrzane względem Y (symetria geometrii).
- CAD: **SolidWorks** (geometria pakietu); domena: **SpaceClaim**; siatka: Fluent Meshing.
- Turbulencja: **k-ε realizable** (wspomniane w ustawieniach / bibliografii Fluent k-ε).
- Kinematyka: parametryczny model koła, **Anty-Ackerman**, uśredniony kąt skrętu δśrd, promień skrętu r, prędkość liniowa v i kątowa z danych torowych / μ(r).
- Post-process: charakterystyki Cx(δ), Cz(δ); rozkład Cp; model toru (udziały prostych i łuków vs r); interpolacja Cx, Cz, A vs średni r przedziału; wskaźnik F(v) = Fx(v) + Crr·(mg + Fz(v)).
- Porównanie konfiguracji: **pełny pakiet** (FW + RW + UT&SW + CS) vs **FW&RW** (+ CS).
- **Brak pomiaru Wh/kWh na torze** — energia wnioskowana wyłącznie ze stosunku średnich sił hamujących.

## Kluczowe liczby (Cl, Cd, downforce, drag, balans, energia, prędkości) — TYLKO z tekstu

| Kontekst | Wielkość | Wartość | Cytat / lokalizacja |
|---|---|---|---|
| Prędkości w zakręcie (Tab. 9) | r [m] → v [m/s] → ω [rad/s] | **17,55 → 13,77 → 0,7846**; **8,77 → 9,41 → 1,0453**; **5,85 → 7,59 → 1,2974**; **4,39 → 6,54 → 1,4897** | Tab. 9 (~s. 30 numeracji pracy) |
| Masa UT (szacunek) | Δm | **~10 kg** przy dołożeniu podłogi | s. 68: „masy całego bolidu o szacowane 10kg” |
| Średnia ważona siła hamująca | F1, F2 | **F1 = 290,319**; **F2 = 282,589** (jednostki jak w arkuszu — siła [N] w sensie modelu) | wzór (20.0), s. 67 |
| Stosunek | F2/F1 | **0,973** | s. 67 |
| Zmiana „energii” (proxy) | Δ | **−2,7%** sił hamujących względem bolidu **bez** podłogi | „mniejsza o 2,7%” s. 68 |
| Zakres kątów opisu Cx | δ | pełny pakiet: niższy Cx dla **0°–10°**; wyższy Cx dla **10°–20°** vs FW&RW | s. 54 |
| Cz | jakościowo | pełny pakiet: **wyższe \|Cz\| dla każdego kąta** vs FW&RW | s. 54–55 |
| Max Cx, Cz pełnego pakietu | argument | przy **δ = 0°** (jazda na wprost) | s. 55 |

**Liczby tylko na rysunkach / w arkuszach (nie w tekście ciągłym):** konkretne Cx, Cz dla każdego δ (Rys. 42–45); A, Cx, Cz vs r (Rys. 55–57); F(v) krzywe (Rys. 60–61); udziały długości toru (Rys. 52); wartości Crr, m, ρ, S użyte w arkuszu — **nie wynotowano z OCR obrazów**. Nie podano Wh/km ani kWh/okrążenie.

## Konfiguracje i geometria (profile, kąty, liczba elementów, DRS itd.)

- Komponenty pełnego pakietu: **FW**, **RW**, **UT&SW** (podłoga + sekcje boczne), **CS** (cooling).
- Konfiguracja odniesienia porównawcza: **FW&RW** (+ CS) — bez UT&SW.
- Geometria skrętu: **Anty-Ackerman** (priorytet max v w zakręcie).
- Badane warunki: jazda na wprost + seria zakrętów o różnych r / δśrd (Tab. 9).
- Nazwy profili lotniczych, liczba elementów RW/FW, kąty ustawienia skrzydeł, **DRS:** nie są przedmiotem tej pracy (użyta „finalna konfiguracja” po fazie projektowej).

## Wnioski projektowe istotne dla NOWEGO pakietu aero

1. **Charakterystyka w zakręcie nie da się wiarygodnie ekstrapolować** z samego case’u „na wprost” — interakcje przepływu są niestabilne / nieprzewidywalne bez siatki punktów CFD vs δ.
2. **Podłoga (UT&SW) jest silnie wrażliwa na kierunek napływu**; nominalny punkt pracy ~0°; przy δ≠0 istotny spadek sił z tego komponentu, podczas gdy FW/RW są „płaskie”.
3. Pełny pakiet wygrywa **dociskiem w całym zakresie δ**; o **oporze** nie da się orzekać z samego wykresu Cx(δ) (krzywe się przecinają ~10°) — potrzebny **model toru** (udziały prostych/łuków).
4. Po zważeniu toru: pełny pakiet (z UT) daje **~2,7% niższą** średnią siłę hamującą mimo **+~10 kg** — proxy na **niższą konsumpcję energii** na tym torze.
5. Metodę (mapa Cx/Cz vs δ + model toru + F_ham) warto **włożyć na stałe do procesu projektowego** pakietu EV FS (kryterium energii Endurance).
6. Projekt UT powinien uwzględniać **utratę efektywności w zakręcie**, nie tylko peak na prostej.

## Ograniczenia / czego NIE wnioskować

- **2,7% ≠ zmierzona energia baterii** — to stosunek średnich sił hamujących przy założeniu proporcjonalności; brak walidacji Wh.
- F1/F2: w tekście stosunek &lt;1 przypisany do konfiguracji **z podłogą** względem **bez**; konkretne Cx/Cz per δ nie są w plain text.
- Jedna geometria pakietu, jeden model toru, interpolacja liniowa między punktami δ/r.
- Brak tunelu / telemetrii energii; Crr i masa w arkuszu nie przepisane z OCR.
- Nie przenosić −2,7% na inny tor bez przeliczenia udziałów r.

## Claims (bullet list: claim | evidence | confidence high/med/low)

- Pełny pakiet ma wyższy \|Cz\| niż FW&RW dla każdego δśrd | opis Rys. 43, s. 54–55 | **high** (kierunek); wartości punktowe **med/low** (tylko wykres)
- Cx(δ) pełnego pakietu i FW&RW przecinają się (~niższy Cx pełnego pakietu 0–10°, wyższy 10–20°) | s. 54 | **high**
- UT&SW traci efektywność przy δ≠0; FW/RW mniej wrażliwe | s. 55–56 + Cp | **high**
- Średnia ważona siła hamująca: 290,319 vs 282,589; stosunek 0,973 → **−2,7%** | (20.0) + s. 67–68 | **high** (jako proxy); **med** jako „energia Wh”
- Dołożenie UT (+~10 kg) i tak obniża proxy energii na modelowanym torze | s. 68 | **med**
- Bez CFD w zakręcie nie przewidzi się charakterystyki | Podsumowanie s. 69 | **med** (teza metodologiczna)
