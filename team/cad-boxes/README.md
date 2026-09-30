# Boxy aero FS 2027 (+ 2026 do porównania) — STEP do SolidWorksa

Parametryczny generator stref z T 8.2 / T 2.1.3 / T 2.1.4. Reguły i cytaty: [`sources/fs-rules-2027-t8.md`](../../sources/fs-rules-2027-t8.md), szare strefy: [`sources/rules-2027-aero-loopholes.md`](../../sources/rules-2027-aero-loopholes.md).

## Pliki

| Plik | Co to jest |
|------|------------|
| `out/fs2027_aero_boxes_full.step` | 2027, całe auto — złożenie z nazwanymi bryłami |
| `out/fs2027_aero_boxes_half_yneg.step` | 2027, połowa auta (y ≤ 0) — jak domena CFD |
| `out/fs2026_aero_boxes_full.step` | 2026 v1.1 — do sprawdzenia, co z obecnego auta wypada w 2027 |
| `out/limits.md` | tabela wymiarów w mm + lista brył z regułami |
| `out/preview.png` | widok z boku i z tyłu, 2027 vs 2026 |
| `params.toml` | wymiary auta (tu podmieniacie liczby) |
| `gen_boxes.py` | generator (`python3 gen_boxes.py`; wymaga `pip install cadquery matplotlib`) |

## Bryły w złożeniu

- `OK_*` — przestrzeń, w której aero może być (keep-outy już odjęte). Część aero musi się mieścić w sumie brył `OK_` swojego roku.
- `SZARA_*` — przód outboard od opon: T 8.2.2 nie ogranicza tu szerokości (loophole B3). Obcięte umownie do +300 mm.
- `KO_*` — keep-out T 2.1.3 dla **każdej** części auta (nie tylko aero). „Bez końca” obcięte do +600 mm w bok / 1500 mm w górę.
- `Q_*` — T 2.1.4 w dwóch interpretacjach: obszar, który byłby zakazany, gdyby Tech mógł ustawić prostopadłościany dowolnie (A: 75 mm wysokości, B: 250 mm). **Nie** są odjęte od `OK_` — czekamy na Q&A.
- `REF_*` — opony oraz płaszczyzny A (LE przednich opon) i HR.

## Układ współrzędnych — jak w CFD

Wymiary w **mm**; osie jak w `team/fluent-scripts/solving.jou`: **x do tyłu** (0 = oś przednia), **y w bok** (0 = symetria, półauto CFD po y < 0), **z w górę** (0 = grunt).

**SolidWorks:** File → Open → `.step`, otworzy się jako złożenie. Jeśli wasze złożenie auta ma inny początek lub oś „do góry” (domyślnie w SW to Y), wstawcie STEP jako komponent i dopasujcie go relacjami: `REF_opony_*` do kół.

## Jak sprawdzić auto

1. **Keep-out:** Tools → Evaluate → Interference Detection między częściami auta a bryłami `KO_*`. Każda kolizja = problem na Tech.
2. **Envelope aero:** dla części aero Combine → Subtract (część minus bryły `OK_`). Jeśli coś zostaje, to ten fragment wystaje poza box. Alternatywnie Interference Detection z bryłami sąsiednich stref.
3. Najpierw sprawdźcie **RWiter017 na pliku 2027**: pas „góra opony – 700 mm” ma szerokość tylko do (wewn. krawędź opony − 150 mm).

## Skąd są liczby

| Parametr | Wartość | Źródło |
|----------|---------|--------|
| Rozstaw osi | 1530 mm | `solving.jou`: oś tylnego koła x = 1.53 m, Reference Length 1.53 m |
| Promień opony | 205,74 mm (OD 411,5 mm) | `solving.jou`: oś koła z = 0.20574 m; ω = 72,9 rad/s przy 15 m/s |
| Szerokość opony | 190,5 mm | **PLACEHOLDER** |
| Rozstaw kół przód / tył | 1200 / 1200 mm | **PLACEHOLDER** (oś kół w skrypcie ma y = −0.7 m, ale dla osi równoległej do y ta wartość nic nie znaczy — nie używamy jej) |
| x płaszczyzny HR | 1000 mm | **PLACEHOLDER** |

Pewne już teraz (nie zależą od placeholderów): **środek auta 2027 < 411,5 mm** (w 2026: 500 mm), przód < 350 mm, limity długości x = −905,7 / +1985,7 mm, okno 175 mm za keep-outem tylnej opony.
Szerokości (rozpiętość RW, pas −150 mm) i długość strefy za HR zależą od placeholderów → **podmieńcie `params.toml` z CAD i przegenerujcie**.

## Uproszczenia

- Opona jako walec (bez cambera, bulge i ugięcia). T 8.2.4 wymaga spełnienia w najgorszym setupie, więc przy dużym camberze zostawcie zapas.
- Środek auta liczony pod **niższą** z gór opon przód/tył (niejasność C2).
- Przy różnym rozstawie przód/tył płaszczyzna szerokości T 8.2.2 b1 jest zbieżna (styczna do obu opon) — generator to uwzględnia.
