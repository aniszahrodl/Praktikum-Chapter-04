import math
tarif1 = 200000
tarif2 = 10000
jamMulai = 6
menitMulai = 0
jamSelesai = 23
menitSelesai = 50
lamaSewa = (jamSelesai - jamMulai)+(menitSelesai-menitMulai)/60
a = math.ceil(lamaSewa)
b = (tarif2)*(a)
totalTarif = (tarif1)+(b)
print(totalTarif)
