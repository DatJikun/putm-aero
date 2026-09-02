# Overnight brief — PUTM aero (rano dla Mikołaja)

**Kiedy:** research w nocy 1/2 IX 2026 (Europe/Warsaw).
**Kotwica zamrożona:** `RWiter017`.

Liczby startowe (bez zmian względem Spec):

- Cx = **1,229**
- |Cz| = **3,682**
- balans ≈ **61,6%** na przód → cel około **50%**
- Aref half-car = **0,50 m²**
- DRS ruchomy = **OUT**
- wentylator spod podłogi = **OUT**
- kolejność pracy: **H1 tylne skrzydło**, potem **H2 podłoga**

---

## Co zrobiliśmy

Dwie nowe notatki po polsku w `sources/` oraz wpisy w `INDEX.md`:

1. **`sources/research-overnight-rw-multi-element.md`** — porównanie 3 vs 4 elementów tylnego skrzydła, kąty / gap / overlap, DRS aktywny vs pasywny, kontekst **EU FS Rules 2026 T8**.
2. **`sources/research-overnight-ut-yaw-balance.md`** — podłoga i dyfuzor a balans i yaw; Staniszewski **2024** oraz Chalmers 2021, OSU Jensen 2010, Jowsey/Passmore; implikacje dla Autocross i Endurance.
3. Równolegle w repo jest też **`sources/research-papers-rw-ut-yaw-clcd.md`** (zbiorcza notatka paperów 3 vs 4 / UT+yaw / Cl/Cd). Warto czytać razem z punktami 1–2.

## Co wyszło (skrót)

### Tylne skrzydło / H1

Domyślny układ high-docisk w literaturze Formula Student to nadal **trzy elementy**.
Z Jacksona, McBeatha i Staniszewskiego 2023:

- profil E423 u Jacksona;
- gap **1–4%** cięciwy, overlap **1–6%** cięciwy;
- Staniszewski 2D: obniżanie main i overlap ok. **−30 mm**;
- na aucie coupling body↔RW zabija naiwny transfer 2D → 3D.

**Cztery elementy** pojawiają się jako wynik optymalizacji (Novais / Aveiro) oraz jako ścieżka „cascade” (LUT / Metropolia EV).
To sensowna hipoteza CAD w limicie T8, **bez** gotowej liczby ΔCz dla RWiter017.

Aktywny DRS w paperach mocno tnie opór skrzydła, ale u nas zostaje **OUT**.
Najwyżej rozważamy stały low-drag setup „pasywny” — osobno, poza peak-dociskiem.

### Podłoga / H2

Staniszewski 2024: podłoga i sekcje boczne są **mocno wrażliwe na yaw**; skrzydła są względnie „płaskie”.
Mimo to pełny pakiet wygrywa |Cz| w całym zakresie kąta skrętu.

Z paperów:

- proxy energii **−2,7%** z podłogą mimo ok. **+10 kg** (Staniszewski);
- Chalmers: dyfuzor pod **odporność** (prosta / hamowanie / zakręt), nie sam peak; ok. **13°** bywało bezpieczniejsze niż **19°**; strakes i side floors pomagają w cornering;
- OSU: lokalizacja throat to dźwignia środka ciśnienia / balansu; yaw **5°** może podnieść docisk; +**1°** roll → docisk ok. **−6%**;
- Multi-channel (Jowsey) rozszerza envelope kąta.

### Regulamin

T8 2026 nie banuje wprost ruchomego aero; nasz DRS OUT to decyzja Spec.
Fan OUT bez zmian (Michalecki + limit 500 W to osobna historia).

## Co nadal otwarte

- Brak bezpośredniego porównania **3 vs 4 elementy** na pakiecie RWiter017 (tylko hipoteza CAD).
- Brak naszej mapy **Fz_UT / yaw** na aktualnym bolidzie (Staniszewski to inny pakiet; wykresy bez pełnych tabel w plain text).
- „Pasywny DRS” 019/020 — hasło Spec bez świeżego ekstraktu liczb w `sources/`.
- Transfer Cl/Cd z Aveiro / LUT / Chalmers / Jackson jest **zakazany** — inne Aref, prędkości i geometrie.

## PDF / dropy, które warto wrzucić rano

1. **LUT** `lutpub.lut.fi/10024/171732` (pełny PDF — bot-wall przy fetch).
2. **Novais** Aveiro PDF (`ria.ua.pt/.../Documento_Pedro_Novais.pdf` — TLS padał z boxa).
3. **MDPI Fluids** `10.3390/fluids7090309` (CDN block).
4. Ewentualnie ponownie **Staniszewski 2024** PDF + arkusz → odczyt Cx(δ)/Cz(δ) z rysunków.
5. Lokalne **019/020** i postprocessing udziału **UT na 017**, jeśli leżą na OneDrive.

## Proponowany następny ruch (gdy wstaniesz)

Nie rozstrzygamy CAD w briefie — tylko kolejka:

1. **H1:** seria kątów / gap / overlap na **trzech** elementach na bazie 017 (guardrail z TARGETS).
2. Równolegle lekki CAD **4-elementowy** do jednego case’u porównawczego.
3. Potem **H2** z minimum δ = 0 oraz 1–2 punktami yaw / kąta skrętu — nie sam peak na prostej.

## Noc 2 (2026-09-01 wieczór)

Notatka AMZ / FaSTTUBe / Running Snail jest już na main (`sources/research-amz-berlin-snails-aero.md`).
Następny research — odciążenie przedniego skrzydła (H3) oraz szczeliny skrzydła tylnego — jest w toku.
Smoke OpenFOAM (~312k komórek) pozostaje poza kartą Spec.
