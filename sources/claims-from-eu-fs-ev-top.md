# Claims do założeń — z researchu top EU FS EV

**Źródło notatki:** [research-eu-fs-ev-top-teams.md](research-eu-fs-ev-top-teams.md) (Aero Koordynator, 2026-09-01).

Tu tylko to, co da się przełożyć na założenia Spec — bez marketingu.
Liczby wyłącznie cytowane.

## Co wynika z topowych teamów EU (EV)

1. Po banach powered ground effect top EU wraca do **pasywnego** high-docisku (skrzydła + podłoga).
   To spójne z naszym fan OUT. Pewność kierunku: **wysoka** (AMZ redesign po banie).

2. **Podłoga** jest kluczową dźwignią efektywności i dużego udziału docisku.
   Cologne mówi o „most efficient”; Kirchberger szacuje udział UT ok. **40%** DF. Pewność: **wysoka**.

3. Jedyna świeża publiczna para „siłowa” od teamu EU w tej rundzie pochodzi z Esslingen:
   - CL·A = **4,9**
   - CD·A = **1,65**
   - warunki: **50 km/h** cornering (rennstall-esslingen.com, Stallardo25)
   To są wielkości **×A**, nie nasze Cx/Cz. Pewność cytatu: **wysoka**.

4. Kirchberger (TU Wien EDGE14):
   - CLA ≈ **4,66–5,2 m²**
   - CDA ≈ **1,51–1,72 m²**
   - A ≈ **1,19 m²**
   - inlet **15 m/s**
   - CFD często **nadmiarowe** względem toru (teza 2023). Pewność: **wysoka**.

5. Top teamy robią **multi-element RW**.
   Publicznych liczb dla **4 elementów** u top EU w tej sesji **nie ma** — nadal hipoteza CAD PUT.
   Revolve pokazuje 3-el. w tunelu; Jackson i Staniszewski też 3-el. Pewność „braku liczb 4-el.”: **wysoka**.

6. Praktyka top: **mapy aero** (ride height / rake / yaw), nie tylko jeden punkt przy δ = 0.
   Dynamis / SimScale ok. **16 m/s**; u nas kierunek jak Staniszewski 2024. Pewność metody: **wysoka**.

7. Overall wygrywa **Autocross + ukończony Endurance**.
   Sam max docisk bez Endurance nie wystarcza (Aachen FSA25: AX 100 pkt, Endurance 0 → overall ~14.). Pewność: **wysoka**.

8. Publiczne **Cl/Cd/balans %** od AMZ / Aachen / Delft / Tallinn / Joanneum 2024–25: **nie znalezione**.
   To jest uczciwa luka w notatce, nie „brak docisku u nich”. Pewność gapu: **wysoka**.

9. Joanneum JR25 deklaruje ok. **+17%** total DF vs poprzednik, aero **passive** (joanneum-racing.at).
   Pewność względnego Δ: **wysoka**; absolutne Cl: **not found**.

## Co to znaczy dla H1–H2 (po ludzku)

1. **H1 (tylnie skrzydło):** więcej docisku z tyłu. Cztery elementy są OK jako eksperyment CAD, bez publicznego benchmarku Cl.
2. **H2 (podłoga):** dźwignia efektywności przy DRS OUT — mapy w zakręcie / ride height przed zamrożeniem kształtu.
3. Nie kopiujemy „balansu mistrza” z Instagrama — top EU go nie publikuje. Trzymamy **61,6% → ~50/50** z własnego arkusza.
4. Esslingen CLA/CDA i Kirchberger to **rząd wielkości**. Nie wklejamy ich 1:1 w Cx/Cz bez wspólnego Aref.

## Tooling (z tej notatki — fragmentarycznie)

Publicznie widać głównie CFD: STAR-CCM+, OpenFOAM/SimScale, dużo iteracji HPC.

Przegląd logów CFD / CAD→CFD / gates / Excel vs luki PUT: **[research-aero-dev-tooling.md](research-aero-dev-tooling.md)** (2026-09-01).
Publiczne Monday / Jira / Notion u top EU: nadal **not found**.
