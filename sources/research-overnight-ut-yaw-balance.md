# Overnight research: podłoga / dyfuzor — balans i wrażliwość na yaw

**Status:** notatka z researchu nocnego (2026-09-01 → rano 2026-09-02 Europe/Warsaw)  
**Język:** PL, zdania czytelne  
**Zasada:** cytujemy **Staniszewski 2024** (już w repo) + nowe źródła publiczne. Liczby Cl/Cd/balansu z Chalmers/OSU dotyczą **ich** aut — nie przepisujemy ich na `RW_iter017`.

**Kotwica Spec:** `RW_iter017` Cx **1,229** / |Cz| **3,682** / balans ≈ **61,6%** przód → ~**50%**; DRS OUT; fan OUT; po H1 RW idzie **H2 UT**; Aref half ≈ **0,50 m²**; eventy **Endurance + Autocross**.

Siostrzana notatka paperów: [research-papers-rw-ut-yaw-clcd.md](research-papers-rw-ut-yaw-clcd.md).

Powiązane: [staniszewski-2024-energy.md](staniszewski-2024-energy.md), [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md), [research-aero-for-targets.md](research-aero-for-targets.md), [michalecki-fan-ground-effect.md](michalecki-fan-ground-effect.md).

---

## 1. Dlaczego UT jest inną dźwignią niż RW

Skrzydła (FW/RW) siedzą w względnie „wolnym” napływie i w mapach vs kąt skrętu bywają **płaskie**. Podłoga z dyfuzorem żyje z **ground effect**: szczelina do toru, uszczelnienie krawędzi, wiry w dyfuzorze, pitch/roll/yaw. W zakręcie napływ pod podłogę jest skośny (yaw / body slip), a samochód ma jeszcze roll i często pitch przy hamowaniu. Dlatego H2 (UT) potrafi **mocno ruszyć balans i energię**, ale też **stracić DF dokładnie wtedy, gdy tor Endurance tego DF najbardziej potrzebuje** — w łuku.

Cel Spec (~12 pp cofnięcia balansu przy max |Cz| i Cx ≲ 1,23) oznacza: UT ma dokładać **tył** (albo przynajmniej nie dokładać przodu), a jednocześnie nie być „paper tigerem” tylko przy δ = 0°.

---

## 2. Staniszewski 2024 (PUT) — już w KB, kotwica yaw/energii

Pełny ekstrakt: [staniszewski-2024-energy.md](staniszewski-2024-energy.md). Skrót wniosków istotnych dla H2:

1. **Charakterystyka w zakręcie nie da się ekstrapolować** z samego case’u „na wprost”. Interakcje są niestabilne bez siatki punktów CFD vs średni kąt skrętu δśrd.
2. **UT&SW jest silnie wrażliwa na kierunek napływu.** Nominalny punkt pracy ~0°. Przy δ ≠ 0 istotny spadek sił z podłogi/sekcji bocznych; FW/RW są względnie „płaskie”.
3. Pełny pakiet (z UT) ma **wyższe |Cz| dla każdego δ** vs konfiguracja FW+RW. Krzywe **Cx(δ)** przecinają się (~niższy Cx pełnego pakietu 0–10°, wyższy 10–20°) — bez **modelu toru** (udziały prostych/łuków) nie wiemy, kto wygrywa oporem.
4. Po zważeniu toru: pełny pakiet daje **~2,7% niższą** średnią siłę hamującą (proxy energii) mimo **+~10 kg** masy UT. To **nie** jest zmierzone Wh baterii.
5. Metodę (mapa Cx/Cz vs δ + model toru + F_ham) warto **włożyć na stałe** do procesu EV FS, zwłaszcza pod Endurance.

**Implikacja projektowa H2:** nie optymalizować dyfuzora wyłącznie pod peak przy δ = 0. Każdy kandydat UT powinien dostać przynajmniej kilka punktów δ (jak Tab. 9 w pracy: r od ~17,5 m w dół) zanim ogłosimy „+X N tyłu”.

Confidence: kierunek wrażliwości UT vs skrzydła — **high** (tekst pracy). Konkretne Cx/Cz per δ — głównie na wykresach, **med/low** bez ponownego odczytu PDF.

---

## 3. Chalmers FS 2021 — dyfuzor w manewrach (prosta / hamowanie / cornering)

Źródło: de Wilde et al., *Development and performance evaluation of undertray diffusers during racing manuevers*, Chalmers bachelor’s thesis 2021.

- Strona item: [https://odr.chalmers.se/items/80856146-3eb6-4d0b-832f-e2d793e7c54a](https://odr.chalmers.se/items/80856146-3eb6-4d0b-832f-e2d793e7c54a)
- PDF bitstream: [download](https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download)

### 3.1 Metoda (jakościowo)

Trzy scenariusze CFD: **jazda na wprost**, **hamowanie** (pitch), **cornering** (przepływ zakrzywiony / asymetria). Parametry dyfuzora: punkt startu (throat), kąt ekspansji, promień throat, **strakes**, **side floors**. Metryki: CD, CL, CL na monocoque+dyfuzor, **aero balance (rearwards)**.

### 3.2 Wyniki istotne dla balansu i „yaw-like” cornering

- W cornering **większy obszar niskiego Cp jest po wewnętrznej stronie** łuku → więcej docisku na wewnętrznej połowie — efekt, który w dynamice pomaga dociążać wewnętrzne opony (kierunek zgodny z intuicją OSU poniżej).
- Większy kąt ekspansji → bardziej agresywne oderwanie / bąbel separacji w środku dyfuzora (skin friction). **13°** miało najgładszy, przyklejony przepływ; **19°** też dawało wysoki DF, ale mniej „kontrolowany”.
- Autorzy wybrali **13°** jako najlepszy kompromis **robustness** we wszystkich trzech scenariuszach (niekoniecznie absolutny peak w jednym case).
- **Strakes** dzielą kanały, indukują dodatkowe wiry, **zmniejszają bąbel separacji** — szczególnie widać w cornering.
- **Side floors** powiększają obszar niskiego ciśnienia i w ich tabelach podnoszą CL w większości scenariuszy.

Fragment tabeli kątów (ich samochód CFS — **nie kopiować na 017**):

| Design | Scenario | CD | CL | Aero balance (rear) |
|--------|----------|-----:|-----:|--------------------:|
| 13° | Straight | 1,419 | 3,729 | 49,68% |
| 13° | Cornering | 1,380 | 3,603 | 49,38% |
| 19° | Straight | 1,402 | 3,663 | 49,35% |
| 19° | Cornering | 1,417 | 3,567 | 49,54% |

Po strakes + side floors (13°): CL straight **3,854**, cornering **3,619**, braking **3,005**; aero balance przy hamowaniu skacze mocno do tyłu (**~67%** rear w ich definicji) — pitch przy brake **migruje balans**. To ostrzeżenie pod Endurance: setup zoptymalizowany tylko pod δ=0 może zachowywać się inaczej przy brake–turn.

### 3.3 Wnioski dla H2 PUT

- Kryterium wyboru UT: **robustness across straight / brake / corner**, nie sam peak CL.
- Dźwignie geometryczne z Chalmers mapują się na nasz CAD: kąt dyfuzora, lokalizacja throat (to też **balans** — patrz OSU/Katz), strakes, side floors / sekcje boczne.
- Asymetria Cp w cornering = naturalny „yaw effect” nawet bez osobnej etykiety „yaw sweep” — warto w Fluent mieć case z napływem skośnym lub kinematyka jak u Staniszewskiego.

---

## 4. Jensen / OSU 2010 — undertray FSAE, balans i yaw 5°

Źródło: Karl Jensen, *Aerodynamic Undertray Design for Formula SAE*, Oregon State University, MSc 2010.

- PDF: [https://ir.library.oregonstate.edu/downloads/7h149t91w](https://ir.library.oregonstate.edu/downloads/7h149t91w)

### 4.1 Mechanika balansu przez dyfuzor

Jensen (za Katz i literaturą underbody) podkreśla dwie rzeczy, które często mylą teamy:

1. Dyfuzor **nie** „produkuje całego DF podłogi” przez magiczne rozszerzanie gęstości — jego rola to **odzysk ciśnienia** i utrzymanie efektywności układu dysza–gardziel–dyfuzor.
2. **Lokalizacja wejścia dyfuzora** przesuwa peak niskiego ciśnienia wzdłuż auta → to jest bezpośrednia dźwignia **center of pressure / balansu**. Przesunięcie throat do przodu lub do tyłu zmienia understeer/oversteer aero.

Kąt dyfuzora: w 2D optimum bywa bardzo płaskie (~5° w cytowanej symulacji), ale w 3D wir wejściowy pozwala na **większe kąty** zanim nastąpi separacja. Po separacji: spadek DF i skok drag.

### 4.2 Yaw 5° i roll

- Symulacja **5° yaw**, bez roll: u nich DF wzrosło do **62 lb** (względem niższego case’u prostego w tej samej sekcji); asymetria ciśnienia generuje moment roll **do wewnątrz** zakrętu — korzystne dla dociążenia wewnętrznych opon.
- **5° yaw + 1° roll:** DF **spadło o 6%** względem samego yaw → z punktu widzenia aero mniej rollu = więcej DF.
- Ride height: **małe zmiany prześwitu → duże zmiany obciążeń** (klasyczna wrażliwość ground effect).
- Tor: b–b z undertray → **~1%** poprawa lap time; błąd CFD vs pomiar DF ~**31%** — pokora walidacyjna.

Implikacja: H2 musi żyć ze **sztywnością zawieszenia / pitch-roll**, nie tylko z CAD dyfuzora. Mapowanie yaw 5° jest tanim „stress testem” przed pełną mapą δ Staniszewskiego.

---

## 5. Jowsey & Passmore (Loughborough) — multi-channel dyfuzory

- Teza: L. Jowsey, *An experimental study of automotive underbody diffusers*, Loughborough, 2013 — [https://dspace.lboro.ac.uk/2134/13646](https://dspace.lboro.ac.uk/2134/13646) (zawiera sekcje **Yaw Tests**).
- Paper: Jowsey & Passmore, *Experimental study of multiple-channel automotive underbody diffusers*, Proc. IMechE Part D, 2010 — [https://doi.org/10.1243/09544070JAUTO1339](https://doi.org/10.1243/09544070JAUTO1339)

Główny wniosek jakościowy z abstraktu paperu: dzielenie dyfuzora na **wiele kanałów** (2–4) daje duże zyski DF **tuż powyżej** kąta optimum płaskiego dyfuzora (tam, gdzie plane diffuser już częściowo się odrywa), przy **minimalnym** wzroście drag. Mechanizm: lepsze „diffuser pumping” i odzysk w kanałach wewnętrznych i zewnętrznych.

Dla nas: strakes / multi-channel (jak Chalmers) to nie kosmetyka — to narzędzie **rozszerzania envelope kąta** i potencjalnie **robustness przy yaw**, bo kanały ograniczają spanwise migrację separacji. Pełne krzywe yaw z tezy Jowsey warto dorzucić po dropie PDF (w tej sesji nie ekstrahowano tabel yaw liczbowo).

---

## 6. Implikacje torowe: Autocross vs Endurance

| Aspekt | Autocross | Endurance |
|--------|-----------|-----------|
| Dominanta | Peak grip w ciasnych łukach, krótkie proste | Energia + stabilny grip przez długi stint |
| UT przy δ≠0 | Staniszewski: UT traci efektywność — ale nadal podnosi \|Cz\| vs brak UT | Ten sam spadek × wiele okrążeń; liczy się **średnia** z modelu toru |
| Opór | Krótki wpływ | Proxy F_ham (Staniszewski −2,7% z UT mimo +10 kg) — UT może **oszczędzać energię**, jeśli model toru podobny |
| Balans | Kierowca czuje under/oversteer od CoP; throat location (OSU) = dźwignia | Zmęczenie opon + migracja balansu przy brake (Chalmers ~67% rear przy braking) → setup „50/50 na prostej” ≠ 50/50 w sekwencji |
| Yaw/roll | 5° yaw może nawet podnieść DF (OSU), roll go zjada | Stabilność aero w ruchu: uniknąć stall dyfuzora przy pitch+yaw jednocześnie |

**Priorytet Spec = Endurance + Autocross** ⇒ H2 nie może być „tylko peak δ=0”. Minimalny pakiet testów CFD dla kandydata UT:

1. δ = 0 (baseline porównawczy do 017),
2. 1–2 punkty δ / yaw (np. 5° albo punkty z Tab. 9 Staniszewskiego),
3. opcjonalnie pitch hamowania, jeśli damy radę kinematycznie,
4. metryki: Cx, Cz, Cm, **balans %**, udział Fz z UT (jeśli postpro pozwala), wizualnie Cp/separacja w dyfuzorze.

Guardrale jak w TARGETS: |Cz| ≥ 3,682, Cx ≲ 1,23, balans w stronę 48–52% przód (~12 pp od 61,6%).

---

## 7. Fan OUT — przypomnienie

Michalecki (KB): wentylator spod podłogi na PM08 **nie bije** bazy osiągami w ich teście → Spec **fan OUT**. T 11.11.1 limituje moc urządzeń „designed to move air” do **500 W**, ale to nie jest nasz powód OUT — powodem są osiągi/masa/complexity. H2 = geometria UT, nie active suction.

---

## 8. Claims (claim | evidence | confidence)

- UT&SW traci efektywność przy δ≠0 mocniej niż FW/RW | Staniszewski 2024 | **high**
- Pełny pakiet z UT i tak wygrywa \|Cz\| w całym zakresie δ; Cx(δ) przecina się ~10° | Staniszewski 2024 | **high**
- Proxy energii −2,7% z UT mimo +~10 kg na modelowanym torze | Staniszewski 2024 s.67–68 | **high** jako F_ham; **med** jako Wh
- Kąt dyfuzora ~13° bywał bardziej robust niż 19° w manewrach CFS | Chalmers 2021 abstrakt + Tab. 4.3 | **med** (ich auto); kierunek „nie max angle” | **high**
- Strakes + side floors poprawiają DF / kontrolę separacji w cornering | Chalmers Tab. 4.5 + figs | **med–high** (ich CFD)
- Wejście dyfuzora przesuwa CoP / balans | Jensen/OSU + Katz (cyt.) | **high** (mechanizm)
- 5° yaw może zwiększyć DF i dać inboard load; +1° roll −6% DF | Jensen tekst | **med** (jedna geometria)
- Multi-channel rozszerza envelope kąta dyfuzora | Jowsey & Passmore 2010 | **high** (WT bluff body); transfer na FS monocoque | **med**

---

## 9. Luki / PDF do dropu

1. Ponowny / pełniejszy odczyt wykresów Cx(δ), Cz(δ) ze **Staniszewski 2024** (liczby tylko na rysunkach) — jeśli Mikołaj wrzuci PDF + ewentualnie arkusz.
2. Tabele **yaw** z tezy Jowsey (Loughborough) — dspace PDF.
3. Nasze **UT iters CSV** vs realny udział Fz_UT na RWiter017 (postpro Fluent) — bez tego H2 planuje w ciemno wielkość dźwigni.
4. Ewentualny PDF lokalnych testów ride height / rake — OSU pokazuje ogromną wrażliwość; nie mamy zamrożonej mapy rake dla 017.

---

## Źródła (URL)

- Staniszewski 2024 — lokalnie `sources/staniszewski-2024-energy.md`
- Chalmers 2021 — https://odr.chalmers.se/items/80856146-3eb6-4d0b-832f-e2d793e7c54a
- Jensen OSU 2010 — https://ir.library.oregonstate.edu/downloads/7h149t91w
- Jowsey teza — https://dspace.lboro.ac.uk/2134/13646
- Jowsey & Passmore 2010 — https://doi.org/10.1243/09544070JAUTO1339
