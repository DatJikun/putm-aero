# Baseline zespołu — RW_iter017 (PUT Motorsport, CFD Fluent 2025/26)

**Kotwica:** tak — **aktualny bolid po zawodach** (decyzja Mikołaj / Aero Pack 2026-09-01). `Baseline002` nie zastępuje tej kotwicy.

**Źródło:** arkusz symulacji RW (CSV `team/rw-iters-2025-2026.csv`); kontekst balansu: log UT (`team/ut-iters-with-balance-2026.csv`).  
**Status w sheetcie:** Done · **Data:** 27.12.2025 · **Autor:** Michał Narożny  
**Model bazowy (wg CSV):** `RW_iter014/15`  
**Opis:** tylne lotki jak w RWiter015 + dwie lotki z przodu z RWiter014  

## Kluczowe liczby — TYLKO z CSV

| Wiersz | Status | Data | Cm | Cx | Cz | η (Efektywność) | CoP | CoP % | Balans Front |
|--------|--------|------|----|----|----|-----------------|-----|-------|--------------|
| **RW_iter017** | Done | 27.12.2025 | **−0,429** | **1,229** | **−3,682** | **2,996** | −0,18 | −0,12 | **brak kolumny w sheetcie RW** |
| RW_iter017.2 | Done | 05.05.2026 | −0,458 | 1,210 | −3,628 | 2,998 | −0,19 | −0,13 | brak — „Nowy skrypt do Fluenta”; wniosek: lekka rozbieżność; model do porównania z przyszłorocznym |

Uwagi:
- Konwencja znaku: w RW_iter017 Cz jest **ujemny** (docisk). W innych wierszach sheetu znak Cz bywa odwrócony — w claims używać **|Cz|** + jawny wiersz.
- **Balans % Front nie jest podany** dla RW_iter017 w CSV RW.
- V_ref: **15 m/s** (workflow). A_ref half-car: **≈ 0,50 m²** (zakres 0,49–0,51; pełny ≈ 1,0 m²) — Mikołaj 2026-09-01.

## Kontekst balansu (osobne źródło — nie mieszać jako tożsamość 1:1 bez potwierdzenia)

Z `team/ut-iters-with-balance-2026.csv`, wiersz **Baseline_1** (Done, 4.3.2026, opis „bazowy”):

| Nazwa | Cm | Cx | Cz | η | CzA_F | CzA_R | **Balans Front** |
|-------|----|----|----|---|-------|-------|------------------|
| Baseline_1 | −0,708 | 1,197 | −3,683 | 3,077 | −2,550 | −1,134 | **0,692 (≈69% przód)** |

|Cz| Baseline_1 (−3,683) jest podobny do RW_iter017 (−3,682), ale **to nie ten sam model** (potwierdzenie Mikołaja). Cm i Cx też inne. Liczb balansu z Baseline_1 (~69% przód) **nie przenosimy** na RWiter017.

## Cel użytkownika (nie liczba z CFD)

Mikołaj (FS Aero, 2026-09-01): **maksymalny downforce przy balansie ≈ 50/50**. To jest **kierunek hard targetu**, nie wynik pomiaru z RWiter017.

## Claims (claim | evidence | confidence)

| claim | evidence | confidence |
|-------|----------|------------|
| Kotwica zespołu (baseline liczbowy Cx/Cz/Cm) = **RW_iter017** | CSV RW: Done, 27.12.2025, Michał Narożny; Cx=1,229, Cz=−3,682, Cm=−0,429, η=2,996 | **high** |
| Re-run Fluent (RW_iter017.2) daje lekką rozbieżność vs 017 | CSV: Cx 1,210 / Cz −3,628 / Cm −0,458; wniosek w sheetcie o rozbieżności | **high** |
| W sheetcie RW **brak Balans Front** dla 017 | brak kolumny wartości balansu w wierszu RW_iter017 | **high** |
| UT Baseline_1 ma |Cz|≈3,683 i balans ≈**69%** przód | CSV UT: Balans Front=0,692; Cz=−3,683 | **high** (dla Baseline_1) |
| **Baseline_1 ≠ RWiter017** | decyzja Mikołaja (FS Aero 2026-09-01): RWiter017 = aktualny bolid po zawodach; Baseline_1 to inny model z arkusza podłogi | **high** |
| Hard target balansu ≈50/50 = decyzja lead, nie wynik RWiter017 | wypowiedź Mikołaja w FS Aero | **high** (jako intent); N/A jako CFD |
| Aref half-car ≈ **0,50 m²** (0,49–0,51); pełny ≈ **1,0 m²** | Mikołaj FS Aero 2026-09-01 | **high** |
| Łańcuch FW 2025/26 i FWiter039 **nie** są baseline bolidu | osobny CSV FW; decyzja Spec/Aero Pack | **high** |

## Limity

- Brak walidacji tunelowej w tych CSV.
- Znak Cz niespójny w sheetach — normalizować do |Cz| + konwencji „ujemny = DF”.
- Nie łączyć liczb Nagłowskiego (Cz≈−4,07) / PM08 (Cz≈−2,03) z RWiter017 bez mapowania A_ref / modelu.


---

## Status zamrożenia (2026-09-01)

Zamrożone w INDEX na prośbę koordynacji FS Aero:
- baseline liczbowy = **RW_iter017** (nie 017.2),
- cel = max docisk przy balansie ~50/50 (48–52% przód),
- fan OUT, DRS TBD,
- **Baseline_1 ≠ RW_iter017** (potwierdzone przez Mikołaja 2026-09-01). RWiter017 = aktualny bolid po zawodach.
- balans RWiter017 **zamrożony 2026-09-01**: ≈ **61,6% przód** z Cm/Cz arkusza (decyzja Mikołaj+Spec+Koordynator); postpro JPG bez CSV — bez zmiany kotwicy.
