# Regulamin — boxy aero i możliwe loophole’y

**Dokument roboczy dla PUTM Aero.**  
Źródło: *Formula Student Rules 2026*, Version **1.1** (PDF skopiowany do `team/rules-current.pdf`; dump tekstowy: `fs-aero-kb/team/rules-raw.txt`).  
**Nie jest to zachęta do łamania ducha przepisów** — poniżej tylko luki / niejasności *w tekście* oraz typowe interpretacje zespołów, z oceną ryzyka Scrutineering.

**Flagi pewności:**  
- **H** = cytat reguły / wymiar wprost w PDF  
- **M** = wynika z połączenia kilku reguł / typowa praktyka FS, ale wymaga ostrożności  
- **L** = spekulacja / historia innych serii — nie opierać decyzji projektu

---

## Identyfikacja dokumentu

| Pole | Wartość | Pewność |
|------|---------|---------|
| Nazwa | **Formula Student Rules 2026** | H |
| Wersja | **1.1** (nagłówek stron PDF) | H |
| Seria | Formula Student (styl FS / FSG-like), **nie** FSAE Rules USA | H |
| Zakres aero | głównie **T 8** (+ T 2.1–T 2.4, T 11.11, T 11.12.3, T 1.1.18, T 3.19–T 3.20) | H |
| Changelog aero | T 8.2.1 v1.0: *„Changed height restriction”* (bez szczegółów poprzedniej wartości) | H |

**UWAGA (krytyczna):** przyszły sezon (2027+) może mocno zmienić envelope, DRS/active aero i limit wentylatorów. Ten brief dotyczy **tylko** PDF 2026 v1.1. Przed zamrożeniem CAD/CFD na kolejny sezon: nowy regulamin + Q&A oficjalne. **H**

---

## Wymiary / envelope (boxy)

Envelope aero **nie jest** stałym prostokątem „800×500 mm”. Jest **zestawem płaszczyzn względem opon / osi / head restraint / ziemi** (T 8.2 + Figure 14). Dodatkowo obowiązuje open-wheel keep-out (T 2.1.3) i min. prześwit 30 mm (T 2.2.1). **H**

### Tabela limitów

| Element | Wymiary / limity | Numer reguły | Cytat krótki | Pewność |
|---------|------------------|--------------|--------------|---------|
| **Front wing / aero przed head restraint** | Wysokość **&lt; 500 mm** od ziemi, przed pionową płaszczyzną przez *rearmost portion of the front face of the driver head restraint support* (bez padów, w pozycji najbardziej do tyłu) | T 8.2.1 | „…must be lower than 500 mm from the ground.” | H |
| **Aero przed osią przednią, outboard od most inboard point of front tire/wheel** | Wysokość **&lt; 250 mm** od ziemi | T 8.2.1 | „…must be lower than 250 mm from the ground.” | H |
| **Rear wing / aero za head restraint** | Wysokość **&lt; 1,1 m** od ziemi (Figure 14: 1100 mm) | T 8.2.1 | „…must be lower than 1.1 m from the ground.” | H |
| **Aero nisko (&lt;500 mm), za osią przednią** (sidepods / underbody / niski dyfuzor / niskie endplate’y) | Nie szersze niż pionowa płaszczyzna styczna do **most outboard point** opony/koła **przód i tył** | T 8.2.2 | „…must not be wider than a vertical plane touching the most outboard point of the front and rear wheel/tire.” | H |
| **Aero wysoko (&gt;500 mm)** (głównie RW + wysokie endplate’y) | Nie outboard od **most inboard point of the rear wheel/tire** | T 8.2.2 | „…must not extend outboard of the most inboard point of the rear wheel/tire.” | H |
| **Przedłużenie do tyłu** | Max **250 mm** za *rearmost part of the rear tires* | T 8.2.3 | „…not extend further rearward than 250 mm from the rearmost part of the rear tires.” | H |
| **Przedłużenie do przodu** | Max **700 mm** przed *fronts of the front tires* | T 8.2.3 | „…not extend further forward than 700 mm from the fronts of the front tires.” | H |
| **Warunek pomiaru envelope** | Koła prosto; **każdy** setup zawieszenia; z kierowcą i bez | T 8.2.4 | „…wheels pointing straight and with any suspension setup with or without a driver…” | H |
| **Open-wheel keep-out (wszystkie części, nie tylko aero)** | Strefa 75 mm przed/za OD opony (side view), bocznie od outside plane do inboard plane wheel/tire; widok boku koła bez przeszkód | T 2.1.3 + Fig. 4 | „No part of the vehicle may enter a keep-out-zone…” | H |
| **Min. ground clearance** | **30 mm** static (oprócz opon), z kierowcą; przy active suspension — w **najniższej** pozycji | T 2.2.1 | „minimum static ground clearance … must be 30 mm.” | H |
| **Sliding skirts / kontakt z torem** | Zakaz urządzeń, które *by design, fabrication or as a consequence of moving* kontaktują tor | T 2.2.2 | „Sliding skirts or other aerodynamic devices … contact the track surface are prohibited.” | H |
| **Bodywork przed cockpit opening, poza obszarem T 8.2** | Brak zewnętrznych wklęsłych promieni w side section view; szczeliny minimalne | T 2.3.2 | „…no external concave radii of curvatures.” | H |
| **Promienie krawędzi aero/bodywork** | ≥3 mm forward-facing; ≥1 mm pozostałe (krawędzie mogące trafić pieszego bez sięgania do auta) | T 2.4.1 | „minimum radius … 3 mm … and 1 mm …” | H |
| **Nose / bodywork przed kołami (tangent &gt;45°)** | Promień ≥38 mm (top/sides/bottom affected edges) | T 2.3.4 | „…radius of at least 38 mm…” | H |
| **Sztywność aero** | 200 N / ≥225 cm² → ugięcie ≤10 mm w kierunku obciążenia; 50 N w dowolnym kierunku w dowolnym punkcie → ugięcie ≤25 mm | T 8.3.1–T 8.3.2 | „…not deflect more than 10 mm… / …25 mm.” | H |
| **Max szerokość / wysokość / długość całego pojazdu** | **Brak** osobnego limitu „vehicle max width/height/length” w sekcji aero; szerokość wynika z opon + T 8.2; wheelbase ≥1525 mm; track ratio ≥75% | T 8.2, T 2.9.1–2 | — | H |
| **Aero/sensory przed AIP** | Attachment point chassis **za** AIP; IA+non-crushable ≤ peak T 3.19.1 / 120 kN (metody w T 3.19.4) | T 3.20.2, T 3.19.4 | „chassis attachment point must be located rearward of the AIP.” | H |
| **Sensory / kamery / elektr.** | W surface envelope (T 1.1.18) **lub** „within the box defined in T 8.2” | T 11.12.3 | „…or within the box defined in T 8.2.” | H |

### Osobno: box 800×500 mm

**Nie występuje** jako box endplate / wing / aero w tym PDF. **H**

- Jedyne „800 mm” znalezione w dumpie: limit powierzchni podłogi wózka TSAC (**EV 8**, nie aero).  
- Regulamin używa słowa **„box defined in T 8.2”** (T 11.12.3) na **envelope z T 8.2 / Fig. 14**, a nie na prostokąt 800×500.  
- Jeśli zespół pamięta 800×500 z **FSAE Rules** lub starszych lat FS — **nie przenosić** na ten dokument bez nowego PDF. **H** / kontekst historyczny **L**

---

## Ruchome elementy / DRS / active aero — co wolno / zakazane

| Temat | Status w tekście 2026 v1.1 | Reguła | Pewność |
|-------|----------------------------|--------|---------|
| **DRS / ruchome skrzydła / active aero** | **Brak explicite zakazu** „movable aerodynamic devices” w T 8 | — (cisza w T 8) | H (cisza) |
| Kontakt aero z torem (sliding skirts itd.) | **Zakazane** | T 2.2.2 | H |
| Envelope przy ruchu zawieszenia | Musi być spełniony przy **any suspension setup** | T 8.2.4 | H |
| Ugięcia / „miękkie” aero | Limit ugięć pod 200 N / 50 N | T 8.3.1–2 | H |
| Active suspension | Dozwolone; prześwit mierzony w najniższej pozycji | T 2.2.1 | H |
| Actuatory CGS / HPHS (np. pneumo/hydro DRS) | Dozwolone pod T 9, ale **całość CGS/HPHS + mountings w rollover protection envelope** (T 1.1.16) | T 9.2.2 | H |
| Push / skrzydła | Przy pchaniu: 2 osoby przy front wing | A 6.6.8 | H |

### One-liner DRS (dla leadu)

**W FS Rules 2026 v1.1 DRS nie jest wprost zakazany w T 8; legalność to „cisza regulaminu + T 2.2.2 / T 8.2.4 / T 8.3 / T 9”, więc decyzja = TBD z Q&A / Scrutineering, nie „automatycznie OUT”.** **H** (cisza) / ryzyko interpretacji **M**

---

## Powered aerodynamics / fans / blown — status

| Temat | Status | Reguła | Cytat / sens | Pewność |
|-------|--------|--------|--------------|---------|
| **Active devices designed to move air** (w tym cooling fans) | **Dozwolone**, łączna moc znamionowa **≤ 500 W** | T 11.11.1 | „maximum combined total rated power … 500 W, this includes cooling fans but does not apply to CV 1.8.” | H |
| Blown diffuser / suction fan aero | **Nie zakazane osobno** — mieszczą się w limicie 500 W *jeśli* uznane za „active devices designed to move air” | T 11.11.1 | — | H (tekst) / duch przepisów **M** |
| Turbo/supercharger CV | Wyłączone z limitu 500 W | T 11.11.1 → CV 1.8 | — | H |
| Finger guards (obroty na postoju) | Osłony; mesh nie przepuszcza obiektu Ø12 mm | T 7.3.5 | Relevant dla wentylatorów | H |
| Rain Test (EV) | Changelog: wentylatory **włączone** podczas Rain Test | IN 9 / changelog IN 9.2.1 | — | H (changelog) |

**Wniosek dla nas:** fan **nie jest zakazany regulaminem** — jest **limitowany mocą**. Decyzja „fan OUT” to decyzja pakietu/osiągów (Michalecki), nie hard ban z T 8. **H**

---

## Możliwe loophole’y aerodynamiczne

Tylko rzeczy wynikające z luk/niejasności **tekstu**. Nie zachęcamy do omijania ducha FS / intencji sędziów.

### 1. Definicja „aerodynamic device” vs mounting vs bodywork
- **Reguły:** T 8.1.1, T 1.1.2  
- **Niejednoznaczne:** Mounting „is not regarded as an aerodynamic device, unless it is intentionally designed to be one”; bodywork = outermost surface / fairings / covers. Granica: pylon/strut „tylko struktura” vs profil nośny; undertray jako „podłoga / bodywork” vs „aero device”.  
- **Typowa interpretacja:** wszystko, co wygląda na skrzydło/dyfuzor/endplate/sidepod aero → T 8.2; czyste mocowania rurowe często poza limitem szerokości/wysokości RW, ale sędziowie pytają o „intentional aero”.  
- **Ryzyko Scrutineering:** **średnie–wysokie** przy agresywnych „structural” endplate’ach / szerokich pylonach. **M**

### 2. Cisza o DRS / movable aero
- **Reguły:** brak zakazu w T 8; ograniczenia T 2.2.2, T 8.2.4, T 8.3, ewentualnie T 9  
- **Niejednoznaczne:** czy ruchomy element w envelope jest OK przez cały zakres ruchu; czy ugięcie pod obciążeniem aerodynamicznym ≠ „deflection” z T 8.3 (T 8.3 to load cases testowe, nie „downforce in corners”).  
- **Typowa interpretacja:** część zespołów FS buduje DRS / driver-adjustable flaps; część woli fixed + setup pits; FSAE USA bywa surowsze — **nie mylić serii**.  
- **Ryzyko:** **średnie** (pytania o fail-safe, pozycje w boxie, CGS poza envelope). Bez oficjalnego Q&A = **nie bazować sezonu na DRS**. **M**

### 3. Powered aero w limicie 500 W
- **Reguła:** T 11.11.1  
- **Niejednoznaczne:** „designed to move air” obejmuje cooling **i** aero; brak rozróżnienia „tylko chłodzenie”. „Rated power” — sumowanie znamionowe vs chwilowe.  
- **Typowa interpretacja:** cooling fans OK; blown/suction bywa dyskutowane jako „spirit”, ale tekst pozwala do 500 W łącznie.  
- **Ryzyko:** **średnie** (dokumentacja mocy, Rain Test ON, bezpieczeństwo wirników). Dla nas i tak **fan OUT**. **H**/**M**

### 4. Płaszczyzna szerokości „front and rear wheel/tire” (T 8.2.2)
- **Reguła:** T 8.2.2 bullet 1  
- **Niejednoznaczne:** jedna płaszczyzna styczna do most outboard przód **i** tył (przy różnym track / rozstawie) — geometria „ściętego” boxu między osiami; opona vs felga; ugięcie zawieszenia (ale T 8.2.4 wymaga compliance we wszystkich setupach).  
- **Typowa interpretacja:** sidepods/underbody w obrysie opon; przy węższym tyle box się zwęża do tyłu.  
- **Ryzyko:** **niskie–średnie** (miara taśmą przy Tech; opony/ciśnienie). **H**/**M**

### 5. Próg 500 mm: „lower/higher than 500 mm” i szerokość
- **Reguły:** T 8.2.1–2  
- **Niejednoznaczne:** element przecinający 500 mm (endplate, wing root) — która reguła szerokości; „lower than” / „higher than” vs „≤”.  
- **Typowa interpretacja:** część powyżej 500 mm musi spełniać wąski box (inboard rear tire); część poniżej — box opon.  
- **Ryzyko:** **średnie** przy wysokich endplate’ach RW/FW transition. **M**

### 6. Head-restraint plane jako granica 500 mm vs 1,1 m
- **Reguła:** T 8.2.1  
- **Niejednoznaczne:** „rearmost portion of the front face” head restraint support, bez padów, most rearward position — zależne od setupu fotela/HR. Sidepods / canopy / beam wing wokół tej płaszczyzny.  
- **Typowa interpretacja:** wszystko przed HR support front face → max 500 mm; za → do 1,1 m.  
- **Ryzyko:** **średnie** (pomiar HR na Tech). **H**/**M**

### 7. Open-wheel keep-out vs endplate / bargeboard (T 2.1.3)
- **Reguła:** T 2.1.3 + Fig. 4  
- **Niejednoznaczne:** „inboard plane of the wheel/tire assembly”; elementy między kołami vs w strefie 75 mm fore/aft OD.  
- **Typowa interpretacja:** zero części w keep-out; wheel must be unobstructed from side.  
- **Ryzyko:** **wysokie** przy agresywnych wheel fence / podcięciach — łatwy fail Tech. **H**

### 8. T 2.3.2 concave bodywork vs underbody / intake
- **Reguła:** T 2.3.2 (+ wyjątek obszaru T 8.2)  
- **Niejednoznaczne:** co jest „outside the area defined in T 8.2”; side section view; gap „reduced to a minimum”.  
- **Typowa interpretacja:** wklęsłości aero tylko tam, gdzie T 8.2 pozwala traktować powierzchnię jako aero; czysty bodywork przed kokpitem — bez concave.  
- **Ryzyko:** **średnie**. **M**

### 9. Ground effect blisko 30 mm + T 2.2.2
- **Reguły:** T 2.2.1–2, T 8.2.4  
- **Niejednoznaczne:** ugięcie podłogi pod load vs „consequence of moving, contact the track”; static 30 mm vs dynamic rake.  
- **Typowa interpretacja:** static ≥30 mm we wszystkich setupach; zero designu „ma ocierać”.  
- **Ryzyko:** **wysokie** przy bardzo niskim UT. **H**/**M**

---

## Implikacje dla naszego pakietu (RWiter017 baseline, cel max DF + balans ~50/50, fan OUT, DRS TBD)

| Decyzja / element | Implikacja z 2026 v1.1 | Pewność |
|-------------------|------------------------|---------|
| **RWiter017** jako kotwica | RW musi być **&lt;1,1 m**, **≤250 mm** za tylnymi oponami, szerokość **≤ most inboard rear tire** (bo &gt;500 mm). Endplate’y wysokie = wąski box. | H |
| **Max DF** | Envelope pozwala na duży RW + UT w boxie opon; limitem praktycznym są T 8.3 (sztywność), keep-out kół, 30 mm GC, IA przy FW. | H/**M** |
| **Balans ~50/50** (cofanie DF z przodu) | FW ograniczony do **&lt;500 mm** (i **&lt;250 mm** outboard przed osią); UT/sidepods w boxie opon; RW wąski ale wysoki — typowa droga do cofnięcia balansu = więcej RW/UT, mniej FW / inne ustawienie. | H/**M** |
| **Fan OUT** | Zgodne z celem zespołu; **regulamin fanów nie banuje** (≤500 W). Nie ma presji „musimy mieć fan bo konkurencja legalnie może” — ale konkurencja *może* do 500 W. | H |
| **DRS TBD** | Tekst **nie zamyka** tematu. Przed IN: (1) potwierdzić Q&A, (2) cały ruch w T 8.2, (3) unikać CGS/HPHS poza rollover envelope, (4) T 8.3 w obu pozycjach. Do czasu Q&A — nie blokować CFD fixed RW; DRS jako opcjonalna gałąź. | M |
| **FW daleko do przodu** | Max 700 mm przed front tires; attachment za AIP; dowód IA+non-crushable (T 3.19.4). | H |
| **Undertray / dyfuzor** | Traktować jako aero → T 8.2.2 (szerokość opon), GC 30 mm, vent holes T 2.3.3 jeśli enclosed, zero kontaktu z torem. | H |
| **Wąsy / wheel aero** | Wysokie ryzyko T 2.1.3 keep-out — projektować z dużym marginesem. | H |

---

## Co NIE wynika z tego PDF / wymaga nowego regulaminu

1. **Box 800×500 mm** (FSAE-style) — **brak** w FS 2026 v1.1.  
2. **Explicite „DRS legal / illegal”** one-liner od oficjeli — tylko cisza T 8; potrzeba **Rules Q&A** sezonu startu.  
3. **Zmiany 2027+** (changelog już ruszał T 8.2.1 height) — przyszły PDF może być „mocno inny”.  
4. **Limit mocy fanów inny niż 500 W**, rozróżnienie cooling vs aero — nie ma; ewentualne nowe zasady.  
5. **Max vehicle width/height/length** jako stałe mm poza envelope opon/T 8.2 — nie podane.  
6. **Konkretne wymiary naszego CAD** (track, HR position, tire OD) — limity są *względne*; liczby mm boxu na aucie = pomiar z modelu, nie z PDF.  
7. **FSAE USA / inne serie** — nie stosować zamiennie.  
8. **Event-specific rules** (FSG/FSEV addenda, skrzynie Tech) — poza tym PDF.

---

## Szybkie odniesienia (do cytowania na review)

- T 8.1.1 — definicja aerodynamic device / mounting  
- T 8.2.1–4 + Fig. 14 — envelope  
- T 8.3.1–2 — sztywność  
- T 2.1.3 — open wheel keep-out  
- T 2.2.1–2 — GC 30 mm, zakaz kontaktu z torem  
- T 2.3.2 / T 2.4.1 — concave / edge radii  
- T 11.11.1 — fans ≤500 W  
- T 11.12.3 — „box defined in T 8.2”  
- T 9.2.2 — CGS/HPHS w rollover envelope  

*Koniec briefu. Źródło: Formula Student Rules 2026 Version 1.1. Nie wymyślano wymiarów spoza PDF.*
