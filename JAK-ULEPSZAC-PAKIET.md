# Jak ulepszać pakiet aerodynamiczny

To nie jest katalog plików. To kolejność pracy: **co ruszać, w jakiej kolejności i po co**, żeby dojść od dzisiejszego bolidu do lepszego pakietu pod Endurance i Autocross.

**Liczby z karty celów** ([TARGETS.md](TARGETS.md)) to nasze targety.  
**Liczby z paperów** poniżej to tylko cytaty / kierunek — **nie** nowe cele Cx/Cz.

---

## Gdzie jesteśmy

Jedziemy na **RWiter017** we Fluencie (15 m/s, half-car). Dziś mamy mniej więcej:

- opór Cx ≈ **1,23**
- docisk Cz ≈ **−3,68**
- balans na przód ok. **62%** — za mocno z przodu

Chcemy **więcej użytecznego docisku** przy możliwie małym oporze i balansie bliżej **pół na pół** (ok. 50/50). Brakuje nam ok. **dwunastu punktów procentowych** w tył — czyli trzeba **cofnąć docisk** (tylnie skrzydło i podłoga), a nie dokręcać samego przedniego na ślepo.

Szerszy obraz sezonu: [SEASON-DIRECTION.md](SEASON-DIRECTION.md).

---

## 1. Tylne skrzydło najpierw (domyślnie trzy elementy)

Zaczynamy od tylnego, bo to najprostsza dźwignia „więcej tyłu” przy naszym starcie z przodu. Domyślna ścieżka to **trzy elementy** na bazie 017, z **zamrożonym endplate** na czas serii kątów i slotów. **Cztery elementy** — najwyżej jedno porównanie obok najlepszego 3-el., nie nowa baza.

Na aucie we Fluencie kręć **po jednym parametrze**, w tej kolejności:

1. kąty main / klap,  
2. overlap,  
3. gap (szczelina),  
4. dopiero potem 1–2 warianty endplate (packaging), gdy sloty już mają sens.

**Z literatury (cytaty, nie targety):** Staniszewski w 2D izolowanym używał kroków rzędu main **1,5°**, klapy **2°**, overlap **10 mm**, gap **+5 / +10 mm**; u niego overlap **−30 mm** był najlepszy, a **−40 mm** już gorszy. Jackson ostrzega przed pchaniem w stall — u niego overall ok. **22,8°** było optimum, stall ok. **25°** (inna geometria, inne auto). Szczegóły: [sources/research-h1-overlap-gap-deep-dive.md](sources/research-h1-overlap-gap-deep-dive.md), [sources/research-season-geometry-profiles.md](sources/research-season-geometry-profiles.md), [sources/research-rw-endplate-packaging.md](sources/research-rw-endplate-packaging.md).

**Kill na RW:** Cx rośnie mocno **bez** zysku |Cz| (ścieżka stall / zły AOA) — case odpada, nawet jeśli „ładnie wygląda”.

Plan kampanii: [SPEC-FLUENT-H1-RWITER017.md](SPEC-FLUENT-H1-RWITER017.md).  
Checklista: [sources/checklist-h1-fluent-rw.md](sources/checklist-h1-fluent-rw.md).

---

## 2. Potem podłoga

Jak tył przestanie być oczywistym wąskim gardłem, bierzemy podłogę.

Najpierw **throat** (gdzie siada peak podciśnienia — to dźwignia balansu) i **kąt dyfuzora**. Z Chalmersa (cytat): wybrali **13°** zamiast **19°**, bo lepiej trzyma się na prostej, hamowaniu i w zakręcie — nie dlatego, że 13° daje absolutne maksimum w jednym punkcie. Dopiero potem **strakes / side floors**. Przed zamrożeniem kształtu zróbcie **mapę yaw / ride height**.

**Ostrzeżenie z cudzego auta (nie nasze Δ%):** Lisboa raportuje rozrzut rzędu ok. **20%** −CL·A przez ride height i ok. **16%** DF przez yaw — czyli podłoga lubi umierać poza „ładnym” punktem na wprost. Szczegóły: [sources/research-h2-undertray-balance-levers.md](sources/research-h2-undertray-balance-levers.md), [sources/research-h2-strakes-yaw-rideheight.md](sources/research-h2-strakes-yaw-rideheight.md).

Nie optymalizujcie podłogi samym peakiem na prostej — Endurance to zabija.

---

## 3. Przednie dopiero na końcu

**H3** to odciążenie **przedniego skrzydła** — ruszacie je **dopiero gdy** po RW + podłodze balans nadal siedzi wyraźnie powyżej ok. **52%** na przód. Odciążanie FW może cofnąć balans, ale łatwo przy okazji zjeść całe |Cz| — dlatego to ostatnia dźwignia, nie pierwsza. **Wąsy** zostają osobno (później / TBD, H4), nie w tej samej serii co H3.

**S1223** z literatury to kandydat pod wąsy / lokalne detale FW, **nie** baseline całego przedniego. Notatka: [sources/research-h3-fw-unload-for-balance.md](sources/research-h3-fw-unload-for-balance.md).

---

## Jak oceniasz, czy case jest dobry (nasza karta)

Po każdym sensownym case’ie Fluenta, przy tych samych Aref / Lref / punkcie momentu co na karcie:

- |Cz| co najmniej **3,682**,  
- Cx około **1,23** lub lepiej,  
- balans bliżej **48–52%** na przód niż dzisiejsze ~62%.

Raportujcie **ΔCx / ΔCz / Δbalans**, a nie tylko jeden „ładny” peak. Patrzcie też na Cp i separację — sam współczynnik bez obrazu przepływu łatwo okłamuje.

Jeśli opór wystrzelił albo balans poszedł jeszcze bardziej na przód — to nie jest ulepszenie.

---

## Cztery poprawki workflow (żeby seria miała sens)

1. **Parametryczny CAD** i jedna wspólna tabela case’ów / hipotez (co zmieniliście i po co).  
2. **Jeden zamrożony setup** Fluent na serię: Aref, znaki, siatka / wall treatment — bez mieszania przepisów między punktami.  
3. Raportujcie **delty i fizykę** (Cp, stall), nie pojedynczy absolut wyjęty z kontekstu.  
4. Po CFD: **nitki / flow-vis**, później tor lub tunel — sama siatka nie zamyka tematu.

Z procesu AMZ bierzemy **kulturę iteracji** (dużo CFD + tunel), **nie** ich Cl. Notatka: [sources/research-amz-berlin-snails-aero.md](sources/research-amz-berlin-snails-aero.md).  
Więcej o workflow w repo: [WORKFLOW.md](WORKFLOW.md).

---

## Czego świadomie nie robimy

- ruchomego DRS,  
- wentylatora spod podłogi,  
- przenoszenia Cl z 2D OpenFOAM na kartę auta,  
- kopiowania cudzych Cl/Cd jako naszych targetów,  
- mieszania kilku dźwigni w jednym case’ie.

---

## Jak czytać to repo

Najpierw [README.md](README.md) i ta strona, potem [SEASON-DIRECTION.md](SEASON-DIRECTION.md) i [TARGETS.md](TARGETS.md).  
[MAPA-REPO.md](MAPA-REPO.md) to spis folderów — dodatek, gdy szukasz konkretnego pliku.
