# Kandydaci profili i geometrii na sezon (RW / FW / undertray)

**Status:** notatka preferencji CAD/CFD, 2026-09-02 (Europe/Warsaw)  
**Zasada:** tylko to, co już jest w paperach / KB. Liczby z cytatem. **Nie** wklejamy ich do `TARGETS.md` jako nowych Cl/Cd PUT.  
**Kotwica pakietu:** RWiter017 — Cx **1,229**, Cz **−3,682**, balans ≈ **61,6%** przód → cel ~**50/50**; DRS OUT; fan OUT; kolejka **H1 RW → H2 UT → H3 FW**.

---

## 1. Tylne skrzydło (H1) — default **3 elementy**

### Co brać jako punkt startu

| Kandydat | Skąd | Uwagi |
|----------|------|--------|
| **3-el. RW** jako default | Spec / claims EU + Staniszewski 2023 + Jackson 2018 | 4-el. tylko **jedno** porównanie, bez absolutów 3 vs 4 |
| Profil **E423** (main + 2 flaps) | Jackson 2018 | main **540 mm**, flaps po **180 mm**; gap **20 mm**; overlap **26,25 mm** — ich auto, nie 017 |
| Profil **nie nazwany** (3 profile) | Staniszewski 2023 (PUT) | w tekście **brak** nazwy NACA/Selig; kroki kątów/overlap/gap są użyteczne |
| S1223 na RW | CFD#1 diagnostyka 2D (OF, zaparkowane) | to był case setupu, **nie** zatwierdzony profil sezonu na aucie |

### Kąty / sloty (kierunek, nie target)

Jackson Study 4 (E423):

- Flap1 = **28°**  
- Flap2 = **60°**  
- overall ≈ **22,81°**  
- stall ostrzeżenie ≈ **25°**

McBeath (cyt. Jackson/Craig):

- gap = **1–4%** c (praktycznie ~**2%** c)  
- overlap = **1–6%** c (praktyka Craig ~**1,5%** c)

Staniszewski 2023 (2D izolowane, V = **15 m/s**):

- kroki: main **1,5°**, klapy **2°**, overlap **10 mm**, gap **5–20 mm**  
- overlap **−30 mm** → Fz = **−565,03 N** (peak w ich tabeli)  
- gap **+5/+10 mm** → Fz = **−559,80 N**

Checklista pod Fluent: [checklist-h1-fluent-rw.md](checklist-h1-fluent-rw.md).

### Czego nie robić

- Nie kopiować Cl/Cd Jacksona / MECDC na kartę 017.  
- Nie porównywać absolutów 3-el. vs 4-el. między różnymi setupami.

---

## 2. Przednie skrzydło (H3 — później)

### Kandydaci profilu

| Kandydat | Skąd | Uwagi |
|----------|------|--------|
| **Selig S1223** | Nagłowski 2024 (wąsy); JRAME 2024 (izolowane 2D double-element FW) | u Nagłowskiego S1223 = **wąsy**, niekoniecznie cały FW 017 |
| Dobór profilu pod lokalizację | decyzja zespołu (wąsy TBD) | „S1223 wszędzie” **nie** jest założeniem sezonu |

Nagłowski 2024 @ **15 m/s** (inny pakiet niż 017):

- Fz_fw = **−221 N**  
- udział FW ≈ **39%** Fz_all  

JRAME 2024 (izolowane 2D FW S1223 — **nie** full car):

- Cl ≈ **4,84**  
- DF FW = **884,3 N**  

H3 = odciążenie FW **dopiero po** H1+H2 — [research-h3-fw-unload-for-balance.md](research-h3-fw-unload-for-balance.md).

---

## 3. Undertray (H2)

### Dźwignie geometrii (kolejność z notatki H2)

1. **Throat** — przesunięcie peak Cp → dźwignia balansu (kierunek: throat dalej do tyłu → więcej % tyłu). Δ% na 017: **nie znaleziono**.  
2. **Kąt dyfuzora** — Chalmers preferuje **13°** nad **19°** pod robustness (nie pod peak w jednym punkcie):  
   - CL straight (13°) = **3,729**  
   - CL cornering (13°) = **3,603**  
   - CD straight (13°) = **1,419**  
   - aero balance rear (13°, straight) ≈ **49,68%**  
3. **Strakes / side floors** — Chalmers po strakes: CL straight = **3,854**; Jowsey: multi-channel pomaga powyżej ~13°, do ok. **+13%** DF w mid-range 16–19°.  
4. **Ride height / rake** — mapować przed zamrożeniem (yaw/RH czułe; szczegóły w [research-h2-undertray-balance-levers.md](research-h2-undertray-balance-levers.md)).  
5. **Kick-up / gurney na TE dyfuzora** — opcjonalnie na końcu (SAE / Willemsen kontekst FSAE).

Fan spod podłogi: **OUT** (decyzja pakietu + Michalecki).

---

## 4. Wąsy / vortex generators

- Profil w literaturze PUT: **S1223** (Nagłowski).  
- Status zespołu: **TBD** — dobrać pod miejsce na aucie, nie automatycznie „jak w pracy”.  
- Kolejność: po H1–H3, jeśli balans nadal za bardzo na przodzie (H4 w shortliście).

---

## 5. Luki (nie znaleziono / TBD)

- Nazwa profilu RW w Staniszewskim 2023.  
- Oficjalny profil FW/RW na **RWiter017** w CSV (same Cx/Cz pakietu).  
- Δbalans pp vs przesunięcie throat na 017.  
- Publiczne Cl/Cd 4-el. RW head-to-head vs 3-el. na tym samym aucie.  
- FW = **588 N** — **not found**.

---

## 6. Werdykt na sezon (roboczy)

| Obszar | Kandydat startowy | Następny krok |
|--------|-------------------|---------------|
| RW | **3-el.**; profil do wyboru przy CAD (E423 = lit. Jackson; Wasz obecny profil 017 = prawda terenowa) | Fluent H1: kąty → overlap → gap |
| FW | nie ruszać agresywnie; S1223 = kandydat wąsów / lit. FW 2D | H3 dopiero po H1+H2 |
| UT | dyfuzor ok. **13°** jako start robustness; throat + strakes | mapa yaw/RH przed freeze |
| Wąsy | S1223 kandydat | TBD lokalizacja |

Żadna liczba z tabel powyżej **nie** zastępuje Cx/Cz RWiter017 w karcie Spec.
