# Workflow CFD zespołu (Fluent) + skrypty

**Źródła:** `team/workflow.txt` oraz skrypty w `team/fluent-scripts/` (`meshing.wft`, `solving.jou`, `postpro-cfdpost.txt`).

## Jak wygląda pipeline

Zespół idzie w tej kolejności:

1. SolidWorks → eksport STEP
2. SpaceClaim (model half-car)
3. Fluent Meshing
4. Fluent Solution
5. CFD-Post

To jest opisane w `workflow.txt` (pewność **wysoka**).

## Setup liczbowy (Reference Values)

- prędkość V = **15 m/s**
- długość odniesienia Lref = **1,53 m**
- moment liczony względem **x = 0,765 m**
- koła: **−72,9 rad/s**
- MRF chłodzenia: **510 rad/s** (to nie „fan car”)
- typowo **2000** iteracji

## Model turbulencji

Dziś w `solving.jou` jest **Realizable k-ε + Enhanced Wall Treatment**
(`ke-realizable? y`, `enhanced-wall-treatment? y`) — pewność **wysoka**.

Cel migracji zespołu (2026-09-01): przejście na **k-ω SST** (omega). To intent, nie jeszcze domyślny solver w arkuszach.

Skrypty trzymamy w `team/fluent-scripts/` obok Excela — to część bazy wiedzy, nie „załącznik czatu”.

## Aref (powierzchnia odniesienia)

- Aref **half-car ≈ 0,50 m²** (w simach zespołu bywa **0,49–0,51 m²**) — Mikołaj, FS Aero 2026-09-01.
- Aref pełnego bolidu ≈ **1,0 m²** (half × 2).
- Różnice Aref między największymi zmianami geometrii ≈ **±0,01 m²** na half-car.

Do porównania Fluent ↔ OpenFOAM na half-car używamy tych samych wartości:

- Aref = **0,50 m²**
- Lref = **1,53 m**
- V = **15 m/s**
- moment @ x = **0,765 m**
