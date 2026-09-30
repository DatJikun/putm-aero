# Wymiary boxów (auto z params.toml)

Układ jak w CFD: x do tyłu od osi przedniej, |y| od symetrii, z od gruntu.

| Wielkość | mm |
|---|---:|
| Płaszczyzna A (LE przednich opon) — x | -205.7 |
| Limit do przodu (700 mm przed oponami) — x | -905.7 |
| Limit do tyłu (250 mm za tylnymi oponami) — x | 1985.7 |
| Płaszczyzna HR — x  [PLACEHOLDER] | 1000.0 |
| Góra przedniej opony — z | 411.5 |
| Góra tylnej opony — z | 411.5 |
| Wewn. krawędź przedniej opony — |y| | 504.8 |
| Zewn. krawędź przedniej opony — |y| | 695.2 |
| Wewn. krawędź tylnej opony — |y| | 504.8 |
| Zewn. krawędź tylnej opony — |y| | 695.2 |
| 2027 pas góra opony–700: max |y| (wewn. − 150) | 354.8 |
| 2027 700–1100: max |y| (zewn. tylnej opony) | 695.2 |
| 2026 >500: max |y| (wewn. tylnej opony) | 504.8 |
| 2027 rozpiętość RW 700–1100 (pełna) | 1390.5 |
| 2026 rozpiętość RW >500 (pełna) | 1009.5 |
| 2027 keep-out tylnej opony — x od | 1249.3 |
| 2027 keep-out tylnej opony — x do | 1810.7 |
| Okno na mocowania endplate'u (loophole A2) — długość | 175.0 |

## Bryły

| Bryła | Reguła | Objętość [dm³] |
|---|---|---:|
| OK_2027_przod_ponizej_350 | T 8.2.1 b1 + T 8.2.3 | 302.3 |
| SZARA_2027_przod_outboard_bez_limitu_szer_T822 | T 8.2.2 milczy (loophole B3) | 120.0 |
| OK_2027_srodek_ponizej_gory_opon | T 8.2.1 b3 + T 8.2.2 b1 | 568.9 |
| OK_2027_tyl_nisko_pelna_szer | T 8.2.1 b2 + T 8.2.2 b1 | 441.3 |
| OK_2027_tyl_pas_gora_opony-700_inboard150 | T 8.2.2 b2 | 201.8 |
| OK_2027_tyl_700-1100_do_zewn_opony | T 8.2.2 b3 | 548.3 |
| KO_2027_T213_kolo_przod | T 2.1.3 b2 (outboard bez końca, bez limitu wys.) | 1331.5 |
| KO_2027_T213_kolo_tyl_do_700 | T 2.1.3 b2 (do 700 mm) | 621.4 |
| KO_2027_T213_tyl_dodatkowy_150 | T 2.1.3 b3 | 48.6 |
| Q_2027_T214_wariantA_obszar_75wys | T 2.1.4 — jeśli 75 mm wys. i Tech ustawia dowolnie | 73.0 |
| Q_2027_T214_wariantB_obszar_250wys | T 2.1.4 — jeśli 250 mm wys. i Tech ustawia dowolnie | 243.3 |
| OK_2026_przod_srodek_ponizej_500 | T 8.2.1 b1 | 429.7 |
| OK_2026_przod_outboard_ponizej_250 | T 8.2.1 b2 | 52.4 |
| OK_2026_srodek_ponizej_500 | T 8.2.1 b1 + T 8.2.2 b1 | 603.3 |
| OK_2026_tyl_ponizej_500 | T 8.2.2 b1 | 543.7 |
| OK_2026_tyl_500-1100_inboard_opony | T 8.2.1 b3 + T 8.2.2 b2 | 597.1 |
| KO_2026_T213_kolo_przod | T 2.1.3 | 320.9 |
| KO_2026_T213_kolo_tyl | T 2.1.3 | 320.9 |
