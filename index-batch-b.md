# Index — batch B (FS aero KB)

## michalecki-fan-ground-effect.md

Jakub Michalecki (PP, 2024) bada CFD wentylator odsysający spod podłogi bolidu PM08.
Na profilowanej podłodze docisk spada (ok. **30%+** vs Cz = **−2,036**).
Na płaskiej podłodze z kanałami i kurtynami |Cz| rośnie (best iter107: Cz = **−1,589**).
Wniosek: obecne wyniki nie uzasadniają wdrożenia na zoptymalizowanym undertrayu bez dalszego redesignu lokalizacji, RPM i geometrii kanałów.

## jackson-2018-cfd-drs.md

Frankie Jackson (Huddersfield, 2018) optymalizuje CFD (CFX, k-ε) 3-elementowe skrzydło tylne E423 z DRS.
Wyniki na ich modelu:

- z CL = **+0,21** / CD = **0,71**
- do CL = **1,15** / CD = **1,21** (DRS closed)
- oraz CL = **0,26** / CD = **0,79** (DRS open)

Predykcje: +**3,1%** cornering (R = 13 m), −**35%** drag force i +**15,7%** accel @ 25 m/s z DRS, Vmax +**18,2%** vs fixed high-DF.
FSAESim **5,31 s** vs tor **5,49 s** (ok. **97%**).

## strojny-2015-rp.md

Piotr Strojny (Mechanik 3/2015) opisuje FDM w budowie bolidu FS.
Model 1:10 (ok. **15 h** montażu, **8** osób) wykrył błędy zawieszenia, kolizje ramy z napędem i packaging fotela.
Osobno: poszycie 1:12 oraz funkcjonalne elementy 1:1 (nos 4-częściowy, grip RE+FDM, łopatki).
Artykuł bez liczb aero — wartość dla procesu iteracji geometrii przed formami i kompozytami.
