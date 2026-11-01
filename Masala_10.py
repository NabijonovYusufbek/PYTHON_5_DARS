narxlar = [8000, 12000, 18000, 25000, 9000, 30000]

Qimmat = list(filter(lambda narx: narx > 15000,narxlar))

print(list(map(lambda narx: narx - 3000,Qimmat)))