# Overnight brief — PUTM aero (rano dla Mikołaja)

**Kiedy:** research w nocy 1/2 IX 2026 (Europe/Warsaw)  
**Kotwica zamrożona:** `RWiter017` Cx **1,229** · |Cz| **3,682** · balans ~**61,6%→50%** · DRS **OUT** · fan **OUT** · H1 RW → H2 UT · Aref half **0,50**

---

## Co zrobiliśmy

Dwie nowe notatki PL w `sources/` + wpisy w `INDEX.md`:

1. **`sources/research-overnight-rw-multi-element.md`** — 3 vs 4 el. RW, AOA/gap/overlap, DRS aktywny vs pasywny, kontekst **EU FS Rules 2026 T8**.
2. **`sources/research-overnight-ut-yaw-balance.md`** — UT/dyfuzor a balans i yaw; Staniszewski **2024** + Chalmers 2021, OSU Jensen 2010, Jowsey/Passmore; implikacje Autocross/Endurance.
3. Równolegle w repo jest też **`sources/research-papers-rw-ut-yaw-clcd.md`** (zbiorcza notatka paperów 3vs4 / UT+yaw / Cl/Cd) — warto czytać razem z (1)–(2).

## Co wyszło (skrót)

**RW / H1.** Domyślny high-DF w literaturze FS to nadal **3 elementy** (Jackson E423 + McBeath gap 1–4%c / overlap 1–6%c; Staniszewski 2023: main↓ i overlap~−30 mm w 2D, na aucie coupling zabija naiwny transfer). **4 elementy** pojawiają się jako wynik optymalizacji (Novais/Aveiro) i jako ścieżka „cascade” (LUT/Metropolia EV) — sensowna hipoteza CAD w envelope T8, **bez** gotowej liczby ΔCz dla 017. Aktywny DRS w paperach mocno tnie Cd skrzydła, ale u nas zostaje **OUT**; najwyżej stały low-drag setup „pasywny”.

**UT / H2.** Staniszewski 2024: UT&SW **mocno yaw-wrażliwe**, skrzydła płaskie; mimo to pełny pakiet wygrywa |Cz| w całym δ, a proxy energii **−2,7%** z UT mimo +~10 kg. Chalmers: wybierać dyfuzor pod **robustness** (prosta/hamowanie/corner), nie sam peak; ~**13°** bywało bezpieczniejsze niż 19°; strakes + side floors pomagają w cornering. OSU: **lokalizacja throat = dźwignia CoP/balansu**; 5° yaw może nawet podnieść DF, +1° roll zjada ~6%. Multi-channel (Jowsey) rozszerza envelope kąta.

**Regulamin.** T8 2026 nie banuje explicite movable aero; nasz DRS OUT to Spec. Fan OUT bez zmian (Michalecki + limit 500 W to osobna historia).

## Co nadal otwarte

- Brak **head-to-head 3 vs 4 el.** na pakiecie RWiter017 (tylko hipoteza CAD).
- Brak naszej mapy **Fz_UT / yaw** na aktualnym bolidzie (Staniszewski to inny pakiet + wykresy bez pełnych tabel w plain text).
- „Pasywny DRS” 019/020 — hasło Spec bez świeżego ekstraktu liczb w `sources/`.
- Transfer Cl/Cd z Aveiro/LUT/Chalmers/Jackson **zakazany** — inne Aref/V/geometrie.

## PDF / dropy, które warto wrzucić rano

1. **LUT** `lutpub.lut.fi/10024/171732` (pełny PDF — bot-wall przy fetch).
2. **Novais** Aveiro PDF (`ria.ua.pt/.../Documento_Pedro_Novais.pdf` — TLS padał z boxa).
3. **MDPI Fluids** `10.3390/fluids7090309` (CDN block).
4. Ewentualnie ponownie **Staniszewski 2024** PDF + arkusz → odczyt Cx(δ)/Cz(δ) z rysunków.
5. Lokalne **019/020** i postpro udziału **UT na 017**, jeśli leżą na OneDrive.

## Proponowany następny ruch (gdy wstaniesz)

Nie rozstrzygamy CAD w briefie — tylko kolejka: **H1** seria kątów/gap/overlap 3-el. na 017 (guardrale TARGETS) → równolegle lekki CAD **4-el.** do jednego case’u porównawczego → potem **H2** z minimum δ=0 + 1–2 punkty yaw/δ, nie sam peak na prostej.
