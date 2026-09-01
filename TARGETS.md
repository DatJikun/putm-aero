# Karta targetów — pakiet aero FS

**Status:** zaktualizowana po decyzjach Mikołaja  
**Data:** 2026-09-01  
**Prędkość odniesienia w CFD:** 15 m/s  

Fluent (zespół): half-car, długość odniesienia Lref = 1,53 m, moment przy x = 0,765 m.  
Dziś w solverze: k-ε realizable + Enhanced Wall Treatment.  
Cel migracji / porównania: uzgodnić z OpenFOAM (u CFD#1 przy 16 GB: funkcje ściankowe, y+ > 30).  
**Aref (powierzchnia odniesienia):** half-car ≈ **0,50 m²** (zakres simów 0,49–0,51); pełny bolid ≈ **1,0 m²**. Do porównania OpenFOAM ↔ Fluent bierzemy **0,50 m²** na half-car.

---

## Kotwica: aktualny bolid = RWiter017

| Wielkość | Wartość | Uwagi |
|----------|---------|--------|
| Cx | 1,229 | Done, 27.12.2025 |
| Cz | −3,682 | ujemny = docisk |
| Cm | −0,429 | |
| Efektywność \|Cz\|/Cx | ok. 3,0 | |
| Balans na przód | ok. **61,6%** | Z arkusza (Cm/Cz); do pół na pół brakuje ok. **12 punktów procentowych** |

Wariant RW_iter017.2 (Cx 1,210 / Cz −3,628) to tylko sprawdzenie skryptu — nie zamienia kotwicy.

Baseline002 (FWiter011 + RWiter017 + UTiter002) to **historyczny miks**, nie aktualny bolid.

---

## Cel nadrzędny

**Endurance i Autocross** są najważniejsze.  
Maksymalny docisk przy **możliwie najniższym oporze**, balans jak najbliżej pół na pół.

| Cel | Wartość robocza |
|-----|-----------------|
| Docisk | \|Cz\| co najmniej **3,682** (nie gorzej niż RWiter017) |
| Opór | Cx możliwie niski; orientacyjnie nie gorzej niż ok. **1,23** przy tym docisku |
| Balans | pasmo **48–52%** na przód; dziś ok. **61,6%** → trzeba **cofnąć docisk** o ok. 12 pp (tylnie skrzydło / podłoga), nie dokręcać samego przedniego na ślepo |
| Prędkość CFD | **15 m/s** |

---

## Zakres elementów (decyzje)

| Element | Status |
|---------|--------|
| Tylne skrzydło | **IN** — rozważamy **4 elementy** (hipoteza; w literaturze PUT często 3) |
| Przednie skrzydło | **IN** |
| Podłoga (+ sekcje boczne) | **IN** |
| Wąsy (np. S1223) | **TBD** — profil dobierać pod konkretne miejsce na aucie, nie z góry |
| Ruchomy DRS | **OUT** — tylko układ pasywny |
| Wentylator spod podłogi | **OUT** |

---

## Shortlista pracy nad balansem (zatwierdzona)

1. **H1** — tylne skrzydło (w tym wariant 4-elementowy)  
2. **H2** — podłoga (i bramka: Cx/Cz nie tylko na wprost, też pod kątem / model toru Endurance)  
3. **H3** — odciążenie przodu tylko gdy trzeba  
4. **H4** — wąsy później, jeśli TBD przejdzie w „tak”  
5. **H5** — DRS i fan poza grą przy peaku docisku  

Szczegóły: `sources/research-balance-shift.md`, `sources/research-balance-levers-h1-h5.md`.

---

## Co znaczy „mapa CFD + model toru jako bramka”

Zanim zamrozicie geometrię **podłogi**, warto policzyć opór i docisk nie tylko jadąc prosto, ale też przy kątach jak w zakręcie, i złożyć to na prosty model toru Endurance. Podłoga lubi tracić docisk w yaw — bez tej bramki można „wygrać prostą” i przegrać Endurance.

---

## Plan walidacji (Wasze słowa)

1. CFD  
2. Symulacja (sim)  
3. Tor — nitki, ewentualnie flow-vis  

---

## RP 1:10 (opcjonalnie, proces)

To nie jest CFD. Chodzi o wydrukowany model bolidu w skali 1:10 przed formami kompozytowymi — łapie kolizje ramy, zawieszenia, packagingu. Pomysł ze Strojnego; nie obowiązek aero.

---

## Regulamin (FS Rules 2026 v1.1, T8) — skrót

Szczegóły z cytatami: `sources/fs-rules-2026-t8.md`.

- Boxy urządzeń aero według T 8.2 — twarde ograniczenia.  
- DRS: w T8 nie zakazany wprost, ale u nas **OUT** decyzją zespołu.  
- Wentylatory: w regulaminie limit mocy, u nas i tak **OUT**.  
- Skrzynka 800×500 mm u CFD#1 to domena numeryczna skrzydła, nie box z regulaminu.

---



## Kotwice z researchu top EU FS EV (literatura publiczna)

Źródła: `sources/research-eu-fs-ev-top-teams.md`, `sources/claims-from-eu-fs-ev-top.md`.

- Po zakazach powered ground effect wygrywa **pasywny high-DF** — spójne z naszym DRS/fan OUT.
- **Podłoga** to główna dźwignia efektywności (obok RW) przy cofaniu balansu — wzmacnia H2.
- Jedyny publiczny rząd CLA/CDA w tym researchu: **Esslingen ≈ 4,9 / 1,65** — sanity check, **nie** hard target (inne Aref/konwencje).
- Multi-element RW jest standardem; **4 elementy bez publicznych liczb** — nasza hipoteza, nie fakt z rankingów.
- Autocross ≠ sukces sezonu bez Endurance (ostrzeżenie Aachen) — bramka mapa w zakręcie + model toru zostaje.
- Brak publicznych Cl/Cd/balansu od AMZ / Aachen / Delft itd. — nie wymyślamy ich liczb.

## Otwarte / potrzebne od zespołu

1. ~~Aref~~ — zamknięte: half ≈ 0,50 m² (pełny ≈ 1,0 m²).
2. Ostateczna decyzja o wąsach po doborze profilu.  
3. Zdjęcie / mapa aero do funkcji celu (Mikołaj: „zaraz podeślę”).


## Aref

- Half-car: **≈ 0,50 m²** (zakres 0,49–0,51 m²)
- Pełny bolid: **≈ 1,0 m²**
- Źródło: Mikołaj, FS Aero 2026-09-01
