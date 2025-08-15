MCNPTools Ptrac Example 1
c
501 601 -1.87276e+1 -401      imp:n=1
502 602 -9.98207e-1  401 -402 imp:n=1
503 603 -1.20500e-3  402 -403 imp:n=1
999 0              403      imp:n=0

c
401 so 5
402 so 6
403 so 7

mode n p e
c
sdef PAR=n ERG=14
nonu
c
m601       92234     0.009849 $ Uranium, HEU, U.S. Average
         92235     0.932166 $ Density: 18.724760 g/cc
         92236     0.004484 $ Composition & Density from PNNL-15870, Rev. 1
         92238     0.053501
c
m602        1001     0.666657 $ Water, Liquid @ 23.15 deg-C
          8016     0.333343 $ Density: 0.998207 g/cc
mt2 lwtr.10                 $ Composition & Density from PNNL-15870, Rev. 1
c
m603        6000     0.000150 $ Air (Dry, Near Sea Level)
          7014     0.784431 $ Density: 0.001205 g/cc
          8016     0.210748 $ Composition & Density from PNNL-15870, Rev. 1
         18000     0.004671
c
f4:n 501
e4 0.01 0.1 1 2 3 4 5 6 7 8 9 10 11 12 13 14
c
c rand gen=2 seed=12345
prdmp 2j 1 $ Write MCTAL file at conclusion of calculation
ptrac file=asc write=all $ Write PTRAC file
print
nps 1000
