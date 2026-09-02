# Bramka Spec: seria 2D tylnego skrzydła (H1)

Po ludzku: kiedy wolno iść z wynikami 2D do decyzji CAD o kątach / overlap / szczelinie.

**Zakres:** ranking wariantów skrzydła w 2D.  
**Zakazane:** wpisywanie Cl/Cd z 2D na kartę całego auta (RWiter017).

Kolejność prac (zamknięta po recenzji raportu z Mikołajem):

1. **Spójny wall treatment** — y+ w zakresie **ok. 30–300** (jak Fluent EWT / Staniszewski), ten sam przepis na wszystkich siatkach.  
2. **Mesh study tej samej topologii** — **2–3 poziomy** gęstości (np. coarse / medium / fine), bez zmiany stylu warstw „po drodze”.  
3. **Dopiero potem** seria overlap → gap → kąty (albo kąty po ustabilizowaniu siatki — ale nie przed czystym mesh study).

---

## Kiedy bramka jest zielona (decyzja CAD)

Wszystko naraz:

1. Wall treatment spełniony (y+ ~30–300, spójnie).  
2. Mesh study domknięty: na 2–3 poziomach tej samej topologii widać, że **szum Cl (i sensownie Cd) między poziomami jest mały** względem kroku serii, który chcemy rozstrzygać.  
3. Ten sam setup dla punktów serii: skrzynka 800×500, V, turbulencja, Aref/Lref 2D, BC, **ta sama rodzina siatki**.  
4. Baseline 2D + każdy punkt jako **ΔCl i ΔCd** vs baseline (nie absoluty na auto).  
5. Zbieżność OK (albo punkt oznaczony „nieużywać”).  
6. **Δ wyraźnie większe niż szum meshu** — orientacyjnie: |ΔCl| między wariantami ma być wyraźnie powyżej skoku Cl między sąsiednimi siatkami (wcześniej ~8–14% to było za dużo względem sygnału kąta ~1–4%).  
7. Trend na ≥2 punktach, nie jeden wyskok.  
8. Kill: Cd↑ bez zysku docisku / stall / silne oscylacje — odpada mimo ładnego Cl.

Dopóki (1)–(2) nie są czyste — **kątów i G/O nie zatwierdzamy do CAD**, nawet jeśli kierunek wygląda „jak w literaturze”.

---

## Co wolno po zielonej bramce

- Wybrać **kierunek** kątów / overlap / gap do Fluent 3D na aucie.  
- Wybrać 1–2 warianty do porównania 4-el. albo case 3D.

## Czego nie wolno

- Cl/Cd 2D → `TARGETS.md` jako Cx/Cz bolidu.  
- „Na aucie będzie tyle samo ΔCz” bez Fluent / 3D.

## Po decyzji

Walidacja na aucie (Fluent): |Cz| ≥ 3,682, Cx około 1,23, balans w stronę 50/50.
