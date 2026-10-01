# Boxy aero FS 2027 (+ 2026 do porównania) — STEP do SolidWorksa

Parametryczny generator stref z T 8.2 / T 2.1.3 / T 2.1.4. Reguły i cytaty: [`sources/fs-rules-2027-t8.md`](../../sources/fs-rules-2027-t8.md), szare strefy: [`sources/rules-2027-aero-loopholes.md`](../../sources/rules-2027-aero-loopholes.md).

## Pliki (`out/`)

| Plik | Co to jest | Kiedy otwierać |
|------|------------|----------------|
| `fs2027_dozwolone_full.step` | **tylko** przestrzeń, w której aero może być (keep-outy odjęte, zapas 10 mm) | to jest „box” do pracy |
| `fs2027_dozwolone_half_yneg.step` | to samo, połowa auta (y ≤ 0) — jak CFD | do złożenia CFD |
| `fs2027_zakazane.step` | keep-outy kół T 2.1.3 + dwa warianty T 2.1.4 | do Interference Detection |
| `fs2026_dozwolone_full.step` | boxy 2026 v1.1 | co z obecnego auta wypada w 2027 |
| `ref_opony.step` | opony z parametrów | do dopasowania w złożeniu |
| `limits.md`, `preview.png` | tabela wymiarów, widok z boku i z tyłu | szybki podgląd |

Strefy **dozwolone i zakazane są w osobnych plikach**. SolidWorks nie wczytuje kolorów z STEP-a, więc w jednym pliku nie dałoby się ich odróżnić.

Nazwy brył: `OK_*` dozwolone · `SZARA_*` przód outboard od opon (T 8.2.2 milczy, loophole B3; obcięte do +150 mm) · `KO_*` keep-out dla **każdej** części auta · `Q_*` T 2.1.4 w interpretacji „Tech ustawia dowolnie” (A: 75 mm, B: 250 mm wysokości) · `REF_*` opony.

## Układ współrzędnych

Jak w `PM09-Model-CFD.SLDASM` i w CFD: wymiary w **mm**, **x do tyłu** (0 = oś przednia), **y w bok** (0 = symetria, półauto po y < 0), **z w górę** (0 = grunt). Wstawione do złożenia auta na początek układu wskakują na miejsce (sprawdzone na zrzucie).

## Parametry (`params.toml`) i skąd są

| Parametr | Wartość | Źródło |
|----------|---------|--------|
| Rozstaw osi | 1530 | `solving.jou` + część kolegi |
| Promień opony | 205,75 | `solving.jou` + część kolegi |
| Krawędzie przedniej opony \|y\| | 490 / 700 | część kolegi, po cofnięciu jego zapasu 10 mm (≈) |
| Krawędzie tylnej opony \|y\| | 467,3 / 662 | jw. (≈) |
| x zagłówka (HR) | 1110,75 | jw. (≈) |
| `margin` | 10 | jak u kolegi; `0` = gołe limity regulaminu |
| `width_plane_mode` | `taper` | interpretacja T 8.2.2 b1 — patrz niżej |

Wartości „≈” warto potwierdzić pomiarem w złożeniu. Po zmianie: `python3 gen_boxes.py` (wymaga `pip install cadquery matplotlib`).

## Porównanie z częścią kolegi (`ref-kolegi/REF-REGULATIONS-2027.SLDPRT`)

Wierzchołki obu modeli porównane 1:1 (z jego pliku wyciągnięta geometria Parasolid). Przy tych samych wymiarach, zapasie 10 mm i `width_plane_mode = "parallel"` modele się pokrywają, poza poniższymi różnicami:

| Miejsce | Kolega | Ten generator | Kto ma rację |
|---------|--------|---------------|--------------|
| Przejście przód → środek | x = −290,75 (początek keep-outu koła); między −290,75 a −205,75 box do **401,5 mm** | x = −195,75 (przód opony + zapas); przed nim max **340 mm** | **T 8.2.1 b1:** przed płaszczyzną przez przód opony < 350 mm → u kolegi pas 85 mm jest za wysoki |
| Wąski pas nad tylną oponą | \|y\| ≤ 316,2 | \|y\| ≤ 307,3 | oba legalne; u kolegi zapas tylko ~1 mm (467,3 − 150 = 317,3) |
| Dół / góra przodu | 35,5 / 340,5 | 30 / 340 | do wyjaśnienia, od czego kolega liczył (różnica 0,5–5,5 mm) |
| Wąski pas od wysokości | 421,5 (góra opony + 10) | 401,5 (góra opony − 10) | oba legalne; między 401,5 a 421,5 kolega nie ma żadnej strefy |
| Szerokość nisko za tylną osią | stałe 690 (`parallel`) | zbieżne 690 → 641 (`taper`) | zależy od interpretacji T 8.2.2 b1 → **Q&A** |
| T 2.1.4 | jeden box 510 × 85 na środku | dwa warianty „najgorszy przypadek” w pliku `zakazane` | interpretacja otwarta → **Q&A** |

## Jak sprawdzić auto w SolidWorksie

1. **Keep-out:** Tools → Evaluate → Interference Detection między częściami auta a `fs2027_zakazane.step`. Każda kolizja = problem na Tech.
2. **Envelope aero:** część aero musi się mieścić w sumie brył z `fs2027_dozwolone_*`. Szybki test: Combine → Subtract (część minus bryły `OK_`) — jeśli coś zostaje, to ten fragment wystaje.
3. Najpierw **RWiter017**: pas „góra opony – 700 mm” ma szerokość tylko do \|y\| = 307 mm.

## Uproszczenia

- Opona jako walec (bez cambera, bulge i ugięcia) — przy dużym camberze zostawcie większy zapas (T 8.2.4).
- Środek auta liczony pod **niższą** z gór opon przód/tył (niejasność C2).
- Prześwit 30 mm bez zapasu.
