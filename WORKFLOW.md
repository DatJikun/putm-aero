# Co poprawić w naszym workflow aero

Krótko: jak pracować, żeby decyzje były uczciwe i żeby repo służyło jak wiki zespołu, a nie jak katalog kodu.

---

## CFD: Fluent na aucie, jeden czysty przepis

Na decyzje o bolidzie liczymy **tylko we Fluencie** (half-car, 15 m/s, Aref ok. 0,50 m², Lref 1,53 m, moment przy x = 0,765 m). OpenFOAM na całe auto i seria 2D są **poza kartą** — 2D zaparkowane; jak kiedyś wrócicie, najpierw protokół ściany i klonów siatki, dopiero potem geometria ([docs/PROTOKOL-2D-OPENFOAM.md](docs/PROTOKOL-2D-OPENFOAM.md)).

Zanim zaczniecie kręcić kątami albo gapem:

1. ustalcie **jeden przepis ściany i siatki** (y+ w sensownym zakresie wall functions, te same refine’y na LE/TE/slotach),  
2. zróbcie **2–3 poziomy tej samej topologii** (zmienia się głównie rozmiar komórki),  
3. dopiero potem serię geometrii.

Nie mieszajcie „fine bez warstw” z „medium z warstwami” i nie nazywajcie tego niezależnością siatki — to test różnych modeli dyskretyzacji, nie gęstości.

Przy raportowaniu Cl/Cd / Cx/Cz pokazujcie nie tylko „ostatnie 200 iteracji”, ale też **czy średnia usiadła** (plateau / średnia krocząca). Jeśli nadal dryfuje — oznaczcie case jako nieużywalny do decyzji.

**Jeden parametr na raz.** Overlap albo gap albo kąt — nie wszystko w jednym shotcie.

Te same **Aref, Lref i punkt momentu** w każdym case’ie, który porównujecie z RWiter017. Inaczej „lepszy Cx” może być artefaktem definicji.

---

## Dane: CSV vs interpretacja

Surowe wyniki i skrypty żyją w **`team/`** (CSV, Excel, joumale Fluent).  
Interpretacja „co to znaczy dla celów” żyje w **`TARGETS.md`** i w notatkach Spec / Źródeł w **`sources/`**.

Nie wklejajcie nowych Cl z paperów ani z 2D prosto na kartę. Najpierw claim w `sources/`, potem decyzja Speca czy to w ogóle rusza TARGETS.

---

## Repo: wiki, nie listing plików

Wejście dla człowieka ma być:

1. [README.md](README.md) — co to jest, gdzie jesteśmy, co dalej,  
2. [JAK-ULEPSZAC-PAKIET.md](JAK-ULEPSZAC-PAKIET.md) — jak ulepszać pakiet,  
3. [SEASON-DIRECTION.md](SEASON-DIRECTION.md) i [TARGETS.md](TARGETS.md) — kierunek i liczby,  
4. dopiero potem [MAPA-REPO.md](MAPA-REPO.md) jako **spis**, gdy szukacie konkretnego folderu.

INDEX i MAPA zostają — ale nie są pierwszą rzeczą, którą ktoś czyta, gdy pyta „co mam zrobić z pakietem”.

---

## Checklist przed „idziemy z tym do CAD”

- Case Fluent na aucie, nie 2D OF.  
- Ten sam setup odniesienia co baseline.  
- |Cz| nie gorsze niż 3,682; Cx spokojne; balans idzie w stronę 50/50, nie odwrotnie.  
- Zmiana geometrii jest jedna i opisana.  
- Wynik wpisany do arkusza / CSV w `team/`, a wniosek po ludzku w pokoju albo w claimie — bez ściany żargonu.
