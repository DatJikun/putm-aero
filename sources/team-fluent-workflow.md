# Workflow CFD zespołu (Fluent) + skrypty

**Źródła:** `team/workflow.txt`, `team/fluent-scripts/` (meshing.wft, solving.jou, postpro-cfdpost.txt).

## Claims

| claim | evidence | confidence |
|-------|----------|------------|
| Pipeline: SolidWorks STEP → SpaceClaim (half-car) → Fluent Meshing → Fluent Solution → CFD-Post | workflow.txt | **high** |
| V = **15 m/s**, Lref = **1,53 m**, moment @ **x = 0,765 m** | workflow.txt / Reference Values | **high** |
| Dziś: **Realizable k-ε + Enhanced Wall Treatment** | solving.jou: `ke-realizable? y`, `enhanced-wall-treatment? y` | **high** |
| Cel migracji: **k-ω SST** (omega) | decyzja zespołu FS Aero 2026-09-01 | **high** (intent) |
| Koła −72,9 rad/s; MRF chłodzenia 510 rad/s; 2000 iteracji | workflow.txt | **high** |

Skrypty trzymać w `team/fluent-scripts/` obok Excela — to część bazy wiedzy, nie „załącznik czatu”.
