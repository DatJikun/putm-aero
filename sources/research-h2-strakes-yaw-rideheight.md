# H2 pogłębienie: strakes + yaw + ride height (undertray)

**Status:** research 2026-09-07 (Europe/Warsaw)  
**Dla kogo:** Spec przed Fluent H2 na aucie.  
**Zasada:** liczby tylko z cytowanych źródeł. Nie wklejamy Cl/Cd cudzych aut do `TARGETS.md`.  
**Kotwica:** RWiter017 — Cx **1,229**, Cz **−3,682**, balans ≈ **61,6%** przód → ~**50/50**; fan OUT; po H1 RW.

Budujemy na: [research-h2-undertray-balance-levers.md](research-h2-undertray-balance-levers.md) · [research-overnight-ut-yaw-balance.md](research-overnight-ut-yaw-balance.md).

---

## 1. Po co strakes (i side floors)

Strakes to pionowe „płotki” w objętości dyfuzora. Dzielą kanał na węższe tunele, ograniczają migrację separacji w poprzek auta i pomagają trzymać wiry / niskie ciśnienie tam, gdzie chcecie (Chalmers CFS; Jowsey).

Chalmers — po dodaniu strakes + side floors przy kącie **13°** (ich CFS, CL = docisk dodatni):

- CL straight = **3,854**  
- CL cornering = **3,619**  
- CL braking = **3,005**  
- aero balance przy hamowaniu ≈ **67%** rear (ich definicja % tyłu)

Źródło: https://odr.chalmers.se/bitstreams/2e9b2842-d1d0-4c5a-aa01-a13458f7ddaf/download

Jowsey & Passmore (bluff body / multi-channel):

- multi-channel pomaga szczególnie **powyżej** ~**13°** ekspansji  
- deklarowany zysk DF do ok. **+13%** w mid-range **16–19°**  
- przyrost drag mały względem zysku DF  

Źródła: https://doi.org/10.1243/09544070JAUTO1339 · https://dspace.lboro.ac.uk/2134/13646

SAE 2017-01-2163 (vanes + flap, FSAE-like):

- vanes: DF ↑ do **13%**  
- vane + flap: DF ↑ do **25%** (max w ich serii)

Źródło: https://saemobilus.sae.org/papers/numerical-investigation-aerodynamic-effects-vanes-flaps-automotive-underbody-diffusers-2017-01-2163

**Dla PUT:** strakes to dźwignia **po** wyborze throat + kąta dyfuzora (~**13°** jako start robustness z Chalmers), nie zamiast nich. Δ% balansu na 017 ze strakes: **nie znaleziono**.

---

## 2. Ride height (prześwit)

Mała zmiana RH mocno rusza siły (ground effect). Regulamin: static GC ≥ **30 mm** (T 2.2); sliding skirts OUT.

FST Lisboa FST10e (aeromap, abstract):

- RH → ok. **10%** rozrzutu CD·A między peakami  
- RH → ok. **20%** rozrzutu −CL·A między peakami  

Źródło: https://scholar.tecnico.ulisboa.pt/records/WjT08GaGU4ee77V1ZI_WgpbeDe_scfAseZd-?lang=en

SAE 2017-01-5016 (ich CFD, ranking L/D):

- best L/D: inlet **3°**, outlet **10°**, GC **30 mm**  
- słaby: inlet **5°**, outlet **16°**, GC **50 mm**  

Źródło: https://doi.org/10.4271/2017-01-5016

OSU / Global Formula Racing (undertray CFD): małe zmiany RH → duże zmiany obciążeń (kierunek; konkretne N zależą od modelu).  
Źródło: https://ir.library.oregonstate.edu/downloads/7h149t91w

**Mapa RH dla RWiter017: nie znaleziono.**

---

## 3. Yaw / cornering / roll

Staniszewski 2024 (PUT): podłoga pomaga na wprost, ale przy kącie skrętu / yaw charakterystyka Cx/Cz się psuje względem pakietu bez UT — **gate yaw przed freeze** (szczegóły w [staniszewski-2024-energy.md](staniszewski-2024-energy.md)).

FST10e (abstract): yaw → rzędu **~16%** zmiany DF między peakami mapy (orientacja ich auta).

OSU: yaw **5°** + roll **1°** → spadek DF ok. **6%** vs sam yaw w ich teście (kierunek: roll + yaw szkodzi bardziej niż sam yaw).  
Źródło: https://ir.library.oregonstate.edu/downloads/7h149t91w

Chalmers: przy hamowaniu (pitch) balans potrafi mocno iść na tył (u nich ~**67%** rear z strakes) — to ostrzeżenie pod Stability / brake, nie przepis na 50/50.

**Mapa yaw 0° / ~5° / ~10–15° dla 017: nie znaleziono** (do zrobienia w Fluent H2).

---

## 4. Checklista pomiarów H2 (Fluent)

Przy **15 m/s**, Aref half **0,50 m²**, moment jak w workflow:

- Cx, Cz, Cm, balans % przód  
- udział Fz_UT / Fz_all (osobne linie)  
- Cp / separacja w kanałach dyfuzora (czy strakes trzymają flow)  
- punkty: RH nominal + wyżej/niżej (w limicie GC)  
- yaw **0°**, potem **~5°**, ewentualnie **~10°**  

Kill / guard:

- |Cz| ≥ **3,682**  
- Cx ≲ **1,23**  
- balans w stronę ~**50/50** (~12 pp), nie „tylko peak CL @ δ=0”

---

## 5. Kolejność CAD pod H2

1. Throat + kąt dyfuzora (start ~**13°**).  
2. Strakes on/off (ta sama siatka / ten sam przepis Fluent).  
3. Gate yaw + RH zanim freeze.  
4. Rake / kick-up opcjonalnie na końcu.

---

## 6. Luki

- Δbalans pp vs strakes na RWiter017 — **nie znaleziono**  
- pełna tabela Staniszewski Cx(δ) w tej notatce — patrz lokalny ekstrakt  
- Jowsey yaw tables dla FS full-car — **nie znaleziono**  
- publiczne Cl/Cd AMZ/Delft UT vs RH — **nie znaleziono** (procesowe, nie liczby)
