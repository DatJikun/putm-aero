# Kierunek sezonu — pakiet aero

Po ludzku: gdzie jesteśmy i co robimy dalej. Liczby z karty założeń (`TARGETS.md`), bez kopiowania Cl z OpenFOAM 2D ani z innych teamów.

---

## Gdzie jesteśmy (baseline)

Aktualny bolid = **RWiter017** (Fluent, 15 m/s, half-car):

- opór **Cx ≈ 1,23** (1,229)
- docisk **Cz ≈ −3,68** (−3,682)
- balans na przód ok. **61,6%** — za mocno z przodu; do pół na pół brakuje ok. **12 punktów**
- Aref half **0,50 m²**, Lref **1,53 m**, moment przy **x = 0,765 m**

Cel nadrzędny: **Endurance + Autocross** — maksymalny docisk przy możliwie małym oporze, balans jak najbliżej **50/50**.

---

## Co jest w pakiecie / czego nie ma

| Element | Decyzja |
|---------|---------|
| Tylne skrzydło | **Tak** — najpierw to (H1) |
| Podłoga | **Tak** — druga kolejka (H2) |
| Przednie skrzydło | **Tak** — dopiero gdy trzeba odciążyć przód (H3) |
| Profil / liczba elementów RW | Domyślnie **3 elementy**; **4 elementy** tylko jako porównanie |
| Wąsy | **Otwarte** — profil pod konkretne miejsce, nie z góry |
| Ruchomy DRS | **Nie** (tylko pasywny układ) |
| Wentylator spod podłogi | **Nie** |

**Fluent only na aucie.** OpenFOAM nie służy do decyzji na bolidzie; 2D OF jest zaparkowane (protokół na później).

---

## Kolejka prac

1. **H1 — tylne skrzydło (3-el.)** we Fluencie na RWiter017  
   Kręcimy kąty / overlap / szczelinę **po jednym parametrze**.  
   Plan: `SPEC-FLUENT-H1-RWITER017.md` + `sources/checklist-h1-fluent-rw.md`.  
   Jedno porównanie **4-el.** obok najlepszego 3-el. — nie nowa baza.

2. **H2 — podłoga**  
   Cofanie docisku / efektywność, też w zakręcie (nie tylko peak na wprost).  
   Notatka: `sources/research-h2-undertray-balance-levers.md`.

3. **H3 — przednie skrzydło**  
   Tylko jeśli po H1+H2 balans nadal za bardzo z przodu.  
   Notatka: `sources/research-h3-fw-unload-for-balance.md`.

---

## Kill (czy case przechodzi)

Z `TARGETS.md` / planu Fluent:

- |Cz| **nie gorsze** niż **3,682**
- Cx **około 1,23** lub lepiej (bez świadomego trade-offu w górę)
- balans **w stronę 48–52%** na przód (nie jeszcze bardziej na przód)

Raportuj Cx, Cz, Cm, balans przy tym samym Aref / Lref / punkcie momentu.

---


## Kandydaci geometrii (ze Źródeł — bez nowych Cl na kartę)

Szczegóły: `sources/research-season-geometry-profiles.md`.

- **RW:** zostajemy przy **3-el.** jako default; profil z RWiter017 jako baza. E423 / gap–overlap z paperów = **kierunek startu** pod Fluent, nie target Cl.  
- **UT:** start od **throat + kąt dyfuzora ~13°** (robustness), potem strakes; mapa yaw/RH przed zamrożeniem.  
- **FW / wąsy:** S1223 tylko jako **kandydat** (wąsy TBD), nie „S1223 wszędzie”. H3 dopiero po H1+H2.  
- Zmiana profilu RW/FW dopiero gdy Fluent pokaże ścianę (stall / martwe sloty) — nie na podstawie 2D OF.

## Świadomie otwarte

- Ostateczna decyzja o **wąsach**
- Czy **4-el.** RW w ogóle warto po jednym porównaniu
- Mapa / wagi funkcji celu od Mikołaja (zdjęcie obiecał wcześniej)
- Walidacja tor (nitki / flow-vis) — w planie, nie w tej chwili

---

## Czego nie robimy w tym kierunku

- Nie przenosimy Cl/Cd z 2D OpenFOAM na auto  
- Nie kopiujemy cudzych Cl/Cd (AMZ, Esslingen itd.) jako naszych targetów  
- Nie odpalamy powered ground effect / fan / ruchomego DRS  

---

*Aktualizacja: wrzesień 2026. Źródło prawdy liczb: `TARGETS.md`.*
