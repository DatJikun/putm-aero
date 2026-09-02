# Protokół 2D OpenFOAM — tylne skrzydło

**Status: ZAPARKOWANE** (wrzesień 2026).  
Nie odpalamy nowych runów 2D, dopóki zespół świadomie nie wróci do tego toru. Aktualna kampania to Fluent H1 na aucie: `SPEC-FLUENT-H1-RWITER017.md`.

---

## Po co ten plik

To **przyszła instrukcja**: jak wrócić do wiarygodnej serii 2D w OpenFOAM, bez powtórki chaosu (mieszane przepisy siatki, y+ poza wall-fn, Cd „niezależny” od niczego).

Szczegóły bramki decyzji: `SPEC-H1-2D-GATE.md`.

---

## Kolejność (obowiązkowa)

1. **Jeden wall treatment** — funkcje ściankowe, y+ w zakresie ok. **30–300**, ten sam przepis na LE/TE i obu slotach. Nie mieszać „bez warstw” z „z warstwami” między poziomami siatki.  
2. **Czyste mesh study** — **2–3 klony tej samej topologii**; zmienia się głównie rozmiar komórki. Raportuj Cl/Cd, y+, Δ między poziomami oraz plateau / średnią kroczącą (nie tylko last-200).  
3. **Dopiero potem gap / overlap**.  
4. **Dopiero potem kąty**.

Dopóki (1)–(2) nie są czyste — **nie stroimy geometrii** i **nie proponujemy CAD**.

---

## Zakazy

- Absolutów Cl/Cd z 2D **nie wpuszczać** na kartę całego auta (`TARGETS.md` / RWiter017).  
- Nie porównywać na ślepo Cl 3-el. vs 4-el. ani vs Fluent pojazdu (inne Aref/Lref/geometria).  
- Nie traktować skoku Cl między różnymi przepisami siatki jako „niezależności od meshu”.

---

## Co wolno raportować

- **ΔCl / ΔCd** względem baseline 2D przy **tej samej** rodzinie siatki.  
- Kierunek trendu (np. „wyższy main → stall / Cd↑”) jako hipoteza pod Fluent na aucie — dopiero po zielonej bramce `SPEC-H1-2D-GATE.md`.

---

## Linki

- Bramka Spec: [`../SPEC-H1-2D-GATE.md`](../SPEC-H1-2D-GATE.md)  
- Kampania Fluent (aktywna): [`../SPEC-FLUENT-H1-RWITER017.md`](../SPEC-FLUENT-H1-RWITER017.md)  
- Cele auta: [`../TARGETS.md`](../TARGETS.md)
