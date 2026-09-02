# Research: dźwignie balansu H1–H5 (Spec)

**Status:** notatka robocza dla Spec (2026-09-01)  
**Język:** PL  
**Zasada:** wyłącznie KB w `sources/` (Staniszewski 2023/2024, Nagłowski 2024, Jackson 2018, Michalecki, T8/rules, research-balance-shift, research-fs-teams-practice, team-rwiter017 / Baseline002 kontekst). **Bez liczb spoza źródeł.**

**Kotwica** (`RW_iter017` @ **15 m/s**, zamrożone):

- Cx = **1,229**
- Cz = **−3,682**
- Cm = **−0,429**
- balans ≈ **61,6%** przód (z Cm/Cz)

**Cel:** maksymalny docisk, spokojny opór (Cx ≲ **1,23**), balans **48–52%** przód (ok. **12 pp** cofnięcia).

**Eventy:** Endurance + Autocross.

**Zamrożone:** DRS ruchomy **OUT**; fan **OUT**; wąsy **TBD**; rozważamy RW **4-el.** jako hipotezę CAD (w literaturze KB = **3** el.).

Powiązane: [research-balance-shift.md](research-balance-shift.md), [research-fs-teams-practice.md](research-fs-teams-practice.md), [fs-rules-2026-t8.md](fs-rules-2026-t8.md), [team-rwiter017-baseline.md](team-rwiter017-baseline.md).

Metryka CFD (Fluent / później OF): moment przy **x = 0,765 m**, Lref **1,53 m**, half-car, V=**15 m/s**. Guardrale sukcesu serii: **|Cz| ≥ 3,682**, **Cx ≲ 1,23**, Δbalans w stronę 50/50.

**Kolejność:** H1 → H2 → (H3 gdy trzeba) → H4 jeśli TBD=IN. **H5 = OUT** (nie ścieżka peak-DF).

---

## H1 — Więcej docisku z tylnego skrzydła (RW)

### Mechanizm

Chodzi o to, żeby **więcej docisku poszło z tyłu**: ustawiamy kąty / overlap / gap wieloelementowego RW w stronę optimum 2D ze Staniszewskiego 2023 — ale **na pakiecie** 017, nie na izolowanej kaskadzie. Montaż możliwie wysoko (Jackson: uniknąć disturbed flow za HR / roll hoop).

Opcjonalna pod-hipoteza CAD: **4 elementy** zamiast 3 (więcej powierzchni/slotów w envelope T8) — **bez** liczb ΔCz w ekstraktach.

### Oczekiwany kierunek (balans / DF / drag)

| Wielkość | Kierunek |
|----------|----------|
| Balans przód | **↓** (więcej tyłu → mniej % przodu) |
| \|Cz\| | **↑ lub =** (cel: nie poniżej 3,682) |
| Cx | **↑ ryzyko** — pilnować ≲ 1,23 |

### Evidence + confidence

| claim | evidence | confidence |
|-------|----------|------------|
| Obniżenie kąta main + overlap ~−30 mm podnosi \|Fz\| 2D izolowanego RW (~398→~560–565 N) | Staniszewski 2023 Tab. 3/4 | **high** (2D) |
| Na pojeździe 3D Cx/Cz prawie stoją; coupling z body — nie wklejać 2D 1:1 | Staniszewski 2023 s. 32 + Wnioski | **high** (ostrzeżenie); efekt na 017 = **TBD** |
| RW closed = skok DF (Jackson CL_DF 1,15 / CD 1,21) | Jackson Results | **high** (kierunek); transfer V/A **low** |
| U Nagłowskiego RW ≈ **24%** Fz_all | Tab. 5.3 | **high** (ich auto); udział na 017 **TBD** |
| 4-el. RW: brak liczb w KB (Jackson/Staniszewski = 3 el.) | ekstrakty | **high** (brak danych); efekt = **hipoteza** |

### Ryzyka (T8, yaw)

- **T8:** RW >500 mm → wysokość **<1,1 m**; max **250 mm** za tylnymi oponami; nie outboard od most inboard tylnej opony (T 8.2.1–3); sztywność T 8.3; envelope przy any suspension (T 8.2.4).
- **4-el.:** więcej cięciwy/slotów łatwo wychodzi poza LE/TE limity i box szerokości endplate.
- **Yaw** (kąt jak w zakręcie): FW/RW „płaskie” vs δ względem UT (Staniszewski 2024) — H1 mniej yaw-wrażliwe niż H2, ale coupling body nadal.
- Stall / zbyt agresywne AOA (Jackson: stall ~25°; ich overall ~22,8°) — nie pchać „dla liczb”.

### Pierwszy eksperyment CFD

Na pakiecie **RWiter017** (nie izolowane 2D): seria 3–5 wariantów kątów/overlap/gap w stronę optimum Staniszewskiego (−main, overlap ~−30 mm jako orientacja, nie target). Mierzyć: Cx, Cz, Cm, **balans %** @ x=0,765 m. Guardrale: |Cz|≥3,682, Cx≲1,23.

**Osobno (później):** CAD 4-el. w T8 envelope → 1 case porównawczy vs 3-el. (bez obietnicy Δ z literatury).

### Kill criteria

- Δbalans **< ~2 pp** przy spełnionych guardralach **lub**
- Cx **> 1,23** przy |Cz| nielepzym od 3,682 **lub**
- stall / rozdział widoczny w Cp (jakościowo) bez zysku Fz tyłu **lub**
- 4-el.: nie mieści się w T8 / T 8.3 bez utraty |Cz| vs 3-el. → porzuć 4-el., zostań przy 3-el. + iteracja kątów.

---

## H2 — Mocniejszy / bardziej „tylny” dyfuzor–UT

### Mechanizm

Przyrost docisku z **podłogi / dyfuzora / uszczelnienia tyłu** — bez obniżania nosa FW. U Nagłowskiego UT ≈ **36%** Fz — duży kawałek, często tylny. Staniszewski 2024: pełny pakiet z UT&SW ma wyższe |Cz| dla każdego δ vs samo FW&RW; po modelu toru proxy energii **−2,7%** mimo **+~10 kg**.

### Oczekiwany kierunek (balans / DF / drag)

| Wielkość | Kierunek |
|----------|----------|
| Balans przód | **↓** (więcej Fz z tyłu UT) |
| \|Cz\| | **↑** (kierunek lit.) |
| Cx | **niejednoznaczny** — przy δ=0 często OK; przy 10–20° Cx pełnego pakietu bywa **wyższy** (Staniszewski 2024) |

### Evidence + confidence

| claim | evidence | confidence |
|-------|----------|------------|
| UT ≈36% Fz_all u Nagłowskiego (Fz_ut ≈−202 N / −561 N) | Tab. 5.3 | **high** (ich auto); na 017 **TBD** |
| Pełny pakiet wyższe \|Cz\| dla każdego δ vs FW&RW | Staniszewski 2024 s. 54–55 | **high** (kierunek) |
| UT&SW yaw-sensitive; FW/RW mniej | Staniszewski 2024 s. 55–56 | **high** |
| Proxy energii −2,7% mimo +~10 kg (jeden tor) | s. 67–68 | **high** (F_ham); **med** (Wh) |

### Ryzyka (T8, yaw)

- **T8 / T2:** GC static ≥ **30 mm** (T 2.2.1); zakaz sliding skirts / kontaktu z torem (T 2.2.2); UT w boxie opon (T 8.2.2 <500 mm); envelope any setup (T 8.2.4). Niski UT = **wysokie** ryzyko Tech/dynamic rake.
- **Yaw (krytyczne przy Autocross+Endurance):** utrata Fz_UT przy δ≠0; Cx(δ) przecina się ~10° — **nie** zamrażać UT na samym δ=0.
- Masa (~+10 kg w szacunku Staniszewskiego) vs zwrot energii — wymaga modelu toru.

### Pierwszy eksperyment CFD

1 case: wzmocniony dyfuzor / uszczelnienie tyłu na bazie 017 (bez zmiany nosa FW). δ=**0°**: Cx, Cz, Cm, balans %. **Gate przed zamrożeniem:** mini-mapa Cx,Cz vs δ (przynajmniej 0° / ~5–10° / ~15°) + nota vs udziały toru (metoda Staniszewski 2024). GC w CAD ≥30 mm z marginesem.

### Kill criteria

- Przy δ=0: brak Δbalans ≥~2 pp **i** brak wzrostu |Cz| przy Cx≲1,23 **lub**
- Mapa δ: średni ważony |Cz| / F_ham **gorszy** niż baza na modelu toru Endurance **lub**
- GC / T 2.2.2 nie do utrzymania w any setup **lub**
- +kg bez zwrotu proxy energii → OUT geometrii / redukcja masy UT.

---

## H3 — Lekkie odciążenie przodu (FW w dół)

### Mechanizm

Zmniejszenie kąta / elementów FW (lub lokalne odciążenie), żeby zejść z front-bias — **tylko jeśli H1–H2 nie domykają ~12 pp**. Nie dokręcać FW „dla docisku” (pcha jeszcze bardziej na przód). U Nagłowskiego FW ≈ **39%** Fz — duża dźwignia w obie strony.

### Oczekiwany kierunek (balans / DF / drag)

| Wielkość | Kierunek |
|----------|----------|
| Balans przód | **↓** |
| \|Cz\| | **↓ ryzyko** (łatwo stracić peak DF) |
| Cx | **↓ lub ≈** (mniej AOA FW) |

### Evidence + confidence

| claim | evidence | confidence |
|-------|----------|------------|
| Nie dokręcać samego FW jako pierwszej dźwigni cofania balansu | research-balance-shift; fizyka pakietu; Spec | **high** (kierunek) |
| FW ≈39% Fz u Nagłowskiego | Tab. 5.3 | **high** (ich auto) |
| FW box: <500 mm przed HR; <250 mm outboard przed osią; max 700 mm przed oponami | T 8.2.1–3 | **high** |

### Ryzyka (T8, yaw)

- **T8:** FW wysokość/outboard (T 8.2.1); keep-out kół (T 2.1.3); IA / attachment za AIP przy długim nosie (T 3.20).
- **Yaw:** FW mniej wrażliwe niż UT (Staniszewski 2024) — odciążenie FW jest „bezpieczniejsze” yawowo niż agresywny UT, ale kosztuje |Cz|.
- Utrata |Cz| poniżej 3,682 = fail celu Spec.

### Pierwszy eksperyment CFD

**Dopiero po** tabeli H1 (±H2). 1–2 warianty: −Δα FW / mniej agresywny element tylny FW na pakiecie po H1/H2. Guardrail twardy: |Cz| ≥ 3,682; cel balans 48–52%.

### Kill criteria

- |Cz| **< 3,682** przy jakimkolwiek kroku odciążenia **lub**
- Δbalans nieosiągalne bez łamania guardrala DF → wróć do H1/H2 (więcej tyłu), nie pogłębiaj H3 **lub**
- H1+H2 już w 48–52% → **nie uruchamiać** H3.

---

## H4 — Wąsy (profil TBD; lit. Selig S1223)

### Mechanizm

Generatory wirów / wąsy wpływają na przepływ wokół FW/RW/UT: u Nagłowskiego cofają balans o kilka pp (60,3%→**57,3%** best), wspierają RW/UT, same bywają **nośne** (Fz_whiskers > 0). Blisko FW kradną powietrze spod przedniego skrzydła. **U nas TBD** — nie automatycznie S1223; dobór profilu pod lokalizację.

### Oczekiwany kierunek (balans / DF / drag)

| Wielkość | Kierunek |
|----------|----------|
| Balans przód | **↓** kilka pp (Nagłowski) |
| \|Cz\| | **↑ lekko** lub ≈ (iter111.4: −4,071→−4,100) |
| Cx / L/D | **lekko gorzej** (efektywność −2,802→−2,770) |

### Evidence + confidence

| claim | evidence | confidence |
|-------|----------|------------|
| Best wąsy: balans 57,3%, Cx 1,480, Cz −4,100 | Nagłowski Tab. 5.2 iter111.4 | **high** (ich auto) |
| Fz_whiskers > 0 (+5…+13 N) | Tab. 5.3 | **high** |
| Wspierają RW/UT, psują FW gdy blisko | s. 35 + Podsumowanie | **high** / interpretacja **med** |
| Transfer na 017 + inny profil | brak w KB | **low–med** |

### Ryzyka (T8, yaw)

- **T8 / T2.1.3:** wheel keep-out — **wysokie** ryzyko Scrutineering przy agresywnych wąsach (rules-aero-boxes-loopholes).
- Envelope <500 mm / szerokość opon; promienie krawędzi T 2.4.1.
- Yaw: brak mapy δ dla wąsów w KB — nieznana wrażliwość.
- Decyzja Spec = **TBD** — nie blokować H1/H2.

### Pierwszy eksperyment CFD

**Tylko jeśli** po H1–H3 nadal >~52% przód **i** Spec = IN. 1 lokalizacja + 1 profil (dobrany pod keep-out), porównanie vs baza po H1/H2: Δbalans, ΔCx, ΔCz, Fz komponentów. Nie kopiować ślepo S1223 / iter111.4.

### Kill criteria

- Spec zostaje **OUT** / TBD bez IN → nie CFD **lub**
- Δbalans <~2 pp przy koszcie L/D / Cx **lub**
- naruszenie T 2.1.3 / T 8.2 w any setup **lub**
- Fz_whiskers nośna bez netto zysku pakietu → OUT.

---

## H5 — Ruchomy DRS — **OUT** (ścieżka peak-DF zamknięta)

### Mechanizm

Regulowane elementy RW: closed = high DF + high drag; open = niski drag i **niższy** DF (Jackson). Własne pasywne `RW_iter019/020` na bazie 017: Cx↓ do ~**0,83**, |Cz|↓ do ~**3,01** — poniżej kotwicy 3,68. **Nie** narzędzie do trzymania peak DF ani do cofania front-bias przy high-DF.

### Oczekiwany kierunek (gdyby IN — tylko kontekst)

| Wielkość | Closed → Open |
|----------|----------------|
| Balans | nie rozwiązuje „za dużo z przodu przy high-DF” |
| \|Cz\| | **↓** (Jackson; 019/020) |
| Cx | **↓** (Jackson −35% siły oporu; 019/020 Cx~0,83) |

### Evidence + confidence

| claim | evidence | confidence |
|-------|----------|------------|
| Jackson closed CL_DF=1,15/CD=1,21; open 0,26/0,79 | Results | **high** |
| Pasywne 019/020: Cx~0,83, \|Cz\|~3,01 < 3,68 | research-balance-shift / CSV RW | **high** |
| DRS ruchomy **OUT** (Spec 2026-09-01); fan OUT (Michalecki) | INDEX / TARGETS | **high** (decyzja) |
| T8 cisza o movable aero — legalność ≠ decyzja Spec | fs-rules-2026-t8 | **high** (cisza); decyzja = Spec |

### Ryzyka (T8, yaw)

- Gdyby wrócić: T 2.2.2, T 8.2.4 (cały zakres ruchu w boxie), T 8.3 obu pozycji, T 9 CGS; Q&A/Scrutineering **M**.
- Priorytet Endurance+Autocross bez Accel-as-P1 → zysk prostych DRS mniej krytyczny niż peak DF + balans.
- Fan (pokrewny powered aero): Michalecki — na profilowanej podłodze |Cz| ~30%+ gorzej; decyzja OUT.

### Pierwszy eksperyment CFD

**Brak** w ścieżce Spec peak-DF. Ewentualna gałąź **pasywnego** low-AOA RW tylko jako osobny trade oporu (nie H5 ruchomy) — poza shortlistą balansu 12 pp.

### Kill criteria

- **Już zabite decyzją Spec (DRS ruchomy OUT).**
- Wznowienie tylko po jawnej zmianie Spec + Q&A; nawet wtedy: open |Cz| < 3,682 → nie jako narzędzie peak-DF / balans high-DF.

---

## Macierz skrótowa (dla Spec)

| # | Status | Pierwsza dźwignia? | Główne kill |
|---|--------|--------------------|-------------|
| **H1** RW | **IN — start** | tak | Cx>1,23 / brak Δbalans / stall; 4-el. poza T8 |
| **H2** UT | **IN — po/z gate yaw** | tak (2.) | gorszy F_ham na torze / GC / brak Δ |
| **H3** FW↓ | warunkowo | nie | \|Cz\|<3,682 |
| **H4** wąsy | **TBD** | nie | keep-out / brak Δ / Spec OUT |
| **H5** DRS | **OUT** | — | decyzja Spec |

**Fan:** OUT (Michalecki) — poza H1–H5; nie reanimować w tej shortliście.

---

## Claims zbiorcze

| claim | evidence | confidence |
|-------|----------|------------|
| Gap 017 ≈ **12 pp** (61,6%→50%) | Cm/Cz + INDEX | **high** (roboczo) |
| Kolejność H1→H2→H3→H4; H5 OUT | research-balance-shift + Spec | **high** |
| 4-el. RW = hipoteza CAD bez liczb w KB | Jackson/Staniszewski = 3 el. | **high** (brak danych) |
| Przy Endurance+Autocross mapa δ = gate UT | Staniszewski 2024 | **high** (proces) |
