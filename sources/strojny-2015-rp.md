# Wykorzystanie technik szybkiego prototypowania przy budowie bolidu / Piotr Strojny / 2015 / krótki artykuł (Mechanik nr 3/2015; Politechnika Rzeszowska, Katedra Konstrukcji Maszyn)

## Cel pracy
Pokazanie zalet technik szybkiego prototypowania (RP) przy przygotowaniu modelu bolidu Formula Student oraz przy wytwarzaniu elementów funkcjonalnych pojazdu — w celu uniknięcia błędów montażowych/kolizyjnych, skrócenia czasu budowy i redukcji kosztów.

## Metody
- Projekt CAD bolidu (SolidWorks — literatura [1÷3]), następnie model fizyczny RP.
- Technologia: **FDM** (Fused Deposition Modeling).
- Model całego pojazdu w skali **1:10** (wszystkie planowane komponenty; silniki/różnicowy uproszczone do pełnych brył ze względu na minimalną grubość ścianek i brak potrzeby weryfikacji ich działania).
- Osobno poszycie w skali **1:12** — ocena wizualna.
- Elementy funkcjonalne 1:1: uchwyty kierownicy (inżynieria odwrotna + FDM), nos bolidu (FDM, formy), łopatki zmiany biegów (FDM).
- Inżynieria odwrotna uchwytu: odcisk dłoni kierowcy w glinie → skaner 3D → obróbka chmury punktów w SolidWorks → uniwersalny model CAD → druk FDM.

## Kluczowe liczby — tylko z tekstu
- Skala modelu całego bolidu: **1:10**
- Skala modelu poszycia: **1:12**
- Czas łączenia części modelu 1:10: **ok. 15 h** (zespół **ośmioosobowy**)
- Nos bolidu: podział na **cztery części** (ograniczona przestrzeń robocza drukarki), następnie scalenie z kadłubem
- Publikacja: **Mechanik nr 3/2015**, s. 260–261
- Dostęp do regulaminów / stron FS w literaturze: **22.07.2014**

*(Brak w tekście liczb aero: CL/CD, sił, prędkości, mas elementów — artykuł nie dotyczy aerodynamiki numerycznej.)*

## Geometria / konfiguracje
- Model RP 1:10 z stopniami swobody zbliżonymi do rzeczywistego bolidu → wykryto, że **zawieszenie nie spełnia założeń** → zmiana układu przedniego zawieszenia (amortyzatory u góry ramy pod innym kątem + układ krzywkowy vs model RP).
- Kolizja ramy z półosiami napędu → **częściowa zmiana kształtu ramy**.
- Ocena przestrzeni wewnętrznej → **zmiana układu fotela**.
- Nos: złożony kształt → druk FDM w 4 częściach + scalenie z kadłubem → kształt do wykonania form.
- Łopatki zmiany biegów przy kierownicy: złożona geometria + wymagana wytrzymałość; w tekście wspomniana wada łopatki z nieprawidłowego STL.
- Uchwyt kierownicy: uniwersalny względem dłoni różnych kierowców.

## Wnioski dla nowego pakietu aero FS
- Przed zamrożeniem geometrii pakietu aero / undertray / bodywork warto zrobić **fizyczny model skali** (FDM) całego bolidu — łapie kolizje ramy, napędu, zawieszenia i packaging fotela zanim powstaną formy/kompozyty.
- Złożone kształty nosa / elementów body: druk FDM jako **master do form** (podział na części wg volume drukarki).
- Elementy sterowania (łopatki, grip) da się tanio zrobić FDM 1:1, ale kontrolować jakość **STL** (wady geometrii przenoszą się na część).
- Reverse engineering dłoni kierowcy przyspiesza ergonomię cockpit — istotne przy ograniczonej przestrzeni wokół kierownicy i aero kokpitu.
- RP skraca czas i koszt poprzez eliminację poprawek **już zbudowanego** pojazdu — bezpośrednio wspiera iteracje pakietu aero.

## Ograniczenia
- Artykuł krótki (2 strony); brak danych ilościowych o wytrzymałości, tolerancjach, czasie druku, koszcie filamentu.
- Brak treści aerodynamicznej / CFD / tunelu.
- Uproszczenia komponentów w skali 1:10 (silniki, dyfer) — nie weryfikują funkcji, tylko packaging.
- Brak porównania FDM z innymi technologiami RP (SLA, SLS itd.).
- Wnioski jakościowe („wiele korzyści”, „redukcja wydatków”) bez liczb.

## Claims (claim | evidence | confidence)
| claim | evidence | confidence |
|---|---|---|
| Model FDM 1:10 ujawnił wady zawieszenia i wymusił redesign przedniego układu | Tekst: zawieszenie nie spełniało wymagań; Rys. 2 RP vs final | high |
| Model wykrył kolizję ramy z półosiami → zmiana kształtu ramy | Sekcja „Model fizyczny…” | high |
| Montaż modelu 1:10 zajął ~15 h ośmioosobowemu zespołowi | Bezpośrednio w tekście | high |
| Nos FDM (4 części) posłużył do uzyskania kształtu pod formy | Rys. 5 + opis | high |
| Połączenie RE + FDM dało funkcjonalny uchwyt kierownicy | Rys. 4 + opis | high |
| RP skróciło czas budowy i zredukowało koszty przez uniknięcie błędów late-stage | Wnioski | medium |
