# Karta targetów — pakiet aero FS

**Status:** robocza (RWiter017 = aktualny bolid; Baseline002 ≠ aktualny)  
**Data:** 2026-09-01  
**V odniesienia:** 15 m/s  
**Fluent (zespół):** half-car, Lref 1,53 m, moment przy x=0,765 m, Realizable k-ε + EWT, koła −72,9 rad/s · **cel migracji:** k-ω SST

## Punkt odniesienia (aktualny bolid)

### RW_iter017 — jedyna kotwica bolidu
| Wielkość | Wartość |
|----------|---------|
| Cx | 1,229 |
| Cz | −3,682 |
| Cm | −0,429 |
| η ≈ | 3,0 |

Źródło: arkusz RW / `sources/team-rwiter017-baseline.md`.  
`RW_iter017.2` = wariant skryptu Fluent — nie zamienia kotwicy.

### Baseline002 — NIE aktualny bolid
Połączenie FWiter011 + RWiter017 + UTiter002 (historyczny miks).  
Cx ≈ 1,187, |Cz| ≈ 3,678, balans przód ≈ **69%** (po korekcie znaku w Excelu).  
Używać tylko jako **kontekst** (jak mierzono balans / formuły), **nie** jako baseline osiągów ani startowy balans aktualnego auta.

Baseline_1 z arkusza UT też **nie** jest RWiter017.

## Cele twarde

1. **Maksymalny docisk** przy spokojnym oporze: |Cz| ≥ **3,682** (nie gorzej niż RWiter017).
2. **Opór:** Cx ≲ **1,23** przy tym DF.
3. **Balans:** jak najbliżej **50/50** (48–52% przód). Startowy % dla samego RWiter017 w arkuszu RW **brak** — do zmierzenia w postpro. Jeśli pełny pakiet zachowuje się jak Baseline002 (~69% przód), kierunek to **cofać DF** (RW/UT).
4. **Prędkość CFD:** 15 m/s.

## Cel nadrzędny (słowa Mikołaja)

Maksymalny docisk przy spokojnym oporze, balans jak najbliżej pół na pół.

## Zakres elementów

- **IN:** RW, FW, UT (+ sekcje boczne)
- **Kandydat:** wąsy
- **OUT:** wentylator spod podłogi
- **TBD:** DRS

## Co dalej

1. Repo wiedzy (`putm-aero`) — ta paczka.
2. Research: cofanie balansu → ~50/50 przy |Cz| ≥ 3,682 i Cx ≲ 1,23.
3. CAD RWiter017 → CFD (Fluent/OF), gdy będzie plik; zmierzyć balans aktualnego bolidu.

## Otwarte

- % balansu aktualnego bolidu (RWiter017 / pełny model po zawodach)
- DRS (regulamin)
- Masa, energia / model toru
- Konwencja znaku balansu w Excelu
