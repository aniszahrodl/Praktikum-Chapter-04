import math

jarakAB = 125
kecepatanAB = 62

jarakBC = 256
kecepatanBC = 70

jamBerangkatA = 6.00
lamaJamIstirahatB = 00.45

lamaPerjalananAB = jarakAB / kecepatanAB
p = round(lamaPerjalananAB)

jamTibaB = jamBerangkatA + p 

jamBerangkatB = jamTibaB + lamaJamIstirahatB 

lamaPerjalananBC = jarakBC / kecepatanBC
q = round(lamaPerjalananBC)

tibaC = jamBerangkatB + q 
print(tibaC)
