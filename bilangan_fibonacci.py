angka = int(input('Jumlah bilangan : '))
x = 0;
awal = 1;
first = 1;
while (x < angka):
	keN = awal + first;
	fibonnanci = awal;
	awal = first;
	first = keN;
	print(fibonnanci)
	x += 1;
	pass