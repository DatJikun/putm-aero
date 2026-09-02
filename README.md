# putm-aero

Baza wiedzy o pakiecie aerodynamicznym PUT Motorsport (Formula Student).
Trzymamy tu źródła, zamrożone ustalenia i kartę celów — bez zgadywania liczb.

## Od czego zacząć

1. [INDEX.md](INDEX.md) — źródła i ustalenia, które już zamroziliśmy.
2. [TARGETS.md](TARGETS.md) — karta celów (Spec): co optymalizujemy i w jakich widełkach.
3. [sources/](sources/) — notatki ze źródeł i claims (literatura oraz arkusze zespołu).
4. [team/](team/) — arkusze CFD zespołu (CSV) oraz skrypty Fluent.
5. [assumptions/ASSUMPTIONS-DRAFT.md](assumptions/ASSUMPTIONS-DRAFT.md) — szkic założeń (DRAFT; przy konflikcie wygrywa Spec).

## W skrócie

**Baseline bolidu** to `RW_iter017` — aktualny bolid po zawodach:

- Cx = **1,229**
- Cz = **−3,682**
- Cm = **−0,429**

**Cel:** jak największy docisk przy spokojnym oporze i balansie możliwie blisko pół na pół (ok. 50/50).
Priorytet eventów: **Endurance** i **Autocross**.
Ruchomego DRS nie robimy. Wentylatora spod podłogi nie robimy.
Kolejność pracy: najpierw **tylnie skrzydło (H1)**, potem **podłoga (H2)**.

### Kilka skrótów (raz na start)

- **Cx** — współczynnik oporu powietrza (im niżej, tym mniej „ciągnie” bolid).
- **Cz** — współczynnik docisku; u nas **ujemny = docisk** (przyciska auto do toru).
- **Aref** — powierzchnia odniesienia używana w CFD do przeliczenia sił na współczynniki.
  Half-car ≈ **0,50 m²**, pełny bolid ≈ **1,0 m²**.
- **Half-car** — model połowy bolidu (symetria), żeby oszczędzić siatkę i czas.
- **Yaw** — kąt „bokiem do napływu”, jak w zakręcie; ważne przy Autocross i Endurance.
