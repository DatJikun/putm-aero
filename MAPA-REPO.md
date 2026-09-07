# Mapa repozytorium putm-aero

> **To jest spis folderów**, nie przewodnik po pakiecie. Najpierw przeczytaj [README.md](README.md) i [JAK-ULEPSZAC-PAKIET.md](JAK-ULEPSZAC-PAKIET.md), potem [SEASON-DIRECTION.md](SEASON-DIRECTION.md) / [TARGETS.md](TARGETS.md). Tu wracasz, gdy szukasz konkretnego pliku.

Prosty przewodnik: **gdzie co leży** i **czego gdzie szukać**.  
Pisane pełnymi zdaniami, bez ściany skrótów.

Stan: wrzesień 2026.

---

## Od czego zacząć (kolejność czytania)

1. **[README.md](README.md)** i **[JAK-ULEPSZAC-PAKIET.md](JAK-ULEPSZAC-PAKIET.md)** — wiki start.  
2. **[SEASON-DIRECTION.md](SEASON-DIRECTION.md)** / **[TARGETS.md](TARGETS.md)**.  
3. **Ten plik** — tylko gdy szukasz folderu.  
~~3. **[SEASON-DIRECTION.md](SEASON-DIRECTION.md)**~~ — kierunek sezonu w skrócie.  
4. **[TARGETS.md](TARGETS.md)** — karta celów (liczby i kill).  
5. **[INDEX.md](INDEX.md)** — spis źródeł i zamrożonych ustaleń.  
6. Dopiero potem folder **`sources/`** albo **`team/`**, zależnie od pytania.

---

## Pliki w katalogu głównym (najważniejsze)

| Plik | Co to jest |
|------|------------|
| **TARGETS.md** | Karta celów Speca: baseline RWiter017, Cx/Cz/balans, Aref, co IN/OUT, kill. To źródło prawdy liczb zespołu. |
| **SEASON-DIRECTION.md** | Podsumowanie sezonu: kolejka H1 tylne → H2 podłoga → H3 przednie, Fluent only, otwarte tematy. |
| **SPEC-FLUENT-H1-RWITER017.md** | Plan kampanii Fluent na aucie (tylnie skrzydło): co kręcić, kill, 3-el. default / 4-el. porównanie. |
| **SPEC-H1-2D-GATE.md** | Bramka: kiedy seria **2D** OpenFOAM byłaby wiarygodna do decyzji. **Na razie zaparkowane** — nie odpalamy nowych 2D. |
| **SPEC-MORNING.md** | Krótki one-pager „stan na rano” (snapshot). |
| **SPEC-FROM-OVERNIGHT.md** | Spięcie nocnego researchu pod cele (bez nowych liczb baseline). |
| **OVERNIGHT-BRIEF.md** | Brief z nocnego researchu (RW / podłoga / yaw). |
| **INDEX.md** | Indeks całej bazy: ustalenia + lista notatek w `sources/`. |
| **index-batch-a.md** / **index-batch-b.md** | Stare indeksy cząstkowe prac dyplomowych (PUT + literatura). |
| **README.md** | Wejście do repo. |
| **MAPA-REPO.md** | Ten przewodnik. |

---

## Folder `sources/` — wiedza i claims

Tu są **notatki ze źródeł**: prace dyplomowe, papery, research zespołu agentów, checklisty i sanity-checki.  
Zasada: liczby tylko z cytatem / ścieżką do źródła — bez zgadywania.

### Ekstrakty z prac (PUT i literatura)

- `staniszewski-2023-wing.md` — tylne skrzydło wieloelementowe.  
- `staniszewski-2024-energy.md` — aero a energia / zakręty.  
- `naglowski-2024-package.md` — pakiet + wąsy.  
- `michalecki-fan-ground-effect.md` — wentylator / podłoga (u nas fan OUT).  
- `jackson-2018-cfd-drs.md` — RW + DRS (u nas DRS OUT).  
- `strojny-2015-rp.md` — druk 3D / proces (bez liczb aero).

### Ustalenia z arkuszy zespołu

- `team-rwiter017-baseline.md` — kotwica RWiter017.  
- `team-baseline002.md` — historyczny miks (nie aktualny bolid).  
- `team-fluent-workflow.md` — jak liczycie we Fluencie (V, Lref, moment…).

### Regulamin

- `fs-rules-2026-t8.md` — T8 aero, cytaty.  
- `rules-aero-boxes-loopholes.md` — boxy i szare strefy (brief).

### Research (kierunek sezonu, H1–H3, teamy)

Tu m.in.: balans i dźwignie (`research-balance-*.md`, `research-h2-*.md`, `research-h3-*.md`), overlap/gap, Endurance/energia, top EU / AMZ / Berlin / Snails, profile/geometrie sezonu (`research-season-geometry-profiles.md`), tooling rozwoju aero.

- Packaging endplate RW (H1): patrz `sources/research-rw-endplate-packaging.md`.
- H2 strakes / yaw / ride height: `sources/research-h2-strakes-yaw-rideheight.md`.
- 3 vs 4 elementy RW (teamy/papery): `sources/research-rw-3vs4-elements-teams.md`.


### Checklisty i sanity

- `checklist-h1-fluent-rw.md` — **aktywna** pod serię Fluent na aucie.  
- `checklist-h1-2d-rw-gap-aoa.md` — pod 2D (zaparkowane).  
- `sanity-cfd1-2d-rw-vs-lit.md` — porównanie starych 2D OF vs literatura (nie do karty auta).

**Czego tu szukać:** „co mówi paper / arkusz / research” — nie raw CSV i nie skrypty Fluent.

---

## Folder `team/` — dane i narzędzia zespołu

| Ścieżka | Co to jest |
|---------|------------|
| `fw-iters-*.csv`, `rw-iters-*.csv`, `ut-iters-*.csv` | Arkusze iteracji CFD (przednie / tylne / podłoga). |
| `putm-aero-sim-log.xlsx` | Log symulacji (Excel). |
| `fluent-scripts/` | Skrypty meshing / solving / postpro Fluent. |
| `rwiter017/` | Materiały wokół case’u RWiter017 (jeśli wrzucone). |
| `rules-current.pdf`, `rules-raw.txt` | Regulamin FS (PDF + tekst). |
| `workflow.txt` | Notatki o workflow Fluent. |

**Czego tu szukać:** surowe wyniki zespołu, skrypty, regulamin w oryginale.  
Interpretację liczb bierz z `sources/team-*.md` albo `TARGETS.md`, nie zgaduj z samego CSV.

---

## Folder `assumptions/`

- **ASSUMPTIONS-DRAFT.md** — wczesny szkic założeń.  
Przy konflikcie z **TARGETS.md** / **SEASON-DIRECTION.md** wygrywa Spec (karta celów i kierunek sezonu).

---

## Folder `docs/`

- **PROTOKOL-2D-OPENFOAM.md** — protokół 2D OpenFOAM: status **ZAPARKOWANE**, kolejność wall-fn → klony mesh → gap/overlap → kąty. Instrukcja na później, bez nowych runów 2D.

---


## OpenFOAM 2D (zaparkowane) — gdzie jest raport

Seria **2D tylnego skrzydła** w OpenFOAM jest **zaparkowana**. Nie odpalamy nowych runów; nie wrzucamy tych Cl/Cd do `TARGETS.md`.

Pełny raport setupu (geometria → mesh → BC → solver → post-pro + figury) leży **poza tym repo**, lokalnie na komputerze agentów:

- `/workspace/fs-rear-wing-2d-3el/RAPORT_PELNY_SETUP.md`
- oraz PDF w tym samym folderze (jeśli wygenerowany)
- obrazki: `/workspace/fs-rear-wing-2d-3el/raport_figs/`

Instrukcja na później (jak wrócicie do 2D): `docs/PROTOKOL-2D-OPENFOAM.md` + bramka `SPEC-H1-2D-GATE.md`.

**Endplate RW (packaging):** notatka Źródeł w `sources/research-rw-endplate-packaging.md` — wsparcie pod H1, nie nowe liczby na kartę.

## Czego gdzie szukać (szybkie pytania)

| Pytanie | Idź do |
|---------|--------|
| Jakie są cele Cx/Cz/balans? | `TARGETS.md` |
| Co robimy w sezonie i w jakiej kolejności? | `SEASON-DIRECTION.md` |
| Jak odpalić serię tylnego na Fluencie? | `SPEC-FLUENT-H1-RWITER017.md` + `sources/checklist-h1-fluent-rw.md` |
| Co mówi literatura / research? | `sources/` (+ `INDEX.md`) |
| Gdzie są CSV i skrypty Fluent? | `team/` |
| Co z OpenFOAM 2D? | Zaparkowane → protokół w `docs/` + raport lokalnie `fs-rear-wing-2d-3el/RAPORT_PELNY_SETUP.md` (**nie** TARGETS) |
| Endplate RW (packaging)? | `sources/research-rw-endplate-packaging.md` |
| Regulamin T8 / boxy? | `sources/fs-rules-2026-t8.md` albo `team/rules-current.pdf` |

---

## Na zapamiętanie

- **Baseline auta** = RWiter017 we **Fluencie** — nie OpenFOAM, nie 2D.  
- **Cl/Cd z paperów i z 2D** nie nadpisują karty celów.  
- DRS ruchomy i wentylator spod podłogi = **OUT**.  
- Kolejka: **tylnie skrzydło (3-el.) → podłoga → ewentualnie przednie**.
