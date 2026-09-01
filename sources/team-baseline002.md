# Baseline zespołu — Baseline002 (pełny pakiet z balansem)

**Źródło:** natywny Excel `team/putm-aero-sim-log.xlsx`, arkusz **Baseline**, wiersz **Baseline002** (formuły + wartości).  
**Autor w sheetcie:** Mikołaj Wojnowski  
**Opis:** „Baseline002, połączenie **FWiter011**, **RWiter017**, **UTiter002**”  
**Status:** NIE aktualny bolid — historyczny miks FWiter011+RWiter017+UTiter002. Aktualny bolid = **RW_iter017** (decyzja 2026-09-01).

## Workflow Fluent

Z `team/workflow.txt` oraz skryptów w `team/fluent-scripts/`:

| Etap | Plik | Uwagi |
|------|------|--------|
| Meshing | `meshing.wft` | Fluent Meshing workflow |
| Solving | `solving.jou` | dziś: **`ke-realizable` + Enhanced Wall Treatment** |
| Postpro | `postpro-cfdpost.txt` | CFD-Post |

Setup (workflow + jou):
- połowa bolidu, inlet **15 m/s**
- Length ref **1,53 m**, Velocity **15 m/s**
- moment Cm względem **x = 0,765 m**
- koła **−72,9 rad/s**; ziemia/sky ruchome 15 m/s
- MRF chłodzenia **510 rad/s** (to nie „fan car”)
- **Cel migracji modelu:** z Realizable k-ε + EWT na **k-ω SST** (omega) — decyzja zespołu 2026-09-01

## Liczby surowe z wiersza Baseline002

| Wielkość | Wartość | Uwagi |
|----------|---------|--------|
| Cm | **−0,670** | |
| Cx | **1,187** | |
| Cz w Excelu | **+3,678** | w arkuszu Baseline docisk jest **dodatni** |
| Efektywność | **≈ 3,099** | |
| CzA_F (formuła) | `=Cz/2+Cm` → 1,169 | |
| CzA_R (formuła) | `=Cz/2−Cm` → 2,508 | |
| Komórka „Balans Front” | `=CzA_F/Cz` → **0,318** | przy **dodatnim** Cz ta liczba jest **odwrócona** względem klasycznej konwencji ujemnego Cz |

## Jak czytać balans (ważne)

Formuły w Excelu zakładają de facto rozdział momentu przy danym znaku Cz. Przy **ujemnym** Cz (docisk w dół, jak w arkuszu RW: Cz=−3,682) ten sam wzór daje balans przodu ≈ **68–69%**.

**Decyzja zespołu (Mikołaj / Spec / Aero Pack, 2026-09-01):** prawdziwy balans Baseline002 to **około 69% na przód**. Jesteśmy **za mocno z przodu**. Cel ~50/50 = **cofać docisk** (tylnie skrzydło / podłoga), **nie** dokładać samego przedniego skrzydła.

Surowa komórka 0,318 zostaje w claims jako „wartość w sheetcie przy dodatnim Cz” — do interpretacji zawsze podawać **~69% przód**.

## Claims

| claim | evidence | confidence |
|-------|----------|------------|
| Skład Baseline002 = FWiter011 + RWiter017 + UTiter002 | opis wiersza Baseline | **high** |
| Cx ≈ **1,187**, \|Cz\| ≈ **3,678**, Cm ≈ **−0,670** | Excel Baseline002 | **high** |
| Balans przód ≈ **69%** (aktualna interpretacja zespołu) | 1−0,318 przy dodatnim Cz / równoważnie wzór przy Cz\<0; decyzja Spec+Aero Pack+Mikołaj | **high** (intent + konsystencja znaku); **med** dopóki Excel nie dostanie poprawionej formuły |
| Kierunek korekty: **cofać DF** (RW/UT) do ~50/50 | TARGETS.md + decyzja Spec | **high** |
| Dziś solver: Realizable k-ε + EWT | `solving.jou`: `ke-realizable? y`, `enhanced-wall-treatment? y` | **high** |
| Cel migracji: **k-ω SST** | wypowiedź Mikołaja + Aero Pack w FS Aero | **high** (jako intent) |
| Setup: 15 m/s, Lref 1,53 m, moment @ 0,765 m, half-car | workflow.txt | **high** |

## Limity

- Formuła „Balans Front” w Excelu przy dodatnim Cz myli odczyt (pokazuje ~32% zamiast ~69%) — nie cytować 31,8% jako front bez komentarza o znaku.
- `Baseline_Szczegóły` dla Baseline002 puste.
- Baseline_1 z CSV UT to **inny** model.
