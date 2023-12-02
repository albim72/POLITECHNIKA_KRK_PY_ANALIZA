from pojazd import Pojazd

p1 = Pojazd()
odl = 567
lt = 51
cen_l = 6.32

print(f'spalanie [l/100km]: {p1.spalanie(odl,lt):.2f}')
print(f'koszt przejazdu na odcinku {odl} km wynosi {p1.kosztyprzejazdu(odl,lt,cen_l):.2f} zł')