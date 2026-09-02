# Research: ogólne rady aero pod cele Spec (PUT Motorsport / putm-aero)

**Status:** notatka robocza do Spec (2026-09-01)  
**Język:** PL

**Cel tej notatki:** zebrać **ogólne** rady aero (nie plan CAD/CFD) pod **nasze** targety i mapować je na hipotezy **H1–H4**.

**Kotwica liczbowa** (`RW_iter017`, kontekst **15 m/s**):

- Cx = **1,229**
- Cz = **−3,682**
- Cm = **−0,429**
- balans ≈ **61,6%** przód (`1/2 + Cm/Cz`)

**Hard targety:**

- |Cz| ≥ **3,682**
- Cx ≲ **1,23**
- balans **48–52%** przód (≈ **−12 pp** od 61,6%)

**Zakres zamrożony Spec:** DRS ruchomy **OUT** (pasywne klapy — osobna gałąź oporu); fan spod podłogi **OUT**; wąsy **TBD**; priorytet **Endurance + Autocross**; rozważyć RW **4-elementowe**.

**Aref** (powierzchnia odniesienia): nie inventujemy. Fluent i OpenFOAM porównujemy dopiero po Reference Values z Fluenta.

Powiązane: [research-balance-shift.md](research-balance-shift.md), [research-fs-teams-practice.md](research-fs-teams-practice.md) (jeśli w repo), [TARGETS.md](../TARGETS.md), [fs-rules-2026-t8.md](fs-rules-2026-t8.md).

---

## 0. Co optymalizujemy (słowa Spec → metryki CFD)

| Decyzja Spec | Metryka / guardrail | Źródło |
|--------------|---------------------|--------|
| Max docisk przy możliwie niskim oporze | \|Cz\| ≥ **3,682**, Cx ≲ **1,23** @ 15 m/s | TARGETS / RW_iter017 |
| Cofnąć balans ~**12 pp** (61,6% → ~50/50) | Balans Front = `1/2 + Cm/Cz` (arkusz) przy **x = 0,765 m**, Lref **1,53 m** | research-balance-shift; team-rwiter017 |
| Endurance + Autocross | Nie tylko peak @ δ=0 — mapa Cx/Cz vs δ + model toru (energia = proxy F_ham) | Staniszewski 2024 |
| Ruchomy DRS OUT; fan OUT | Nie projektować peak-DF przez open DRS ani ssanie wentylatora | Decyzja 2026-09-01; Michalecki |
| RW 4-el. do rozważenia | Więcej parametrów setupu tyłu; koszt masa/sztywność/T8.3 | Spec + Quintanas 2023 (UPC) |

**Zasada dźwigni (kolejność):** **H1 RW → H2 UT → H3 odciążenie FW tylko jeśli trzeba → H4 wąsy TBD**. Nie dokręcać samego FW „żeby dogonić docisk” — to pcha balans jeszcze bardziej na przód.

---

## 1. H1 — tylne skrzydło (główna dźwignia balansu tyłu)

### 1.1 Czego uczą źródła PUT / Jackson (3 elementy)

W źródłach lokalnych RW jest **3-elementowe**:

- **Staniszewski 2023:** izolowane 2D — obniżanie kąta main względem baseline **7,5°** podnosi |Fz| (baseline Fz ≈ **−398 N** → przy −6,5° ≈ **−502 N**); overlap ≈ **−30 mm** daje szczyt ≈ **−565 N**; **−40 mm** już pogarsza. Gap **+5/+10 mm** utrzymuje wysoki DF przy niskim Fx. Na **całym pojeździe** Cx/Cz prawie stoją (**~0,72 / −2,03**) — autor ostrzega przed **couplingiem** RW↔body / element boczno-przypodłogowy i niepewnością CFD.
- **Jackson 2018:** 3 el., E423, gap/overlap wg McBeath (**1–4%c** / **1–6%c**); AOA overall **22,81°** (flaps **28°/60°**) przed stall ~**25°**. Na pojeździe DRS closed: CL_DF **1,15**, CD **1,21**; DRS open: CL **0,26**, CD **0,79** (−**35%** siły oporu). U nas DRS ruchomy **OUT** — liczby open służą tylko jako ostrzeżenie: low-drag setup **zjada** peak |Cz|.

**Wniosek H1:** więcej docisku z tyłu przez kąty / overlap / gap / (ew. 4. element) — **zawsze na pakiecie**, nie tylko 2D. Pilnować Cx ≲ 1,23 i |Cz| ≥ 3,682.

### 1.2 3 vs 4 elementy — co da się powiedzieć bez inventowania

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Źródła PUT w KB (Staniszewski 2023, Jackson) = **3** elementy; brak lokalnych liczb „4 el. bije 3 o X%” na naszym Aref | ekstrakty KB | **high** |
| 4. element zwiększa liczbę parametrów setupu (kąty + gurney na ostatnich foils) i pozwala eksponować ostatni flap na czystsze powietrze | Quintanas / Dynamics UPC 2023: „fourth foil… increase the number of parameters”; setup pod Accel/Skid/AX/Endurance | **high** (motywacja); **med** transfer na 017 |
| Multi-element pozwala wyższe AOA bez stall przez re-energizację BL (slotted flaps) | Jackson cyt. McBeath; Quintanas § slotted flaps; NablaFlow (F1 context, jakościowo) | **high** kierunek |
| McBeath (przez Jackson): gap **1–4%c**, overlap **1–6%c**; flap1 ~**25–30°**, flap2 ~**30–70°** jako start do optymalizacji AOA | Jackson 2018 § multi-element | **high** jako start; **med** na 4-el. (więcej szczelin) |
| 4-el. kosztuje: masa, formy, sztywność T8.3, coupling z body (lekcja Staniszewski: 2D≠3D) | Quintanas: masa RW ~**7 kg** real; Staniszewski coupling; T 8.3.1–2 | **high** ryzyka |
| LUT / Metropolia 2026 (teza): DF z RW poprawia cornering mimo nieliniowego wzrostu drag — priorytet \|CL\| pod lap, nie ślepy L/D | LUTPUB abstract (HPF026) | **med** (kierunek eventowy AX/Endurance) |

**Rada Spec (H1):** traktować **4-el.** jako **hipotezę setupu i peak tyłu**, nie jako gwarantowany zysk Cx/Cz. Gate: tabela Δbalans / ΔCx / ΔCz na pakiecie 017 vs 3-el. baseline; nie przenosić optimum 2D 1:1.

### 1.3 Gurney (narzędzie fine-tune tyłu / ostatnich elementów)

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Gurney na TE zwiększa CL (efektywny camber / cyrkulacja) przy koszcie CD | ICAS 2006 (2-el.); PMC4897339; Quintanas: gurney na 3. i 4. foil w Design Manager | **high** kierunek |
| Wysokość ~**1–2%** lokalnej cięciwy: dobry L/D; **>2%** — drag rośnie ostro | PMC / numerical Gurney studies (1%c, 2%c vs 4%c) | **high** literaturowo; **med** na naszym RW |
| Montaż blisko TE (≤~10%c od TE) | PMC4897339 | **med–high** |
| U nas: gurney na **ostatnich** elementach RW = tani sposób dołożyć tył bez redesignu całego main — ale pilnować Cx ≲ 1,23 | mapowanie na H1 + guardrail Spec | **med** (hipoteza projektowa) |

---

## 2. H2 — undertray / dyfuzor (druga dźwignia + energia Endurance)

### 2.1 Udział i kierunek balansu

Z **Nagłowski 2024** (inny model niż 017 — **kierunki**, nie targety):

| Komponent | Fz @ 15 m/s | Udział ≈ |
|-----------|------------:|---------:|
| FW | **−221 N** | ~**39%** |
| UT | **−202 N** | ~**36%** |
| RW | **−135 N** | ~**24%** |
| Fz_all | **−561 N** | 100% |

Balans baseline **60,3%** przód → z wąsami best **57,3%** (kilka pp). UT to duży, często „tylny” kawałek Fz.

**Staniszewski 2024:** pełny pakiet (FW+RW+**UT&SW**) ma **wyższe |Cz| dla każdego** δśrd vs FW&RW; Cx(δ) przecina się (~niższy Cx pełnego pakietu **0–10°**, wyższy **10–20°**). Po modelu toru: średnia siła hamująca **F2/F1 = 0,973** → **−2,7%** mimo **+~10 kg** masy UT — proxy energii Endurance (**high** jako F_ham; **med** jako Wh).

### 2.2 Yaw / steer / ride height — ostrzeżenia praktyczne

Yaw = kąt „bokiem do napływu”, jak w zakręcie. Podłoga na to mocno reaguje.

| Claim | Evidence | Confidence |
|-------|----------|------------|
| **UT&SW silnie wrażliwe** na kierunek napływu; nominal ~0°; przy δ≠0 istotny spadek sił z podłogi; FW/RW „płaskie” | Staniszewski 2024 s. 55–56 | **high** |
| Nie ekstrapolować zakrętu z samego δ=0 | Staniszewski 2024 Podsumowanie | **high** (metoda) |
| FST Lisboa aeromap: **yaw** najbardziej wpływowy — **~16%** zmiany DF w badanym zakresie; roll **~9%** DF i **~12%** przesunięcia CoP; ride height **~10%** CD·A i **~20%** −CL·A między peakami | Técnico Lisboa / FST10e thesis abstract | **high** na ich aucie; **med** transfer |
| Chalmers CFS: kąty ekspansji **13°** vs **19°** — oba wysoki DF, wybrano **13°** dla **robustness** w manewrach; typowo ~**15°** jako start, zbyt stromy → separacja | Chalmers undertray thesis | **med–high** |
| GC min. **30 mm** static z kierowcą (T 2.2.1); zakaz sliding skirts / kontaktu z torem (T 2.2.2) | fs-rules-2026-t8 | **high** |
| Monash aero map: ground-effect wrażliwy na FRH/RRH/roll/steer/yaw — mapowanie postaw > jeden case @0° | Hendy / Monash 2019 | **high** (metoda) |

**Rada Spec (H2):** szukać **tylniejszego** docisku dyfuzora / uszczelnienia tyłu **bez obniżania nosa FW**. Gate przed zamrożeniem: **mapa Cx/Cz vs δ** (+ roll / RH jeśli budżet) i model toru Endurance. Nie optymalizować UT tylko pod δ=0 — Autocross to właśnie δ≠0.

---

## 3. H3 — odciążenie FW (ostatnia dźwignia balansu, nie pierwsza)

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Dokręcanie samego FW pcha balans na przód i utrudnia 50/50 | research-balance-shift; fizyka pakietu; Nagłowski: FW ~39% Fz | **high** |
| FW unload (kąt / elementy w dół) — tylko jeśli H1+H2 nie domykają ~12 pp | shortlista H3 w research-balance-shift | **high** jako kolejność Spec |
| Box FW: wysokość < **500 mm** przed HR; outboard przed osią < **250 mm**; envelope przy każdym setupie zawieszenia (T 8.2.1–4) | fs-rules-2026-t8 | **high** |
| Łatwo stracić \|Cz\| poniżej 3,682 przy odciążeniu przodu — mierzyć ΔCz równolegle z Δbalans | guardrail TARGETS | **high** (ryzyko) |

**Rada Spec (H3):** trzymać FW jako **stabilizator** Autocross (mniej yaw-sensitive niż UT — Staniszewski 2024), nie jako generator „brakujących Newtonów”. Odciążać dopiero z tabelą: ile pp balansu za ile |Cz|.

---

## 4. H4 — wąsy (TBD; nie baseline)

Z **Nagłowski 2024** (profil **Selig S1223** w ich serii — u nas **dobór profilu otwarty**):

| Wielkość | Baseline | Best iter111.4 |
|----------|---------:|---------------:|
| Cx | **1,453** | **1,480** |
| Cz | **−4,071** | **−4,100** |
| Balans przód | **60,3%** | **57,3%** |
| Cz/Cx | **−2,802** | **−2,770** |
| Fz_whiskers | — | **+12,9 N** (nośna!) |

Mechanizmy: blisko FW — wąs **kradnie** powietrze spod FW → cofa balans; nad wahaczem — chroni RW przed brudnym powietrzem; pozytywny wpływ też na UT. Same wąsy **nie** są generatorem docisku.

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Wąsy cofają balans o **kilka pp** przy lekkim koszcie L/D | Tab. 5.2: 60,3→57,3%; eff −2,802→−2,770 | **high** na ich aucie; **low–med** transfer na 017 |
| Nie automatycznie S1223 — dobrać profil pod lokalizację | decyzja Spec 2026-09-01 | **high** (proces) |
| Wchodzą **po** H1–H3, jeśli nadal za dużo z przodu | research-balance-shift H4 | **high** (kolejność) |

---

## 5. Co jest OUT / poza peak-DF

### 5.1 DRS ruchomy — OUT

- Jackson: open = −**35%** drag, ale DF spada mocno (CL 1,15→0,26).
- Własne `RW_iter019/020` (z research-balance-shift): Cx ↓ do **~0,83**, |Cz| ↓ do **~3,01** — **poniżej** kotwicy 3,682.
- **Wniosek:** DRS (nawet pasywne otwarcie) to narzędzie **prostych / oporu**, nie trzymania peak-DF ani domykania 12 pp balansu high-DF. Ruchomy = OUT; pasywny = osobna gałąź, nie ścieżka Spec peak.

### 5.2 Fan spod podłogi — OUT

- Michalecki: na profilowanej podłodze PM08 wentylator **psuje** |Cz| (~**30%+** gorzej vs baza Cz **−2,036**); żadna iteracja nie pobiła bazy.
- Legalnie T 11.11.1 ≤ **500 W** — ale decyzja osiągów = OUT (nie redesign pod ssanie).

---

## 6. Ograniczenia regulaminu i konstrukcji (nie „nice to have”)

| Limit | Treść | Impact na targety |
|-------|-------|-------------------|
| T 8.2.1 | RW za HR: wysokość < **1,1 m**; FW < **500 mm**; outboard przed osią < **250 mm** | Max chord/span RW ograniczone boxem — 4-el. musi zmieścić się w **250 mm** za oponami (T 8.2.3) |
| T 8.2.2 | RW (>500 mm): nie outboard od most inboard **tylnej** opony | Wąski box szerokości — endplate/4-el. |
| T 8.2.4 | Envelope przy **any** suspension setup, z kierowcą i bez | Nie projektować „idealnego” RH tylko w CAD static |
| T 8.3.1–2 | **200 N** / ≥**225 cm²** → ugięcie ≤**10 mm**; **50 N** dowolny punkt → ≤**25 mm** | 4-el. + duże endplate = więcej powierzchni do ugięcia (Quintanas: tip endplate flex) |
| T 2.2.1 | GC ≥ **30 mm** static | Dyfuzor agresywny vs kontakt / T 2.2.2 skirts |
| T 11.11.1 | Active air movers ≤ **500 W** | Fan OUT i tak; cooling fans w limicie |

---

## 7. Endurance + Autocross — jak czytać trade-offy

| Event | Co wynika ze źródeł | Czego unikać |
|-------|---------------------|--------------|
| **Autocross** | Docisk w zakresie δ ważniejszy niż sam peak @0°; UT pomaga \|Cz\|, ale **traci** przy yaw — FW/RW stabilniejsze (Staniszewski 2024). Yaw może ruszyć DF o rząd **~16%** (FST Lisboa) | Optymalizacja UT tylko @ δ=0; „sztywny” dyfuzor bez mapy |
| **Endurance** | UT może **obniżyć** proxy energii (−**2,7%** F_ham mimo +~**10 kg**); trzeba modelu toru (udziały r). Bez DRS open — Cx ≲ 1,23 jest twardym limitem energii/prostych | Przenoszenie −2,7% na inny tor; dokładać masę aero bez proxy energii; fan |
| **Accel / długie proste** (niższy priorytet) | Jackson DRS −35% drag **niedostępne** jako aktywna ścieżka; pasywny low-AOA RW = świadomy trade \|Cz\| | Pogarszanie Cx 017 bez zwrotu w lap/energii |

**Praktyczna reguła Spec:** najpierw **tył (H1)** żeby zbliżyć CoP do 50/50 przy trzymanym |Cz|; potem **UT (H2)** pod DF+energię z gate yaw; FW (H3) tylko do domknięcia pp; wąsy (H4) jako polish.

---

## 8. Ostrzeżenia pakietowe (checklist przed zamrożeniem geometrii)

1. **Coupling 2D→3D:** optimum overlap/kątów z izolowanego RW **nie** przenosi się 1:1 (Staniszewski 2023: Cx/Cz na aucie prawie flat mimo dużego zysku 2D).
2. **Yaw/steer UT:** sam Cx@δ=0 **kłamie** przy mocnej podłodze — mapa δ przed freeze.
3. **Ride height / pitch:** ground effect i dyfuzor wrażliwe na FRH/RRH; GC **30 mm** + ugięcia T8.3 + bump = projektuj z marginesem, nie na styk.
4. **Sztywność T8.3:** zwłaszcza duże endplate i 4. element — ugięcie tipów zmienia skuteczny AOA w zakręcie.
5. **Nie mieszać modeli:** Nagłowski Cz≈−4,07 / Staniszewski pojazd Cz≈−2,03 / Jackson CL≈1,15 / **017 Cz=−3,682** — różne Aref/V/pakiety. Kierunki OK; liczby nie uśredniać.
6. **Nie inventować Aref** — Fluent Reference Values przed porównaniem OF.
7. **Wąsy:** Fz_whiskers > 0 — success metric = Δbalans / ΔRW / ΔUT, nie „siła na wąsie”.
8. **DRS/fan:** nie wracają jako „łatwy Cx” przy celu |Cz| ≥ 3,682.

---

## 9. Claims — tabela zbiorcza (do Spec)

| # | claim | evidence | confidence |
|---|-------|----------|------------|
| C1 | Główne dźwignie cofania balansu = **RW + UT**, nie samo FW | Spec + research-balance-shift; Nagłowski udziały Fz; Staniszewski 2023/24 | **high** |
| C2 | Balans 017 ≈ **61,6%** przód; gap ≈ **12 pp** do 50/50 | Cm/Cz RW_iter017; zamrożenie 2026-09-01 | **high** roboczo; **med** vs pełny postpro Fluent CSV |
| C3 | Guardrail: \|Cz\| ≥ **3,682**, Cx ≲ **1,23** @ 15 m/s | TARGETS / CSV 017 | **high** |
| C4 | Optimum overlap RW ~**−30 mm** w 2D; na aucie wymaga re-check | Staniszewski 2023 Tab. 2D | **high** 2D; **med** 3D pakiet |
| C5 | Gap/overlap start McBeath **1–4%c / 1–6%c**; flaps ~25–30° / 30–70° | Jackson 2018 | **high** start |
| C6 | 4-el. RW = więcej parametrów setupu + potencjalnie więcej tyłu; koszt masa/sztywność/coupling | Quintanas 2023; Spec | **med** (zysk na 017 do zmierzenia) |
| C7 | Gurney ~**1–2%c** na ostatnich elementach = tani DF z tyłu | literatura Gurney + Quintanas setup | **med–high** |
| C8 | UT ~**1/3** Fz w pakiecie Nagłowskiego; pełny pakiet z UT wyższe \|Cz\| vs FW&RW dla każdego δ | Nagłowski Tab. 5.3; Staniszewski 2024 | **high** kierunek |
| C9 | UT yaw-sensitive; gate = mapa Cx/Cz(δ) + model toru (−**2,7%** F_ham proxy) | Staniszewski 2024; FST Lisboa ~**16%** DF vs yaw | **high** |
| C10 | Dyfuzor: start ~**13–15°** ekspansji, preferuj robustness nad max kątem | Chalmers 13° vs 19° | **med** |
| C11 | Wąsy: kilka pp balansu tył, lekki koszt L/D; same nośne; TBD po H1–H3 | Nagłowski 60,3→57,3% | **high** u nich; **low–med** transfer |
| C12 | Pasywne/open DRS obniża \|Cz\| poniżej 3,68 — nie ścieżka peak-DF | Jackson; RW_iter019/020 Cx~0,83 / \|Cz\|~3,01 | **high** |
| C13 | Fan OUT na profilowanej podłodze — psucie \|Cz\| ~30%+ vs baza PM08 | Michalecki | **high** |
| C14 | T8.3 + GC **30 mm** + box RW limitują agresję 4-el. / dyfuzora | FS Rules 2026 v1.1 | **high** |

---

## 10. Rekomendacje dla Spec (krótka shortlista)

1. **Kolejność prac:** H1 (RW, rozważyć 4-el. + gurney 1–2%c na TE) → H2 (UT/dyfuzor tylniejszy + mapa δ) → H3 (FW unload tylko do domknięcia pp) → H4 (wąsy, profil pod lokalizację).
2. **Każda iteracja raportuje:** Cx, Cz, Cm, **balans %** przy x=0,765 m — nie tylko „ładniejsze Cp”.
3. **4-el. RW:** tak jako kandydat setupu/peak tyłu; zamrozić dopiero po porównaniu z 3-el. na **tym samym** pakiecie 017 (coupling!).
4. **UT:** nie freeze bez Cx/Cz(δ); celuj w kąt ekspansji raczej **robust** (~13–15°) niż max theoretical; GC ≥ 30 mm z marginesem ugięć.
5. **FW:** nie dokręcać; odciążać świadomie z tabelą Δpp vs Δ|Cz|.
6. **DRS/fan:** zostają OUT względem peak-DF; pasywne klapy tylko jeśli kiedyś osobno liczycie energię prostych bez łamania |Cz|≥3,682.
7. **Walidacja:** CFD → symulacja toru → tor (nitki / flow-vis) — zgodnie z decyzją Spec; bez inventowanego Aref.

---

## Źródła (lokalne + web użyte w tej notatce)

**Lokalne KB:** `research-balance-shift.md`, `staniszewski-2023-wing.md`, `staniszewski-2024-energy.md`, `naglowski-2024-package.md`, `jackson-2018-cfd-drs.md`, `fs-rules-2026-t8.md`, `michalecki-fan-ground-effect.md`, `team-rwiter017-baseline.md`, `TARGETS.md`.

**Web (uzupełnienie multi-el. / gurney / yaw):**  
- Quintanas i Yani, *Design and manufacturing of a rear wing for Formula Student* (Dynamics UPC, 2023) — 4-el. RW, gurney, setup eventów.  
- McBeath guidelines via Jackson 2018 (gap/overlap/AOA).  
- Gurney: ICAS 2006; PMC4897339 (wysokość 1–2%c).  
- Yaw/aeromap: FST Lisboa aerodynamic mapping (~16% DF vs yaw).  
- Diffuser robustness: Chalmers CFS undertray (13° vs 19°).  
- LUTPUB Metropolia multi-element RW performance trade-offs (kierunek lap vs drag).
