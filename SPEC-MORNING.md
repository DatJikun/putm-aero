# Na rano — stan założeń (Spec)

Krótko, żeby dało się to przeczytać po kawie. Liczby bez zmian względem karty.

---

## Gdzie jesteśmy

Aktualny bolid = **RWiter017** (Fluent, 15 m/s, half-car):

- opór Cx = **1,229**
- docisk Cz = **−3,682**
- moment Cm = **−0,429**
- balans na przód ≈ **61,6%** (ok. 12 punktów do pół na pół)
- powierzchnia odniesienia Aref (half) = **0,50 m²**

Cel: **Endurance + Autocross** — dużo docisku, możliwie mały opór, balans w stronę 50/50.

---

## Co robimy / czego nie

| | |
|--|--|
| Tylne skrzydło, przednie, podłoga | tak |
| 4 elementy z tyłu | hipoteza — jeden case porównawczy obok 3-el. |
| Wąsy | jeszcze nie wiadomo |
| Ruchomy DRS | **nie** |
| Wentylator spod podłogi | **nie** |

Kolejka: **najpierw tylne skrzydło**, potem **podłoga** (też w zakręcie, nie tylko na wprost).

---

## Punkty z regulaminu (FS 2026, tabela 3 — klasa z kierowcą)

To **nie** są nasze wagi decyzyjne — to limit punktów w zawodach. Pokazuje, czemu Endurance i Autocross wygrywają rozmowę o aero:

- Endurance = **250** pkt  
- Autocross = **100** pkt  
- Efficiency = **75** pkt  
- Acceleration = **50** pkt  
- Skidpad = **50** pkt  

Suma dynamiki z aero w tle: Endurance jest największy kawałek; Efficiency dokłada wagę oporu / energii. Źródło: `team/rules-raw.txt` / Table 3.

---

## Czego nie wpuszczamy do karty

- Smoke OpenFOAM (~312k komórek, Cd≈1,22 / Cl≈−1,72) — tylko check setupu.  
- Cudze absolutne Cl/Cd z AMZ / Snails / Esslingen jako nasze targety (Esslingen najwyżej rząd wielkości).

---

## Otwarte na Ciebie

1. Wąsy — tak/nie po doborze profilu.  
2. Mapa / zdjęcie funkcji celu (obiecałeś).  
3. Lepszy eksport (IGES/OBJ) pod CFD — link nocny już poszliście; CFD#1 ogarnia.  
4. Czy na Endurance ważycie też Efficiency osobno w funkcji celu, czy „mały opór” wystarczy jako proxy.

Szczegóły: `TARGETS.md`, `SPEC-FROM-OVERNIGHT.md`.
