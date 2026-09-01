# Aerodynamic optimisation of Formula student vehicle using computational fluid dynamics / Frankie F. Jackson / 2018 (publ. 21.02.2018; accepted 08.11.2017) / artykuł naukowy (University of Huddersfield)

## Cel pracy
Poprawa zewnętrznej aerodynamiki bolidu Formula Student University of Huddersfield 2017 poprzez wieloelementowe skrzydło tylne z regulowanymi elementami (DRS), aby zwiększyć prędkość w zakrętach oraz przyspieszenie / prędkość maksymalną na prostych.

## Metody
- CFD: ANSYS CFX; RANS + standard **k-ε**; przepływ nieściśliwy, izotermiczny (**25 °C**); RMS residual target **1×10⁻⁴**.
- Model bazowy: uproszczony 1:1 bolidu **Huddersfield 2014** (model 2017 niepełny; wymiary zbliżone); usunięte detale zawieszenia.
- Domenа: skalowanie jak Franck et al. (Ahmed): **4540 × 3027 × 30270 mm** (X,Y,Z); inlet **26,8 m/s (60 mph)**; outlet static pressure **0 Pa**; free-slip na ścianach domeny; no-slip na pojeździe.
- Mesh independence: finalna siatka bazowa **933 024** elementów, min. sizing **4 mm**, growth rate **1,20**; z tylnym skrzydłem **1 669 602** elementów.
- Optymalizacja wolnego strumienia skrzydła (symmetry → siły ×2); potem montaż na pojeździe (DRS closed / open).
- Predykcje osiągów: równania cornering / top speed / acceleration (McBeath, Wordley & Saunders); walidacja FSAESim vs wynik torowy Hungary 2017.
- Silnik w modelu przyspieszenia: **KTM EXC 500** (dane dynamometryczne zespołu z 2012); rozkład masy założony **35:65** przód:tył; μ opon w zakresie **0,8–1,2**.

## Kluczowe liczby — tylko z tekstu
**Baseline (bez urządzeń aero):**
- CL = **0,21** (dodatni — lift); CD = **0,71**
- Siła oporu użyta do CD: **277,6 N** (oś Z w notacji pracy)
- Porównanie CD z Monash FSAE 2005 (CD=0,83): podobieństwo **86%**

**Skrzydło tylne — geometria:**
- Max chord **c = 860 mm**, span **s = 920 mm** (limit regulaminowy wykorzystany w pełni)
- 3 elementy, profil **E423**: main **540 mm**; Flap 1 & 2 po **180 mm**; overlap **26,25 mm**; gap **20 mm**
- Wybrane AOA: Study No. **4** — Flap1 **28°**, Flap2 **60°**, overall AOA **22,81°** (stall wskazany przy ~25°)
- Montaż: góra endplate **1200 mm** od ziemi; tylna ściana endplate **250 mm** za tylnymi kołami

**Pojazd + skrzydło:**
| Konfiguracja | CL | CD | A czołowa |
|---|---:|---:|---:|
| DRS closed (high DF) | **1,15** (ujemny Y = downforce) | **1,21** | **1,18 m²** |
| DRS open (low drag) | **0,26** (DF) | **0,79** | **0,99 m²** |

**Osiągi (teoretyczne):**
- Redukcja siły oporu DRS open vs closed: **35%**
- Max cornering speed (+skrzydło closed vs baseline): **+3,1%** przy R = **13 m**
- V_max: baseline **53,62 m/s**; DRS closed **40,86 m/s**; DRS open **49,94 m/s** → DRS open **+18,2%** vs closed
- Potencjał przyspieszenia przy **25 m/s**: **+15,7%** z DRS open
- Acceleration 75 m: FSAESim **5,31 s** vs tor Hungary 2017 **5,49 s** → podobieństwo **96,7%** (abstract: „97%”)

**Tabela AOA (Study 0–5):** Flap1 20→29°, Flap2 20→70°, overall 13,80→24,71°.

## Geometria / konfiguracje
- Wieloelementowe RW: main + 2 flaps (E423), gap/overlap wg wytycznych McBeath (1–4%c / 1–6%c).
- DRS: regulowane tylne elementy — pozycja closed (max DF) vs open (min drag / mniejsza powierzchnia czołowa).
- Na pojeździe: front wing, side pods i diffuser wspomniane jako część pakietu 2017 (Rys. 1), ale w pracy CFD optymalizowane jest głównie tylne skrzydło; balance aero z front wing zaniedbany na tym etapie.
- Sześć wariantów AOA w free-stream; wybór Study 4 przed stall.

## Wnioski dla nowego pakietu aero FS
- Multi-element RW + DRS daje duży skok \|CL\| (0,21 lift → 1,15 DF) kosztem CD (0,71 → 1,21); DRS open przywraca CD ≈ **0,79** — kluczowe na krótkich prostych FS.
- Montować RW **jak najwyżej**, by uniknąć disturbed flow za głową kierowcy / roll hoop / air intake.
- Overall AOA ~**23°** (flaps 28°/60°) jako punkt wysokiego DF przed stall (~25°) — nie pchać AOA do stall „dla liczb”.
- DRS warto projektować równolegle z predykcją acceleration (traction-limited → power-limited); zysk **~16%** a przy 25 m/s jest istotny dla eventów accel/endurance.
- Walidacja CD względem literatury + FSAESim vs tor zwiększa wiarygodność pipeline’u CFD→osiągi.
- Na torach FS z wieloma zakrętami: DF w zakręcie + DRS na prostej = typowy trade-off wart wdrożenia, jeśli regulamin pozwala na ruchome elementy.

## Ograniczenia
- Model 2014 zamiast finalnego 2017; uproszczenia geometrii (brak zawieszenia).
- Optymalizacja AOA w free-stream — założenie, że optimum przenosi się na pojazd.
- Balance / stabilność z front wing pominięte; DF założony tylko na tylne koła.
- Mesh DRS-open: gorsza zbieżność DF (ograniczenia mocy obliczeniowej); fokus na drag (1% discrepancy).
- Brak pełnej walidacji tunelowej własnego modelu; porównanie CD z innym bolidem (Monash) tylko orientacyjne.
- Clutch slip i rolling resistance zaniedbane w modelu przyspieszenia.

## Claims (claim | evidence | confidence)
| claim | evidence | confidence |
|---|---|---|
| RW closed poprawia CL z +0,21 do −1,15 i podnosi CD z 0,71 do 1,21 | Abstract + Results (frontal area 1,18 m²) | high |
| DRS open obniża CD do 0,79 i CL DF do 0,26 (A=0,99 m²) | Results / Conclusions | high |
| DRS open redukuje siłę oporu o 35% vs closed | Eq. 3 + tekst Results | high |
| Optimum multi-element przed stall: overall AOA 22,81° (flaps 28°/60°), E423 | Table 2 + Figure 7 discussion | high |
| Cornering +3,1% przy R=13 m; accel +15,7% @ 25 m/s; Vmax DRS +18,2% vs fixed high-DF | Abstract / Conclusions | high |
| Predykcja accel 75 m (5,31 s) zgadza się z Hungary 2017 (5,49 s) w ~97% | FSAESim vs track | medium |
| Baseline CD=0,71 ma ~86% podobieństwa do Monash WT CD=0,83 | Validation paragraph | medium |
