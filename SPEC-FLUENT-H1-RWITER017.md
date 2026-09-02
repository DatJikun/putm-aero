# Kampania Fluent H1 — tylne skrzydło na RWiter017

Krótki plan Spec po zaparkowaniu 2D OpenFOAM. Liczymy **na aucie we Fluencie**, nie przenosimy Cl z 2D.

---

## Po co

Cofnąć balans z ok. **62%** na przód w stronę **50/50**, nie pogarszając docisku i trzymając spokojny opór. Najpierw **tylnie skrzydło** (H1), podłoga później (H2).

---

## Punkt startu (nie zmieniać)

Z `TARGETS.md` / RWiter017 @ 15 m/s, half-car, Aref **0,50 m²**, Lref **1,53 m**, moment przy **x = 0,765 m**:

- Cx = **1,229**
- Cz = **−3,682**
- Cm = **−0,429**
- balans przód ≈ **61,6%**

---

## Co kręcić (tylko RW)

Na geometrii **3-elementowej** (domyślna ścieżka):

1. Kąty elementów (zwłaszcza main / flapów) — ostrożnie, bez pchania w stall.  
2. Overlap i szczelina (gap) między elementami.  
3. Ewentualnie lokalne detale TE / endplate tylko jeśli nie mieszają setupu Fluent.

**4 elementy:** jeden case porównawczy obok zwycięskiego 3-el. — nie domyślna baza.

Nie kopiujemy Cl/Cd ani „optimum” z serii 2D OpenFOAM na ten case. 2D może najwyżej podpowiedzieć **kierunek** (np. „nie podnoś main”), gdy wróci z czystym mesh study (`SPEC-H1-2D-GATE.md` = instrukcja na później).

---

## Kill / pass (całe auto)

Case odpada albo nie idzie do CAD final, jeśli:

- |Cz| **spada poniżej 3,682** (gorzej niż baseline), albo  
- Cx **wyraźnie powyżej ~1,23** bez świadomej decyzji, albo  
- balans **nie idzie w stronę 50/50** (albo jedzie w złą stronę — jeszcze bardziej na przód).

Pass diagnostyczny: |Cz| ≥ 3,682, Cx ≲ 1,23, balans bliżej 48–52% niż 62%.

Raportuj Cx, Cz, Cm, balans % (albo Cz przód/tył) przy tym samym Aref/Lref/punkcie momentu.

---

## Kolejność

1. Baseline RWiter017 odtworzony / potwierdzony w Fluent (te same liczby).  
2. Seria 3-el.: overlap → gap → kąty (albo kąty po ustaleniu slotów — byle jeden parametr naraz).  
3. Jeden porównawczy **4-el.**  
4. Dopiero potem H2 podłoga (osobna kampania).

---

## Świadomie poza tą kampanią

- OpenFOAM half-car i 2D OF — **zaparkowane** / nie blokują Fluenta.  
- DRS ruchomy — OUT.  
- Wentylator — OUT.  
- Wąsy — TBD, nie w tej serii.

---

*Źródło prawdy liczb: `TARGETS.md`. Bramka 2D na przyszłość: `SPEC-H1-2D-GATE.md`.*
