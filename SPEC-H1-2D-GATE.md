# Kryterium Spec: kiedy seria 2D H1 wystarczy do decyzji kątów / gap / overlap

**Zakres:** tylko ranking wariantów tylnego skrzydła w 2D (kąty, overlap, szczelina).  
**Poza zakresem:** przenoszenie Cl/Cd z 2D na kartę RWiter017 (całe auto) — **zakazane**.

## Seria jest wystarczająco wiarygodna do decyzji, gdy spełnione jest wszystko naraz

1. **Ten sam setup** dla wszystkich punktów: ta sama skrzynka (800×500), V, model turbulencji, Aref/Lref 2D, siatka z tego samego przepisu, te same BC.  
2. **Baseline 2D** policzony i zapisany; każdy punkt ma **ΔCl i ΔCd** względem tego baseline’u (nie same absoluty).  
3. **Zbieżność / jakość:** residua usiadły albo jasno oznaczony punkt „nieużywać”; checkMesh bez hard fail; bez oczywistego crashu / divergencji.  
4. **Powtórka:** przynajmniej jeden punkt (np. baseline albo najlepszy kandydat) policzony drugi raz / sąsiedni krok siatki — różnica ΔCl i ΔCd mała względem kroku serii (orientacyjnie: zmiana między wariantami powinna być wyraźnie większa niż szum powtórki).  
5. **Trend, nie szum:** wybieramy wariant tylko gdy poprawa ΔCl (albo ΔCl/ΔCd) jest **powtarzalnym kierunkiem** na ≥2 sąsiednich punktach sweepu, nie pojedynczym „wyskokiem”.  
6. **Kill:** jeśli |ΔCd| rośnie mocniej niż zysk docisku bez uzasadnienia (np. stall / oscylacje) — punkt odpada mimo ładnego Cl.

## Co wolno zdecydować po spełnieniu bramki

- Który **kierunek** kątów / overlap / gap brać dalej do CAD / Fluent 3D na aucie.  
- Które 1–2 warianty zasługują na **jedno porównanie 4-el.** albo na case 3D.

## Czego nadal nie wolno

- Wpisywać Cl/Cd 2D do `TARGETS.md` jako Cx/Cz bolidu.  
- Twierdzić „na aucie będzie ΔCz = …” bez Fluent / 3D na pakiecie.

## Po decyzji

Zostaje walidacja na aucie (Fluent): te same kierunki geometrii, metryki z karty — |Cz| ≥ 3,682, Cx około 1,23, balans w stronę 50/50.
