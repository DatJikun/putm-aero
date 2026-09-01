# Overnight research: wieloelementowe RW FS (3 vs 4 elementy, AOA/gap/overlap, DRS)

**Status:** notatka z researchu nocnego (2026-09-01 → rano 2026-09-02 Europe/Warsaw)  
**Język:** PL, zdania czytelne  
**Zasada:** tylko publiczne paper/teza + to, co już jest w KB repo. **Bez wymyślonych Cl/Cd dla naszego bolidu.** Liczby Cl/Cd poniżej pochodzą wyłącznie ze źródeł zewnętrznych (inny samochód / inna Aref / inna V) i służą jako kontekst, nie jako targety PUT.

**Kotwica Spec (zamrożona):** `RW_iter017`

- Cx = **1,229**
- |Cz| = **3,682**
- balans ≈ **61,6%** przód → cel ~**50%**
- Aref half ≈ **0,50 m²**
- **DRS ruchomy OUT**; **fan OUT**
- kolejność **H1 RW → H2 UT**

**Kontekst regulaminu:** preferujemy **EU Formula Student Rules 2026 v1.1** (T8 / T2.2 / T11.11) — lokalne claims w [fs-rules-2026-t8.md](fs-rules-2026-t8.md) oraz [rules-aero-boxes-loopholes.md](rules-aero-boxes-loopholes.md).

Siostrzana notatka paperów: [research-papers-rw-ut-yaw-clcd.md](research-papers-rw-ut-yaw-clcd.md).

Powiązane lokalnie: [staniszewski-2023-wing.md](staniszewski-2023-wing.md), [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md), [research-balance-levers-h1-h5.md](research-balance-levers-h1-h5.md), [research-aero-for-targets.md](research-aero-for-targets.md).

---

## 1. Po co w ogóle multi-element RW w FS

Na torach Formula Student / FSAE prędkości są umiarkowane (rzędu 15–30 m/s w CFD i typowych zakrętach), a share prostych jest krótki względem zakrętów. W takim reżimie skrzydło tylne ma dostarczyć **dużo docisku przy wysokim efektywnym AOA**, a nie „czystą” efektywność jak w samolocie. Wieloelementowa kaskada (main + flaps) pozwala utrzymać przepływ przy większym kącie niż pojedynczy profil — sloty „doprowadzają” energię do warstwy przyściennej kolejnych elementów i opóźniają oderwanie.

Dla nas H1 oznacza przede wszystkim **więcej |Fz| z tyłu** bez rozwalania Cx. Guardrail:

- balans startowy ~**61,6%** przód
- Cx ≲ **1,23**

Liczba elementów (3 vs 4) to tylko jedna z dźwigni obok kątów, gap i overlap; nie zastępuje mapy na pakiecie 017.

---

## 2. Trzy elementy — co mówią źródła publiczne i PUT

### 2.1 Staniszewski 2023 (PUT, już w repo)

Lokalna praca inżynierska optymalizuje **3-profilowe** RW w 2D (kąty, overlap, gap), potem weryfikuje na pojeździe. Wnioski jakościowe (szczegóły liczbowe w [staniszewski-2023-wing.md](staniszewski-2023-wing.md)):

- Obniżanie kąta main względem baseline **7,5°** w 2D podnosi |Fz| i obniża Fx aż do ok. **−6,5°**; dalsze **−7,0°** już pogarsza Fz.
- Zmniejszanie **overlap** do ok. **−30 mm** mocno zwiększa docisk 2D; **−40 mm** już pogarsza — jest optimum.
- Drobne **gap +5 / +10 mm** utrzymuje wysoki DF przy niskim oporze.
- Na **całym pojeździe** (tamtym pakiecie):
  - Cx ≈ **0,72**
  - Cz ≈ **−2,03**
  - **coupling body↔RW** zabija naiwny transfer 2D→3D — ostrzeżenie wprost dla naszej serii H1 na 017.

### 2.2 Jackson 2018 (Huddersfield / Fields) — 3 el. + DRS

Artykuł [Jackson, *Fields* 2018](https://doi.org/10.5920/fields.2018.02) (ekstrakt: [jackson-2018-cfd-drs.md](jackson-2018-cfd-drs.md)):

- Wybrano **3 elementy** (main + 2 flaps), profil **E423**; max chord/span wg ówczesnych limitów: **860 / 920 mm**.
- Gap/overlap wg **McBeath**:
  - gap = **1–4%c**
  - overlap = **1–6%c**
  - u nich: overlap = **26,25 mm**, gap = **20 mm**
- McBeath (cytowany), zakres high-DF:
  - flap1 AOA = **25–30°**
  - flap2 AOA = **30–70°**
- Study 4:
  - flap1 = **28°**
  - flap2 = **60°**
  - overall AOA ≈ **22,8°** (stall ~**25°**)
- Na pojeździe (ich model, ich A) — **nie** kopiować na RWiter017:
  - DRS closed: CL_DF = **1,15**, CD = **1,21**
  - DRS open: CL_DF = **0,26**, CD = **0,79**

Wniosek praktyczny: 3-el. + agresywne klapy to sprawdzony „domyślny” high-DF layout FS; stall siedzi blisko peaku — nie pchać overall AOA „dla liczb”.

### 2.3 Wytyczne McBeath (Competition Car Aerodynamics) — punkt startu, nie optimum

Publiczne cytowania (Jackson i inni) powtarzają te same startowe zakresy:

| Parametr | Zakres startowy (McBeath, cyt.) |
|----------|----------------------------------|
| Slot gap | **1–4%** cięciwy poprzedniego elementu |
| Overlap | **1–6%** cięciwy |
| Flap 1 AOA | ok. **25–30°** |
| Flap 2 AOA | ok. **30–70°** |

Inne prace (np. monografie / tezy FSAE cytujące McBeath) czasem wybierają gap ~**2%** i overlap ~**1,5%** ze względu na ugięcia konstrukcji pod obciążeniem — bardzo mały gap „zamyka się” przy deflekcji. Dla nas: **T 8.3** (sztywność) + ugięcie kompozytu muszą wejść do kryteriów CAD 3- vs 4-el., zanim CFD ogłosi zwycięzcę.

Linki kontekstowe: Jackson DOI powyżej; McBeath — książka (brak otwartego PDF w tej sesji); omówienie gap/overlap w publicznych notatkach skrzydeł (np. [SM Designs advice](http://sm-designs.co.uk/advice.html) — porównanie single vs dual, nie FS rules).

---

## 3. Cztery elementy — co da się powiedzieć bez wymyślania Cl/Cd

### 3.1 Novais 2021 (Aveiro) — optymalizacja → 4 airfoile

Teza: *Development and optimization of an aerodynamic device for the UA Formula Student car* (Universidade de Aveiro, 2021).

- Abstrakt / handle: [http://hdl.handle.net/10773/33796](http://hdl.handle.net/10773/33796) · PDF: [ria.ua.pt bitstream](https://ria.ua.pt/bitstream/10773/33796/1/Documento_Pedro_Novais.pdf)
- Cel: kod optymalizacji (Harmony Search) parametrów RW na podstawie profilu prędkości z tyłu auta (CFD car → inlet do izolowanego RW).
- **Wynik optymalizacji: konfiguracja z 4 airfoilami**; autor deklaruje wyniki lepsze niż RW zwycięzcy FSAE Czech 2016 (porównanie w pracy — **nie** przenosimy ich Cl/Cd na PUT).
- Narracja w tezie: RW multi-element zwykle **3 lub 4** zestawy. Udział RW w DF:
  - Novais (ich claim): ~**30%** całkowitego DF
  - Nagłowski (inny bolid): RW ~**24%** Fz_all

Implikacja dla H1: 4-el. pojawia się jako **wynik optymalizacji przestrzeni parametrów**, nie jako dogma „więcej = lepiej”. Bez naszego CAD w envelope T8 i bez case’u 3↔4 na pakiecie 017 nie mamy liczby ΔCz.

### 3.2 LUT / Metropolia 2026 — parametric study secondary flaps + cascade

Teza LUTPub: *Optimising the aerodynamic design process: a parametric study of multi-element rear wings for Formula Student electric vehicles* (Metropolia Motorsports HPF026).

- Handle: [https://lutpub.lut.fi/handle/10024/171732](https://lutpub.lut.fi/handle/10024/171732)
- Dwie ścieżki: (1) retune kątów secondary flaps i **slot gaps** wokół stałego mainplane; (2) **modularne dołożenie cascade** do baseline RW.
- CFD steady → współczynniki → model osiągów (cornering, lap time, drag). Fokus na **trade-off DF↔drag** i alokacji czasu rozwoju, nie na katalogu Cl/Cd do skopiowania.
- Wniosek jakościowy z abstraktu: DF z RW mocno poprawia cornering i skraca szacowany lap time; wzrost drag **nie jest liniowy**. Dla torów technicznych (niskie V w zakręcie) **max |CL|** bywa ważniejsze niż peak L/D.

Implikacja: ścieżka „dołóż cascade / 4. element” jest w EU FS EV traktowana jako **modułowy** eksperyment obok retune 3-el. — dokładnie nasza hipoteza CAD z Spec.

### 3.3 Inne wzmianki 4-el. (orientacja)

- Prace FSAE / IJCNWC opisują wybór **4-elementowego** skrzydła (slat + main + 2 flaps) jako kompromis DF vs masa/drag; walidacja WT vs CFD często pokazuje Cl w ~10%, Cd gorzej (klasyczny problem RANS) — [przykład PDF](https://www.ijcnwc.com/admin/uploads/23.pdf).
- UPC / Dynamics (design & manufacturing RW): w opisach kolejnych sezonów pojawia się **dodanie czwartego flapu** i współdzielone formy — sygnał, że teamy EU idą w 4 el. gdy envelope i tooling na to pozwalają ([UPC handle](https://hdl.handle.net/2117/396194)).
- Merkel 2014 (UT Arlington): aktywne multi-element (nawet 5-el. FW/RW) + min-drag pose — [http://hdl.handle.net/10106/24176](http://hdl.handle.net/10106/24176). Kontekst **FSAE US** (inny regulamin ruchu elementów niż nasza decyzja DRS OUT).

**Czego nie wnioskujemy:** że 4 el. da nam X% ΔCz albo że „zawsze wygrywa” 3 el. Koszt: masa, sztywność T8.3, więcej slotów do tolerancji produkcji, łatwiej wyjść poza LE/TE / box T8.2.

---

## 4. AOA, gap, overlap — jak czytać parametry pod H1

1. **Najpierw main AOA i overlap** (Staniszewski 2D: największe dźwignie na izolowanym RW), potem drobny gap.
2. **Gap zbyt mały** = ryzyko zamknięcia szczeliny pod obciążeniem i stall slotu; **zbyt duży** = słabsze „zasilanie” warstwy przyściennej kolejnego elementu.
3. **Overlap** ma optimum; „więcej overlap = więcej DF” jest fałszywe poza pewnym punktem (−40 mm w Staniszewskim).
4. **Kąty tylnych flaps** po ustabilizowaniu main mogą być płaskie w wrażliwości (±2° w Staniszewskim nie pomagało) — ale u Jacksona / McBeath to właśnie flaps niosą high-AOA DF; konflikt znika, gdy pamiętamy, że Staniszewski startował już z ustawionymi flaps.
5. **Free-stream ≠ on-car.** Jackson zakładał transfer optimum free-stream→pojazd; Staniszewski pokazał, że body i sekcje boczne potrafią zabić zysk. Nasza seria H1 = **na pakiecie RWiter017**, nie izolowana kaskada.
6. **Montaż wysoko** (Jackson): mniej disturbed flow za head restraint / roll hoop — pod limitem T 8.2.1 (max **1,1 m** za HR).

---

## 5. DRS: aktywny vs „pasywny” — literatura vs nasz Spec i T8

### 5.1 Co mówi literatura (aktywny DRS)

| Źródło | Mechanizm | Co mierzono (ich auto) | Link |
|--------|-----------|------------------------|------|
| Jackson 2018 | Ruchome tylne elementy closed/open | CD 1,21→0,79; duży zysk Vmax/accel w modelu | [doi:10.5920/fields.2018.02](https://doi.org/10.5920/fields.2018.02) |
| MDPI Fluids 2022 | 3-el. S1123 + aktuatory liniowe; DRS rotacja flaps | Abstrakt: przy min-drag ~**78%** spadek Cd skrzydła i ~**53%** spadek Cl względem high-DF (izolowane/aktuatory w modelu) | [doi:10.3390/fluids7090309](https://doi.org/10.3390/fluids7090309) |
| NOVA / FCT 2022 (Numerical Study of a DRS…) | 3-el.; mapowanie AOA flaps + centers of rotation (StarCCM+) | Flap2 AOA silniej steruje siłami; min-drag okolice flap1≈0°, flap2≈6° (ich mapa) | [http://hdl.handle.net/10362/149236](http://hdl.handle.net/10362/149236) |
| Fluids 2026 sliding DRS + GNN | Sliding DRS + ducktail; surrogate GNN | CFD drag skrzydła 82,68→25,51 N (ich case); tor: +4,6% accel 50 m itd. | [doi:10.3390/fluids11020059](https://doi.org/10.3390/fluids11020059) |
| UMD Kuchar 2025/26 | 6-el. active (4 FW + 2 RW flaps), FSM | Ich claim: Cd 1,44→0,73; migracja CoP 78%→20% front — **FSAE**, Innovation Award | [DRUM item](https://drum.lib.umd.edu/items/239475f2-f580-4ad8-9f84-d99fe41c566c) |

Wspólny wniosek jakościowy: aktywny DRS rozwiązuje konflikt **DF w zakręcie ↔ drag na prostej** i może też **migrować balans**. To jest atrakcyjne na Endurance/Autocross z krótkimi prostymi — ale **u nas ruchomy DRS jest OUT** decyzją Spec.

### 5.2 „Pasywny” DRS / low-drag pose bez aktuatora

W Spec: ruchomy OUT; ewentualnie tylko **pasywny** (jak testy 019/020 w KB). Interpretacja praktyczna:

- **Stała geometria low-drag** (klapy „otwarte” / mniejszy AOA) jako wariant setupu torowego — bez ruchu w czasie jazdy.
- Albo geometria, która **przy wyższym Re / innym napływie** naturalnie traci mniej (bez aktuatora) — to już wymaga własnego CFD; literatura aktywnego DRS nie daje gotowej recepty.

Nie przenosimy procentów ΔCd z Jacksona/MDPI na nasz pasywny wariant.

### 5.3 EU FS Rules 2026 — co wolno, a czego nie rozstrzygamy tu

Z lokalnego dumpa T8 ([fs-rules-2026-t8.md](fs-rules-2026-t8.md)):

- T 8 **nie** zawiera explicite zakazu „movable aerodynamic devices”.
- Obowiązują: envelope T 8.2 (także przy any suspension), sztywność T 8.3, zakaz kontaktu z torem T 2.2.2, limit **500 W** urządzeń „designed to move air” T 11.11.1 (to o wentylatorach/ssaniu — nie to samo co serwo klapy, ale Scrutineering patrzy szeroko).
- Decyzja **DRS OUT** u nas = Spec (masa, fail-safe, czas, risk Q&A), nie „T8 automatycznie banuje”.

Dla poranka: nie inwestujemy nocy w CAD aktuatora; trzymamy się **H1 retune 3-el. + opcjonalny CAD 4-el. stały**.

---

## 6. Mapowanie na PUT (H1) — bez nowych liczb

| Pytanie | Stan wiedzy po tej nocy | Co zrobić dalej |
|---------|-------------------------|-----------------|
| 3 vs 4 el.? | 3-el. = default w Jackson/Staniszewski; 4-el. = wynik opt. Novais + ścieżka cascade LUT + praktyka UPC | CAD 4-el. w T8 envelope → **1 case CFD** vs 3-el. na 017 |
| Gap/overlap? | Start McBeath 1–4% / 1–6%; PUT 2D: overlap ~−30 mm peak, gap +5/+10 mm dobre | Seria 3–5 wariantów **na pakiecie**, nie izolacja |
| AOA? | Nie wchodzić w stall (~25° overall u Jacksona); main najpierw (Staniszewski) | Guardrail: \|Cz\|≥3,682, Cx≲1,23, balans w dół od 61,6% |
| DRS aktywny? | Literatura silnie za trade-off DF/drag | **OUT** Spec; max pasywny low-drag setup |
| Transfer liczb? | Zakaz | Żadnych Cl/Cd z Aveiro/LUT/Jackson jako targetów 017 |

---

## 7. Claims (claim | evidence | confidence)

Poniżej skrót twierdzeń z tej nocy — claim, skąd, pewność.

- Multi-element RW pozwala na wyższy AOA niż single-element przed stall | Jackson + McBeath (cyt.) | **high**
- Gap 1–4%c i overlap 1–6%c to **start**, nie optimum konkretnego profilu | Jackson cyt. McBeath | **high** (jako guideline)
- Na PUT 3-el. 2D: main↓ i overlap~−30 mm podnoszą \|Fz\|; na aucie 3D zysk może zniknąć | Staniszewski 2023 | **high**
- Optymalizacja Aveiro wybrała **4** airfoile | Novais abstrakt hdl:10773/33796 | **high** (fakt wyboru); transfer Δ na 017 | **low**
- LUT/Metropolia traktuje retune flaps/gaps i cascade jako dwie ścieżki decyzji EV FS | lutpub.lut.fi/10024/171732 | **med** (abstrakt; pełny PDF bot-wall w tej sesji)
- Aktywny DRS potrafi ściąć Cd skrzydła o dziesiątki % w publikacjach | Jackson; Fluids 2022 abstrakt | **high** (ich modele); nasz bolid | **n/a (OUT)**
- T8 2026 nie banuje explicite movable aero; decyzja OUT = Spec | fs-rules-2026-t8.md | **high**

---

## 8. Luki / PDF do dropu (dla Mikołaja)

1. Pełny PDF **LUT 171732** (bot-wall przy fetch) — doprecyzuje 3 vs cascade i czy są tabele Cl/Cd.
2. Pełny PDF **Novais** (TLS do ria.ua.pt padał w boxie) — geometria 4-el., gap/AOA, porównanie z 3-el.
3. PDF **MDPI Fluids 7(9):309** (CDN block) — aktuatory, Cd/Cl DRS.
4. Ewentualnie lokalne **019/020** (pasywny DRS) z OneDrive — żeby „pasywny” nie był pustym hasłem.

---

## Źródła (URL)

- Staniszewski 2023 — lokalnie `sources/staniszewski-2023-wing.md` (+ PDF w team jeśli wrzucony)
- Jackson 2018 — https://doi.org/10.5920/fields.2018.02
- Novais 2021 — http://hdl.handle.net/10773/33796 · https://ria.ua.pt/bitstream/10773/33796/1/Documento_Pedro_Novais.pdf
- LUT parametric RW — https://lutpub.lut.fi/handle/10024/171732
- Fluids DRS 2022 — https://doi.org/10.3390/fluids7090309
- NOVA DRS numerical — http://hdl.handle.net/10362/149236
- Sliding DRS + GNN — https://doi.org/10.3390/fluids11020059
- Merkel active aero — http://hdl.handle.net/10106/24176
- UMD active 6-el. — https://drum.lib.umd.edu/items/239475f2-f580-4ad8-9f84-d99fe41c566c
- FS Rules 2026 v1.1 — lokalnie `team/rules-current.pdf` / formulastudent.de
