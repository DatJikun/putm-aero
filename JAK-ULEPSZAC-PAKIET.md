# Jak ulepszać pakiet aerodynamiczny

To nie jest katalog plików. To kolejność pracy: **co ruszać, w jakiej kolejności i po co**, żeby dojść od dzisiejszego bolidu do lepszego pakietu pod Endurance i Autocross.

Liczby poniżej biorą się wyłącznie z karty celów ([TARGETS.md](TARGETS.md)). Nie kopiujemy tu Cl z OpenFOAM 2D ani z innych teamów.

---

## Gdzie jesteśmy

Jedziemy na **RWiter017** we Fluencie (15 m/s, half-car). Dziś mamy mniej więcej:

- opór Cx ≈ **1,23**
- docisk Cz ≈ **−3,68**
- balans na przód ok. **62%** — za mocno z przodu

Chcemy **więcej użytecznego docisku** przy możliwie małym oporze i balansie bliżej **pół na pół** (ok. 50/50). Brakuje nam ok. **dwunastu punktów procentowych** w tył — czyli trzeba **cofnąć docisk** (tylnie skrzydło i podłoga), a nie dokręcać samego przedniego na ślepo.

Szerszy obraz sezonu: [SEASON-DIRECTION.md](SEASON-DIRECTION.md).

---

## Kolejność (trzymaj się jej)

### 1. Tylne skrzydło najpierw (domyślnie trzy elementy)

Zaczynamy od tylnego, bo to najprostsza dźwignia „więcej tyłu” przy naszym starcie z przodu. Domyślna ścieżka to **trzy elementy** na bazie tego, co już jest na 017. **Cztery elementy** robimy najwyżej jako **jedno porównanie** obok najlepszego wariantu trójelementowego — nie jako nową bazę od zera.

Na aucie we Fluencie kręć **po jednym parametrze**:

1. najpierw sensownie ustaw overlap i szczelinę (gap),  
2. potem kąty,  
3. nie podnoś main w strefę stallu — jeśli opór mocno rośnie, a docisk prawie stoi, case zabijasz.

Plan kampanii i kill: [SPEC-FLUENT-H1-RWITER017.md](SPEC-FLUENT-H1-RWITER017.md).  
Checklista pod runy: [sources/checklist-h1-fluent-rw.md](sources/checklist-h1-fluent-rw.md).  
Kandydaci geometrii / profili (bez nowych Cl na kartę): [sources/research-season-geometry-profiles.md](sources/research-season-geometry-profiles.md).  
Packaging endplate: [sources/research-rw-endplate-packaging.md](sources/research-rw-endplate-packaging.md).

### 2. Potem podłoga

Jak tył przestanie być oczywistym wąskim gardłem, bierzemy podłogę. Z literatury i notatek Źródeł sensowny start to:

- **throat** (gdzie siada peak podciśnienia — to dźwignia balansu),  
- kąt dyfuzora raczej w okolicach **~13°** pod robustness (prosta i zakręt), a nie agresywne „19° bo ładnie na wprost”,  
- potem **strakes**,  
- i **mapa yaw / ride height**, zanim zamrozicie kształt.

Nie optymalizujcie podłogi samym peakiem na prostej — Endurance zabija pakiety, które umierają w zakręcie.

Notatki: [sources/research-h2-undertray-balance-levers.md](sources/research-h2-undertray-balance-levers.md), [sources/research-h2-strakes-yaw-rideheight.md](sources/research-h2-strakes-yaw-rideheight.md).

### 3. Przednie dopiero na końcu

Przednie skrzydło i wąsy to **H3**: odciążanie przodu albo lokalne detale **dopiero gdy** tył i podłoga już ruszyły balans. Nie zaczynamy sezonu od dokręcania FW. Wąsy (np. okolice S1223) zostają kandydatem pod konkretne miejsce — nie „S1223 wszędzie”.

Notatka: [sources/research-h3-fw-unload-for-balance.md](sources/research-h3-fw-unload-for-balance.md).

---

## Jak oceniasz, czy case jest dobry

Po każdym sensownym case’ie Fluenta patrzysz na to samo (te same Aref, Lref i punkt momentu co na karcie):

- docisk nie gorszy niż dziś: |Cz| co najmniej **3,682**,  
- opór spokojny: Cx około **1,23** lub lepiej,  
- balans bliżej **48–52%** na przód niż dzisiejsze ~62%.

Jeśli opór wystrzelił albo balans poszedł jeszcze bardziej na przód — to nie jest ulepszenie, nawet gdy „ładnie wygląda na konturach”.

---

## Czego świadomie nie robimy

- **Ruchomego DRS** — tylko układ pasywny, jeśli w ogóle.  
- **Wentylatora spod podłogi** — OUT decyzją pakietu.  
- **Przenoszenia Cl z 2D OpenFOAM** na kartę auta — 2D jest zaparkowane; najwyżej kiedyś podpowie kierunek po czystym protokole.  
- **Kopiowania cudzych Cl/Cd** (AMZ, Esslingen itd.) jako naszych targetów — to najwyżej rząd wielkości / proces.  
- **Mieszania kilku dźwigni naraz** — jeden parametr na case, inaczej nie wiecie co zadziałało.

---

## Jak czytać to repo

Najpierw ta strona i [README.md](README.md), potem [SEASON-DIRECTION.md](SEASON-DIRECTION.md) i [TARGETS.md](TARGETS.md).  
[MAPA-REPO.md](MAPA-REPO.md) to spis folderów — dodatek, nie punkt startu myślenia o pakiecie.
