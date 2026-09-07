# Packaging endplate tylnego skrzydła (FS) — box, praktyka, Fluent H1 na RWiter017

**Status:** research 2026-09-07 (Europe/Warsaw)  
**Dla kogo:** Spec / CAD przed serią Fluent H1 na aucie (`RW_iter017`).  
**Zasada:** liczby tylko z cytowanych źródeł lokalnych. **Bez** wymyślania Cl/Cd dla RWiter017. **Bez** wpisywania Cl/Cd do `TARGETS.md`.  
**Kotwica zespołu (punkt odniesienia kampanii, nie wynik tej notatki):** Cx **1,229**, Cz **−3,682**, balans ≈ **61,6%** przód → ~**50/50**.

Powiązane: [fs-rules-2026-t8.md](fs-rules-2026-t8.md) · [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md) · [checklist-h1-fluent-rw.md](checklist-h1-fluent-rw.md) · [SPEC-FLUENT-H1-RWITER017.md](../SPEC-FLUENT-H1-RWITER017.md) · [SPEC-H1-2D-GATE.md](../SPEC-H1-2D-GATE.md) · [sanity-cfd1-2d-rw-vs-lit.md](sanity-cfd1-2d-rw-vs-lit.md).

---

## 1. Po co ta notatka

Endplate domyka rozpiętość RW, tnie przeciek tipowy i ustawia, jak wir tip oraz ślad za autem wchodzą w RW i wake opon / dyfuzora. Packaging musi najpierw zmieścić się w envelope **T 8**, potem dać sensowny flow na aucie we Fluencie H1. To notatka **packagingowa** — nie karta Cl.

---

## 2. Cue regulaminowe (FS Rules 2026 v1.1 — T 8)

Źródło lokalne: [fs-rules-2026-t8.md](fs-rules-2026-t8.md) (PDF `team/rules-current.pdf`).

Dla **wysokiego RW / endplate** (aero za head restraint, zwykle wysokość **> 500 mm** od ziemi):

- szerokość: **nie outboard** od most inboard point tylnej opony/koła (T 8.2.2) — RW >500 mm siedzi **inboard** tylnej opony;
- wysokość aero za HR: **niższa niż 1,1 m** od ziemi (T 8.2.1; Fig. 14: 1100 mm);
- setback do tyłu: max **250 mm** za rearmost part of the rear tires (T 8.2.3);
- envelope przy kołach prosto i **any suspension setup**, z kierowcą i bez (T 8.2.4).

Implikacja: nasze RW jest w **wąskim** boxie szerokości (inboard tylnej opony), pod limitem **1,1 m**, z max **250 mm** za oponami.

---

## 3. 800×500 mm — to skrzynka meshu OF 2D, **nie** T 8

**Nie mylić:**

| Co | Skąd | Znaczenie |
|----|------|-----------|
| Envelope T 8 | [fs-rules-2026-t8.md](fs-rules-2026-t8.md) | płaszczyzny względem opon / HR / ziemi — **nie** prostokąt 800×500 |
| Skrzynka **800×500 mm** | [SPEC-H1-2D-GATE.md](../SPEC-H1-2D-GATE.md) („skrzynka 800×500”); [sanity-cfd1-2d-rw-vs-lit.md](sanity-cfd1-2d-rw-vs-lit.md) („domena endplate 800×500 mm”) | **domena / mesh box OpenFOAM 2D**, izolowane skrzydło — **nie** limit regulaminowy endplate |

Claim T 8: box **800×500 mm** jako envelope endplate/wing **nie występuje** w FS Rules 2026 v1.1. Jeśli ktoś pamięta 800×500 z FSAE / starszych lat — **nie przenosić** na CAD 2026. Przy Fluent H1 na aucie obowiązuje envelope T 8, nie skrzynka OF 2D.

---

## 4. Jackson 2018 — ich auto (ostrzeżenie T 8 2026)

Źródło lokalne: [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md).

Na **ich** aucie (paper, nie nasz envelope):

- góra endplate **1200 mm** od ziemi;
- tylna ściana endplate **250 mm** za tylnymi kołami;
- wniosek: montować RW **jak najwyżej**, żeby uniknąć disturbed flow / wake za głową kierowcy / roll hoop / air intake.

**Ostrzeżenie 2026:** T 8.2.1 wymaga wysokości **&lt; 1,1 m**. Wartość **1200 mm** z Jacksona to **ich** car / ówczesny envelope — **przekracza** limit T 8 2026. Nie kopiować jako legalny target CAD. Setback **250 mm** zgadza się z T 8.2.3 (max 250 mm za tylnymi oponami). U nas „jak najwyżej” kończy się **pod 1,1 m**, nie na 1200 mm.

CL/CD / AOA Jacksona opisują **ich** RW + DRS — **nie** przenosić na kartę RWiter017 ani do `TARGETS.md`.

---

## 5. Fluent H1 na RWiter017 — endplate zamrożony, potem tipy

Kampania: [SPEC-FLUENT-H1-RWITER017.md](../SPEC-FLUENT-H1-RWITER017.md) · kolejność: [checklist-h1-fluent-rw.md](checklist-h1-fluent-rw.md).

**Proces packaging / endplate w H1:**

1. **Zamrozić endplate** (wysokość / setback / obrys w limicie T 8) na czas serii **3-elementowej**: kąty → overlap → gap (jeden parametr naraz).  
2. Dopiero po sensownym 3-el. — **1–2 warianty tip / endplate** (lokalne detale TE / tip), bez mieszania setupu Fluent.  
3. Ewentualnie jedno porównanie 4-el. obok zwycięskiego 3-el. — nie default.

**Guard / kill (kotwica zespołu, nie paper):**

- |Cz| **≥ 3,682** (nie poniżej baseline);
- Cx ≲ **1,23**;
- balans w stronę ~**50/50**, nie jeszcze bardziej na przód;
- stall / Cx↑ bez zysku DF → odrzut.

**Czego nie robić:**

- **nie** wpisywać Cl/Cd (ani z Jacksona, ani z OF 2D, ani z tej notatki) do `TARGETS.md`;
- nie traktować 1200 mm Jacksona ani skrzynki 800×500 OF jako limitu T 8;
- nie kręcić tipów równolegle z kątami/gap/overlap na 3-el. — najpierw freeze endplate.

---

## 6. Claims (skrót)

| claim | evidence | confidence |
|-------|----------|------------|
| RW >500 mm: inboard tylnej opony; wysokość &lt;1,1 m; setback max 250 mm za tylnymi oponami | [fs-rules-2026-t8.md](fs-rules-2026-t8.md) T 8.2.1–3 | high |
| 800×500 mm = domena/mesh OF 2D (SPEC-H1-2D-GATE / sanity), **nie** envelope T 8 | SPEC-H1-2D-GATE + sanity + fs-rules-2026-t8 | high |
| Jackson: góra endplate 1200 mm (**ich** auto); setback 250 mm; montaż wysoko vs wake | jackson-2018-cfd-drs | high (ich paper) |
| 1200 mm Jacksona &gt; limit T 8.2.1 (1,1 m) 2026 — nie legal CAD | reguła vs paper | high |
| H1: freeze endplate przy sweep kątów/gap/overlap 3-el.; potem 1–2 tipy; \|Cz\|≥3,682, Cx≲1,23; bez Cl → TARGETS | Spec H1 + checklist | high (proces) |
