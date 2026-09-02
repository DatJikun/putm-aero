# H3 — odciążenie przedniego skrzydła pod balans (po H1 i H2)

**Status:** preferencja dla Spec, 2026-09-02 (Europe/Warsaw)  
**Kolejność pakietu:** H1 RW → H2 podłoga → **H3 FW unload** tylko gdy balans nadal za bardzo na przodzie.  
**Kotwica:** RWiter017 ≈ **61,6%** przód → cel ~**50/50** (~12 pp). DRS OUT, fan OUT.  
**Zasada:** liczby z cytowanych źródeł. Nie zmieniamy `TARGETS.md`. Udział FW na 017 = **TBD** (Fluent).

Szerszy overnight: [research-overnight-h3-fw-unload-rw-gaps.md](research-overnight-h3-fw-unload-rw-gaps.md).

---

## 1. Dlaczego H3 jest na końcu

Literatura i shortlista H1–H5 mówią to samo: najpierw dokładaj / poprawiaj **tył** (RW, podłoga), a dopiero potem **odejmuj z przodu**. Odciążenie FW łatwo zjada cały |Cz| i psuje Autocross, jeśli zrobisz to za wcześnie.

Craig & Passmore (SAE 2014-01-0596): flapy służą do dopasowania balansu do masy; w ich setupie udział DF na przedniej osi był w zakresie

- **45–60%** przód  

Pamnani et al. (IJRASET 2020): lekki front bias

- **56%** przód  

regulowany kątami flapów. Przy spadku ride height DF rośnie i balans idzie **do przodu** (~±5% w ich mapie) — czyli wyższy nos / mniej FW działa w stronę H3.

---

## 2. Jak dużą dźwignią jest FW (opublikowane siły)

**Nagłowski 2024 (PUT, inny pakiet niż RWiter017)** @ **15 m/s**:

- Fz_all ≈ **−561 N**  
- Fz_fw = **−221 N**  
- udział FW ≈ **39%** Fz  

To pokazuje, że FW bywa dużym kawałkiem — na 017 trzeba to zmierzyć osobno, nie kopiować −221 N.

**KTH DeV18 (Hokkanen 2024)** — ujemny kąt elementów FW = odciążenie; zmiany CoP były **małe** przy ich krokach kąta (siły FW rzędu ~100 N w tabeli kątów 0/−5/−10/−15°). Wniosek: małe −Δα może dać mały Δbalans — nie licz na cud bez pomiaru.

**EngProc (cyt. overnight):**

- FW = **195 N** @ 54 km/h (fragment o systemie skrzydeł)

**FW = 588 N:** w KB i overnight **nie znaleziono**. Nie inventujemy.

---

## 3. Kiedy wolno ruszać H3

Ruszaj H3 dopiero gdy:

1. H1 (RW) i H2 (UT) są już na stole,  
2. balans nadal **>~52%** przód (roboczy próg z overnight checklist),  
3. |Cz| trzyma się kotwicy **−3,682** albo jest plan jak to odzyskać tyłem,  
4. Cx nie wybucha przy odciążeniu (pilnuj Cx ≲ **1,23** orientacyjnie z karty).

Nie ruszaj H3 „żeby szybko zbliżyć się do 50/50” kosztem docisku.

---

## 4. Co mierzyć w Fluent / OF

Na half-car / full-car przy **15 m/s**, Aref **0,50 m²** (half):

- Cx, Cz, Cm  
- balans % przód (ten sam wzór co w arkuszu; punkt momentu jak w workflow)  
- udział Fz_fw / Fz_all (osobne linie)  
- Cp / separacja na FW (czy odciążenie nie robi dziury w przepływie do UT/RW)

Sweep roboczy:

1. −Δα main FW (małe kroki),  
2. −Δα flap FW,  
3. dopiero kombinacje.

Kill: |Cz| wyraźnie poniżej kotwicy; balans cofnięty, ale auto „pływa” z przodu w AX (jakościowo — potwierdzić sim/tor).

---

## 5. Luki

- Udział FW/RW/UT na **RWiter017** w N i % — **TBD** (postpro / CSV).  
- Δbalans pp vs −1° FW @ 15 m/s na 017 — **not found**.  
- FW = 588 N — **not found**.  
- Gotowa mapa heave/pitch tylko pod unload FW dla PUT — **not found**.

---

## 6. Werdykt dla Spec

H3 to **ostatnia** dźwignia balansu, nie pierwsza. Kierunek (mniej FW → mniej % przodu) jest pewny fizycznie i w paperach; wielkość na 017 poznamy dopiero z Fluent po H1/H2. Do CAD z H3 idziemy dopiero z liczbami z Waszego modelu, nie z −221 N Nagłowskiego.
