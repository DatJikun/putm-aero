# Karta targetów — pakiet aero FS

**Status:** robocza  
**Data:** 2026-09-01  
**V odniesienia:** 15 m/s  
**Fluent (zespół):** half-car, Lref 1,53 m, moment przy x=0,765 m; solving dziś ke-realizable+EWT; cel migracji: k-ω SST

## Kotwica: aktualny bolid = RWiter017

| Wielkość | Wartość | Uwagi |
|----------|---------|--------|
| Cx | 1,229 | Done, 27.12.2025 |
| Cz | −3,682 | ujemny = docisk |
| Cm | −0,429 | |
| η ≈ | 3,0 | |
| Balans przód | **≈ 61,6%** | Z arkusza / Cm÷Cz (−0,429/−3,682); ~11–12 pp do 50/50. Postpro może doprecyzować. |

RW_iter017.2 (Cx 1,210 / Cz −3,628) = tylko wariant skryptu, nie zamienia kotwicy.

## Baseline002 — nie jest aktualnym bolidem

Historyczny miks FWiter011 + RWiter017 + UTiter002 (Cx ≈ 1,187, |Cz| ≈ 3,678). Po poprawie znaku w Excelu balans wychodzi **ok. 69% przód** — to informacja o *tym* miksie, **nie** o samym RWiter017. Nie używać jako hard baseline.

## Cele (słowa Mikołaja)

Maksymalny docisk przy spokojnym oporze, balans jak najbliżej **50/50**.

| Cel | Wartość robocza |
|-----|-----------------|
| Docisk | \|Cz\| ≥ **3,682** (nie gorzej niż RWiter017) |
| Opór | Cx ≲ **1,23** przy tym DF |
| Balans | **48–52%** przód; dziś ≈ **61,6%** → cofnąć o **~11–12 pp** (RW/UT) |
| V CFD | **15 m/s** |

Kierunek: **cofamy docisk o ~12 pp** (RW / podłoga), bez dokręcania samego FW na ślepo.

## Zakres elementów

- **IN:** RW, FW, undertray (+ sekcje boczne)
- **Kandydat:** wąsy
- **OUT:** wentylator
- **TBD:** DRS

## Kolejność

1. Push wiedzy do `putm-aero` (w toku)
2. Balans RWiter017 zamrożony ≈61,6% przód (arkusz); postpro może doprecyzować
3. Research: max DF + spokojny Cx + balans → 50/50
4. CAD → CFD porównawcze

## Ograniczenia regulaminu (FS Rules 2026 v1.1, T8) — skrót

Źródło: `sources/fs-rules-2026-t8.md` / `sources/rules-aero-boxes-loopholes.md` (nie zgadywać poza cytatami).

- Boxy urządzeń aero wg T 8.2 (m.in. FW wysokości / outboard przed osią; RW wysokość; szerokość vs opony; zasięg wzdłużny ±700 mm przód / +250 mm tył) — szczegóły w notatkach KB.
- **DRS:** w T8 nie zakazany wprost → decyzja Spec = **TBD** (Q&A / decyzja zespołu).
- **Wentylatory:** legalnie ≤ 500 W łącznie (T 11.11.1), ale w pakiecie **OUT** (decyzja projektowa).
- Uwaga: skrzynka CFD 800×500 mm (endplate) u CFD#1 to domena numeryczna, **nie** box T8.


---

## Aktualizacja decyzji (2026-09-01, Mikołaj)

- **DRS ruchomy: OUT** (ew. tylko pasywny)
- **Fan spod podłogi: OUT**
- **Wąsy S1223: TBD** — dobór profilu pod konkretne miejsce
- **Priorytet:** Endurance + Autocross
- **Cel:** max docisk przy możliwie niskim oporze
- **Balans start:** ≈61,6% przód → cel ~50/50 (~12 pp)
- **RW:** rozważyć **4 elementy**
- **Walidacja:** CFD → symulacja → tor (nitki / flow-vis)
- **Aref:** nadal wymagane z Fluent Reference Values przed porównaniem OF↔Fluent
