# 3 vs 4 elementy tylnego skrzydła — papery i top zespoły

**Status:** research 2026-09-07 (Europe/Warsaw)  
**Zasada:** tylko to, co da się cytować. **Bez** kopiowania Cl/Cd na kartę RWiter017 / `TARGETS.md`.  
**Decyzja Spec:** default **3-el.**; **4-el.** tylko jedno porównanie.

Kotwica: Cx **1,229**, |Cz| **3,682**, balans ≈ **61,6%** → ~**50/50**; DRS OUT.

Powiązane: [research-overnight-rw-multi-element.md](research-overnight-rw-multi-element.md) · [research-papers-rw-ut-yaw-clcd.md](research-papers-rw-ut-yaw-clcd.md) · [research-season-geometry-profiles.md](research-season-geometry-profiles.md).

---

## 1. Werdykt na start

**Nie znaleziono** uczciwego head-to-head „to samo auto, ta sama siatka, tylko 3 vs 4 el.” z tabelą ΔCl/ΔCd.  
4-el. **istnieje** w FS (tezy / konstrukcje), ale publicznie częściej widać **fakt istnienia** i setup (więcej parametrów), nie „+X% Cl za darmo”.

Dla PUT: domykajcie **3-el. na 017** (kąty → overlap → gap). Jedno porównanie 4-el. dopiero gdy 3-el. siedzi w killach karty.

---

## 2. Papery / tezy — 3 elementy (domyślna literatura)

**Jackson 2018** — świadomie **3 el.** (E423) jako high-DF przy sensownej złożoności:

- gap = **20 mm**, overlap = **26,25 mm**  
- Study 4: flaps **28° / 60°**, overall ≈ **22,81°**, stall ~**25°**  
- na ich aucie (DRS closed): CL_DF = **1,15**, CD = **1,21** — **nie** target 017  

Źródło: https://doi.org/10.5920/fields.2018.02

**Staniszewski 2023 (PUT)** — **3 profile**; nazwy profili w tekście **brak**:

- 2D peak overlap **−30 mm**: Fz = **−565,03 N**  
- na pojeździe (ich pakiet): Cx ≈ **0,72**, Cz ≈ **−2,03** — coupling body↔RW  

Źródło lokalne: [staniszewski-2023-wing.md](staniszewski-2023-wing.md)

**MECDC 2014** (3-el. FS, ich skrzydło):

- Cl = **2,81**  
- Cd = **0,81**  
- gap **3,6%** c, overlap **0,75%**  

Źródło: https://doi.org/10.2478/mecdc-2014-0005

---

## 3. Gdzie pojawia się 4. element

**UPC / teza FS (publiczny PDF):** sezon z **czwartym foilem** na RW — więcej parametrów setupu (kąty 2–4), re-use form poprzednich elementów; deklaracja „load vs masa się opłaca” **bez** tabeli ΔCl vs 3-el. w cytowanym fragmencie.  
Źródło (UPC commons): https://upcommons.upc.edu/server/api/core/bitstreams/413faea5-978a-4d69-8821-6d7645e2a978/content

**PoliTO (struktura RW):** opis RW z main + **trzema flapami** (czyli 4 powierzchnie nośne w stacku) na SC22evo — praca strukturalna, nie tabela aero ΔCl.  
Źródło: https://webthesis.biblio.polito.it/29130/1/tesi.pdf

**Pretoria / inne tezy 4-el.:** w overnight KB wspomniane istnienie 4-el.; **brak** head-to-head ΔCl/Cd vs 3-el. na tym samym aucie w naszych ekstraktach.

**AMZ / Delft / FaSTTUBe / Running Snail (publiczne case’y):** dużo o procesie CFD/WT; **absolutne Cl/Cd i jawna liczba elementów RW często not found** w materiałach partnerskich (patrz [research-amz-berlin-snails-aero.md](research-amz-berlin-snails-aero.md)).

---

## 4. Co 4-el. realnie „kupuje” (jakościowo)

Z tezy UPC i praktyki multi-element:

- więcej stopni swobody setupu (balans / eventy) bez zmiany całego maina,  
- możliwość utrzymania przepływu przy agresywniejszym AOA (ten sam mechanizm slotów co 3-el.),  
- koszt: masa, formy, czas meshu/CAD, ryzyko stall na ostatnim flapie (jak A2b diagnostycznie na 3-el.).

**Publiczne ΔCl / ΔCd „+4. vs 3. na tym samym FS car”: nie znaleziono.**

---

## 5. Implikacja pod Fluent H1 (017)

1. Seria **3-el.** wg [checklist-h1-fluent-rw.md](checklist-h1-fluent-rw.md).  
2. Guard: |Cz| ≥ **3,682**, Cx ≲ **1,23**, balans → 50/50.  
3. Jedno porównanie **4-el.** dopiero po stabilnym 3-el. — raportujcie **Δ vs Wasz 3-el. baseline**, nie vs Jackson Cl=1,15.  
4. Nie mieszajcie absolutów 2D OF / 4-el. diagnostyki z kartą auta.

---

## 6. Luki

- Head-to-head 3 vs 4 el. ΔCl/Cd @ 15 m/s na full-car FS — **nie znaleziono**  
- Publiczna liczba elementów RW AMZ 2024/25 — **nie znaleziono** w tej sesji  
- Pretoria pełna tabela Cl 4-el. vs 3-el. — **nie znaleziono** w KB  
