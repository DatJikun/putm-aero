# Research: praktyka pakietów FS (literatura) — Cl/Cd, udział FW/RW/UT, Endurance vs Autocross

**Status:** notatka robocza do Spec (2026-09-01)  
**Język:** PL  
**Zasada:** wyłącznie liczby i wnioski z ekstraktów w `sources/` (Jackson, Nagłowski, Staniszewski 2023/2024) + zamrożona kotwica zespołu. **Bez inventowanych widełek „typowe FS” spoza źródeł.**

**Kotwica zespołu (nie literatura):** `RW_iter017` — Cx **1,229** / Cz **−3,682** / Cm **−0,429** → balans ≈ **61,6%** przód; cel ≈ **50/50** (48–52%); \|Cz\| ≥ **3,682**, Cx ≲ **1,23** @ **15 m/s**.

**Zakres zamrożony (kontekst Spec):** DRS **OUT** (tylko pasywne warianty w arkuszach — nie ścieżka peak-DF); fan **OUT**; wąsy **TBD**; priorytet eventów **Endurance + Autocross**; rozważyć RW **4-elementowe** (w źródłach: Jackson / Staniszewski = **3** elementy — brak liczb 4-el.); envelope **FS Rules 2026 v1.1 T8**.

Powiązane: [research-balance-shift.md](research-balance-shift.md) (H1–H5), [fs-rules-2026-t8.md](fs-rules-2026-t8.md).

---

## 1. Zakresy Cl/Cd (Cx/Cz) i balansu — tylko z literatury w repo

> Konwencje: prace PUT używają **Cx, Cz** (Cz ujemny = docisk). Jackson używa **CL, CD** (przy RW: CL dodatni = downforce w tabeli high-DF). **Nie mieszać modeli** (różne A_ref, V, geometrie).

### 1.1 Jackson 2018 (Huddersfield; CFD CFX; inlet **26,8 m/s**)

| Konfiguracja | CL | CD | Uwagi |
|---|---:|---:|---|
| Baseline bez aero | **+0,21** (lift) | **0,71** | Abstract / Results |
| Pojazd + RW, DRS closed | **1,15** (DF) | **1,21** | A = 1,18 m² |
| Pojazd + RW, DRS open | **0,26** (DF) | **0,79** | A = 0,99 m²; −35% siły oporu vs closed |

RW: **3** elementy, profil **E423**, overall AOA **22,81°** (flaps 28°/60°) przed stall ~25°. Balance z FW w pracy **pominięty**.

**Pewność liczb:** **high** (tabele Jackson). **Przeniesienie na RWiter017:** **low** (inna V, A, pakiet; DRS u nas OUT).

### 1.2 Nagłowski 2024 (PUT; Fluent; **15 m/s**)

| iter | Cx | Cz | Balans przód [%] | Cz/Cx |
|---|---:|---:|---:|---:|
| iter000 (baseline) | **1,453** | **−4,071** | **60,3** | −2,802 |
| iter111.4 (best wąsy) | **1,480** | **−4,100** | **57,3** | −2,770 |

Siły baseline @15 m/s: Fz_all **−561 N**, Fx **≈200 N** (Tab. 5.3).

**Pewność:** **high** na ich modelu. **Nie** jest hard targetem PUT 2026 (INDEX: kotwica literaturowa).

### 1.3 Staniszewski 2023 (PUT; RW 3-el.; pojazd 3D @ **15 m/s**)

| Kontekst | Cx | Cz | d=Cz/Cx |
|---|---:|---:|---:|
| 3D cały pojazd, iter000 | **0,726** | **−2,036** | **−2,804** |
| iter002 (skrócony 1. profil) | 0,721 | −2,034 | −2,821 |

2D izolowane RW (nie cały auto): Fz od ≈ **−398 N** (baseline MP 7,5°) do ≈ **−560…−565 N** (overlap −30 mm / gap fine-tune) — **nie** target całego bolidu.

**Pewność:** **high** dla ich pakietu; **low** jako „typowe FS dziś” vs Nagłowski / RWiter017 (wyraźnie inny rząd \|Cz\|).

### 1.4 Zestawienie orientacyjne (czytelność — nie uśredniać)

| Źródło | V | \|Cz\| lub CL_DF | Cx/CD | Balans przód |
|--------|---|-----------------|-------|--------------|
| Jackson + RW closed | 26,8 m/s | CL≈1,15 | CD≈1,21 | n/d |
| Staniszewski 2023 pojazd | 15 m/s | \|Cz\|≈2,03 | Cx≈0,72 | n/d w tej pracy |
| Nagłowski baseline | 15 m/s | \|Cz\|≈4,07 | Cx≈1,45 | **~60%** |
| **RWiter017 (zespół)** | 15 m/s (kontekst PUT) | \|Cz\|≈**3,68** | Cx≈**1,23** | ≈**61,6%** (Cm/Cz) |

**Claim:** w źródłach PUT wysokiego DF (Nagłowski, RWiter017) balans jest **front-biased ~57–62%** przód; Jackson nie podaje balansu. | evidence: Tab. Nagłowski + INDEX/017 | **high** (kierunek w tych modelach); **nie** generalizacja „wszystkie FS”.

---

## 2. Udział FW / RW / UT i jak cofać balans

### 2.1 Udział Fz — tylko Nagłowski Tab. 5.3 (baseline iter000)

Przy Fz_all = **−561 N**:

| Komponent | Fz [N] | Udział \|Fz\| / \|Fz_all\| |
|-----------|-------:|--------------------------:|
| FW | **−221,05** | ≈ **39%** |
| UT | **−201,88** | ≈ **36%** |
| RW | **−135,21** | ≈ **24%** |
| (suma FW+RW+UT) | −558,14 | ≈99% (reszta: body / side wing / numeryka) |

Podział osi: Fz przód **−338** / tył **−223** → balans **60,3%** przód (zgodnie z Tab. 5.2).

**Pewność udziałów:** **high** dla modelu Nagłowskiego. **Transfer na 017:** **low–med** (inny pakiet; te same *kierunki* dźwigni).

Jackson optymalizował głównie RW; FW/sidepods/dyfuzor wspomniane, bez tabeli udziałów. Staniszewski 2023 = fokus RW; Staniszewski 2024 porównuje **pełny pakiet (FW+RW+UT&SW)** vs **FW&RW** — bez rozbicia % Fz komponentów w plain text.

### 2.2 Mechanizmy cofania balansu (z literatury + shortlista H)

| Mechanizm | Co robi | Dowód w źródłach | Confidence |
|-----------|---------|------------------|------------|
| **Więcej docisku RW** (kąty / overlap / gap; montaż wysoko) | Zwiększa udział tyłu | Staniszewski 2023: 2D \|Fz\|↑ przy obniżeniu main i overlap ~−30 mm; Jackson: RW closed = skok DF | **high** kierunek; **med** na pojeździe (coupling body) |
| **UT / dyfuzor „tylniejszy”** | Duży kawałek Fz (u Nagłowskiego ~36%); często tylny | Nagłowski Fz_ut; Staniszewski 2024: pełny pakiet wyższe \|Cz\| vs FW&RW dla każdego δ | **high** kierunek |
| **Wąsy S1223** (TBD u nas) | Cofają balans o kilka pp; wspierają RW/UT; same bywają nośne | Nagłowski: 60,3% → **57,3%**; Fz_whiskers > 0 | **high** na ich aucie; **low–med** transfer |
| **Nie dokręcać samego FW** | Pcha jeszcze bardziej na przód | Fizyka pakietu; research-balance-shift | **high** (kierunek) |
| **DRS open** | Obniża DF i drag — nie narzędzie peak-DF / balans high-DF | Jackson closed→open; u nas DRS **OUT** | **high** (Jackson); decyzja OUT = Spec |

**Gap do 50/50 na 017:** ≈ **12 pp** (61,6% → 50%) — patrz [research-balance-shift.md](research-balance-shift.md).

---

## 3. Endurance vs Autocross — trade-offy aero (yaw / UT)

**Priorytet Spec:** Endurance + Autocross (nie Accel jako P1; DRS OUT → brak „otwartego” low-drag na prostych jak u Jacksona).

### 3.1 Staniszewski 2024 — wrażliwość UT na kąt napływu

- Pełny pakiet (z **UT&SW**) ma **wyższe \|Cz\| dla każdego** badanego δśrd vs samo FW&RW | s. 54–55 | **high** (kierunek).
- **Cx(δ):** pełny pakiet **niższy** Cx dla **0°–10°**, **wyższy** dla **10°–20°** vs FW&RW (krzywe się przecinają) | s. 54 | **high**.
- **UT&SW silnie wrażliwe** na kierunek napływu (nominal ~0°); przy δ≠0 istotny spadek sił z podłogi; **FW/RW „płaskie”** vs δ | s. 55–56 | **high**.
- Po zważeniu modelu toru: pełny pakiet → średnia siła hamująca **F2/F1 = 0,973** → **−2,7%** vs bez podłogi, mimo **+~10 kg** | s. 67–68 | **high** jako proxy F_ham; **med** jako Wh baterii.
- Wniosek metodologiczny: **nie ekstrapolować** charakterystyki zakrętu z samego δ=0 | Podsumowanie | **med–high**.

Punkty kinematyki Tab. 9 (przykłady): r≈17,55 m → v≈13,77 m/s; …; r≈4,39 m → v≈6,54 m/s.

### 3.2 Implikacje eventowe (interpretacja pod Spec — pewność med)

| Event | Co wynika ze źródeł | Czego unikać |
|-------|---------------------|--------------|
| **Autocross** (dużo zakrętów, zmienne δ) | Docisk w zakresie δ ważniejszy niż sam peak @0°; UT pomaga \|Cz\|, ale **traci** przy yaw — FW/RW stabilniejsze | Optymalizacja UT tylko pod δ=0 bez mapy Cx/Cz(δ) |
| **Endurance** (energia + powtarzalność) | Staniszewski: UT może **obniżyć** proxy energii mimo masy; trzeba **modelu toru** (udziały r) | Przenoszenie −2,7% na inny tor bez przeliczenia; DRS jako „ratunek energii” przy decyzji OUT |
| **Accel / proste** (niższy priorytet tu) | Jackson: DRS open −35% drag — **niedostępne** jako ścieżka aktywna; pasywny low-AOA RW = trade \|Cz\| | Pogarszanie Cx 017 bez zwrotu w lap/energii |

**Claim:** przy priorytecie Endurance+Autocross gate projektowy UT = **mapa vs δ + model toru**, nie sam Cx/Cz@δ=0 | Staniszewski 2024 + ASSUMPTIONS | **high** (metoda); wielkość zysku na *naszym* 017 = **do zmierzenia**.

---

## 4. Implikacje dla shortlisty H1 (RW) → H2 (UT)

Z [research-balance-shift.md](research-balance-shift.md) + powyższej literatury:

### H1 — RW (pierwsza dźwignia ~12 pp)

1. Szukać **więcej docisku z tyłu** na **pakiecie** 017 (kąty / overlap / gap w stronę optimum 2D Staniszewskiego), guardrale: \|Cz\| ≥ 3,682, Cx ≲ 1,23, balans % przy x=0,765 m.
2. **Nie** wklejać optimum 2D 1:1 (coupling z body / elementem bocznym — Staniszewski 2023).
3. **4-elementowe RW:** w Jackson i Staniszewski 2023 jest **3** elementy; **brak** liczb 4-el. w ekstraktach → traktować jako **hipotezę CAD** (więcej powierzchni / slotów w envelope T8: wysokość &lt;1,1 m, max 250 mm za oponami, RW &gt;500 mm nie outboard most inboard tylnej opony) — **bez** obietnicy ΔCz z literatury.
4. DRS / passive flaps: **poza** ścieżką peak-DF (OUT; Jackson open obniża DF).

**Pewność kierunku H1:** **high**; wielkość pp na 017: **TBD CFD**.

### H2 — UT (druga dźwignia, po / równolegle z gate yaw)

1. Przyrost docisku **dyfuzora / uszczelnienia tyłu** (bez dokręcania nosa FW); GC ≥ **30 mm** (T 2.2.1); zakaz sliding skirts (T 2.2.2).
2. Przed zamrożeniem geometrii: **Cx,Cz vs δ** + udziały toru (jak Staniszewski 2024) — krytyczne przy Endurance+Autocross.
3. Pilnować masy (~+10 kg w szacunku Staniszewskiego) vs proxy energii.
4. U Nagłowskiego UT ≈ **36%** Fz — duży dźwigniowy kawałek; u nas udział **do zmierzenia** na 017.

**Pewność kierunku H2:** **high** w literaturze PUT; krok na 017: **TBD**.

### Po H1→H2

- **H3** (odciążenie FW) tylko jeśli nadal &gt;~52% przód i \|Cz\| trzyma się.
- **H4** wąsy: TBD (Nagłowski: kilka pp, koszt L/D).
- **H5** DRS: OUT ze ścieżki Spec.

**Kolejność rekomendowana pod Spec:** **H1 → H2** (z gate yaw na UT) → H3 opcjonalnie → H4 jeśli TBD=IN.

---

## 5. Claims (claim | evidence | confidence)

| claim | evidence | confidence |
|-------|----------|------------|
| W źródłach PUT wysokiego DF balans ~57–62% przód (Nagłowski 60,3→57,3%; 017 ≈61,6%) | Nagłowski Tab. 5.2; INDEX/Cm/Cz 017 | **high** (te modele) |
| U Nagłowskiego udział Fz: FW≈39%, UT≈36%, RW≈24% @ baseline | Tab. 5.3 | **high** (ich auto) |
| Jackson: RW closed CL_DF=1,15 / CD=1,21; open 0,26 / 0,79 | Results Jackson | **high** |
| Staniszewski 2023 pojazd: Cx≈0,72 / Cz≈−2,03 — inny rząd niż Nagłowski/017 | tabela s. 32 | **high** |
| UT&SW yaw-sensitive; FW/RW mniej; pełny pakiet −2,7% F_ham mimo +~10 kg | Staniszewski 2024 s. 54–68 | **high** (proxy); **med** (Wh) |
| Główne dźwignie cofania balansu = RW + UT, nie samo FW | research-balance-shift + §2 | **high** (kierunek) |
| Przy Endurance+Autocross mapa Cx/Cz(δ) jest gate’em UT | Staniszewski 2024 metoda | **high** (proces) |
| 4-el. RW: brak liczb w ekstraktach — tylko hipoteza w T8 envelope | Jackson/Staniszewski = 3 el.; T8 | **high** (brak danych); efekt = **TBD** |
| DRS OUT / fan OUT zgodne z zamrożeniem; DRS nie rozwiązuje front-bias high-DF | kontekst Spec; Jackson open ↓DF; Michalecki fan | **high** |

---

## 6. Limity (czego nie wnioskować)

- Nie uśredniać Jackson (26,8 m/s, CL~1) z Nagłowskim (Cz~−4) w jeden „typowy FS Cl/Cd”.
- Nie brać Fz 2D izolowanego RW jako Fz auta.
- Nie przenosić −2,7% energii na inny tor bez modelu udziałów r.
- Nie obiecywać Δ pp z 4-el. RW bez CFD na pakiecie 017.
- Envelope T8 ogranicza geometrię — nie jest źródłem liczb Cl/Cd.
