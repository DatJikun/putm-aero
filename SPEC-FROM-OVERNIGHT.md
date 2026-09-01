# Co nocny research zmienia w celach (Spec)

Bez nowych liczb baseline. RWiter017, Aref 0,50 m², DRS OUT, wentylator OUT — bez zmian.

## Co przyjmuję do pracy

**Tylne skrzydło (pierwsza dźwignia).**  
W literaturze FS domyślny układ high-docisk to nadal **trzy elementy**. **Cztery elementy** zostają hipotezą CAD w limicie regulaminu — robimy jeden case porównawczy 3 vs 4 na naszym aucie, **nie** kopiujemy Cl/Cd z Aveiro ani LUT. Najpierw seria kątów / szczelin / overlap na **trzech** elementach przy RWiter017 (pilnując Cx ≈ 1,23 i |Cz| ≥ 3,682), równolegle lekki wariant 4-elementowy do jednego porównania.

**Podłoga (druga dźwignia).**  
Podłoga mocno reaguje na jazdę w zakręcie, ale nadal pomaga w docisku i (u Staniszewskiego) w proxy energii. Zanim zamrozimy kształt podłogi: policzyć nie tylko jazdę na wprost, ale też co najmniej **jeden–dwa kąty** jak w zakręcie i złożyć to na prosty obraz toru Endurance. Nie optymalizujemy samego peaku na prostej.

**Balans.**  
Nadal: z ~62% na przód w stronę pół na pół przez **tył i podłogę**, nie przez dokręcanie samego przedniego skrzydła.

**Czego nie wpuszczam do karty**

- Żadnych Cx/Cz z OpenFOAM na rzadkiej / dziurawej siatce.
- Żadnych liczb Cl/Cd z innych teamów jako naszych targetów (inne powierzchnie, prędkości, geometrie).
- Aktywnego DRS — zostaje OUT; „pasywny low-drag” to osobna decyzja później, nie teraz.


## Top teamy (AMZ / FaSTTUBe / Running Snail) — co biorę do założeń

Źródło: `sources/research-amz-berlin-snails-aero.md` (same publiczne fakty).

- **FaSTTUBe** = Berlin (nie „Equipe/FU Berlin”).
- **AMZ:** dużo CFD (NX + STAR-CCM+) i tunel (RUAG); publicznie Δ docisku ok. **+25%** vs poprzedni pakiet — bez absolutnego Cl/Cd. Wniosek procesowy: iteracje + walidacja, nie jeden shot.
- **Running Snail:** nowe aero RS25 + druk 3D; **brak** publicznych Cl/Cd.
- **Esslingen** nadal jedyny publiczny rząd: CL·A ≈ **4,9** / CD·A ≈ **1,65** @ 50 km/h — tylko orientacja, **nie** nasz target.
- To **wspiera** kolejność tylne skrzydło → podłoga oraz DRS/fan OUT. **Nie** wpuszczam cudzych Cl/Cd do karty targetów.

## Kolejka (gdy Mikołaj wróci)

1. Fluent: seria tylnego skrzydła 3-el. na bazie 017 (kąty / gap / overlap) pod cele z karty.  
2. Równolegle: jeden wariant CAD 4-el. do porównania.  
3. Potem podłoga: prosta + 1–2 punkty w zakręcie.  
4. OpenFOAM: dopiero gdy będzie sensowna geometria i siatka — na razie tylko check setupu.

Szczegóły i cytaty: `OVERNIGHT-BRIEF.md` oraz notatki w `sources/research-overnight-*.md` i `research-papers-rw-ut-yaw-clcd.md`.
