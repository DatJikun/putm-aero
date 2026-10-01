# Wymiary boxów (auto z params.toml)

Układ jak w CFD: x do tyłu od osi przedniej, |y| od symetrii, z od gruntu.

| Wielkość | mm |
|---|---:|
| Zapas bezpieczeństwa m (już odjęty od stref dozwolonych) | 10.0 |
| Płaszczyzna A (LE przednich opon) — x | -205.8 |
| Limit do przodu (700 mm przed oponami) — x | -905.8 |
| Limit do tyłu (250 mm za tylnymi oponami) — x | 1985.8 |
| Płaszczyzna HR — x | 1110.8 |
| Góra przedniej opony — z | 411.5 |
| Góra tylnej opony — z | 411.5 |
| Wewn. / zewn. krawędź przedniej opony — |y| | 490.0 / 700.0 |
| Wewn. / zewn. krawędź tylnej opony — |y| | 467.3 / 662.0 |
| 2027 pas góra opony–700: max |y| (wewn. tylnej − 150 − m) | 307.3 |
| 2027 700–1100: max |y| (zewn. tylnej − m) | 652.0 |
| 2027 rozpiętość RW 700–1100 (pełna, z zapasem) | 1304.0 |
| 2026 rozpiętość RW >500 (pełna, z zapasem) | 914.6 |
| Szerokość nisko (T 8.2.2 b1, tryb taper) przy x = 0 / x = limit tył | 690.0 / 640.7 |
| Okno na mocowania endplate'u (loophole A2) — długość | 155.0 |

## Bryły

| Plik | Bryła | Reguła | Objętość [dm³] |
|---|---|---|---:|
| fs2027_dozwolone | OK_2027_przod_ponizej_350 | T 8.2.1 b1 + T 8.2.3 | 287.1 |
| fs2027_dozwolone | SZARA_2027_przod_outboard_bez_limitu_szer_T822 | T 8.2.2 milczy (loophole B3) | 60.0 |
| fs2027_dozwolone | OK_2027_srodek_ponizej_gory_opon | T 8.2.1 b3 + T 8.2.2 b1 | 588.2 |
| fs2027_dozwolone | OK_2027_tyl_nisko_pelna_szer | T 8.2.1 b2 + T 8.2.2 b1 | 329.8 |
| fs2027_dozwolone | OK_2027_tyl_pas_gora_opony-700_inboard150 | T 8.2.2 b2 | 162.1 |
| fs2027_dozwolone | OK_2027_tyl_700-1100_do_zewn_opony | T 8.2.2 b3 | 423.7 |
| fs2027_zakazane | KO_2027_T213_kolo_przod | T 2.1.3 b2 (outboard bez końca, bez limitu wys.) | 473.3 |
| fs2027_zakazane | KO_2027_T213_kolo_tyl_do_700 | T 2.1.3 b2 (do 700 mm) | 292.9 |
| fs2027_zakazane | KO_2027_T213_tyl_dodatkowy_150 | T 2.1.3 b3 | 53.8 |
| fs2027_zakazane | Q_2027_T214_wariantA_obszar_75wys | T 2.1.4 — jeśli 75 mm wys. i Tech ustawia dowolnie | 73.5 |
| fs2027_zakazane | Q_2027_T214_wariantB_obszar_250wys | T 2.1.4 — jeśli 250 mm wys. i Tech ustawia dowolnie | 245.0 |
| fs2026_dozwolone | OK_2026_przod_srodek_ponizej_500 | T 8.2.1 b1 | 400.0 |
| fs2026_dozwolone | OK_2026_przod_outboard_ponizej_250 | T 8.2.1 b2 | 53.4 |
| fs2026_dozwolone | OK_2026_srodek_ponizej_500 | T 8.2.1 b1 + T 8.2.2 b1 | 637.5 |
| fs2026_dozwolone | OK_2026_tyl_ponizej_500 | T 8.2.2 b1 | 408.3 |
| fs2026_dozwolone | OK_2026_tyl_500-1100_inboard_opony | T 8.2.1 b3 + T 8.2.2 b2 | 469.2 |
