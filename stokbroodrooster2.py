file = open('mstokbroodrooster.txt', 'r')
cont = file.read()
data = cont.split('!*!\n')[:-1]
data = [d.split('\n')[:-2] for d in data]
for d in data:
	d[0] = d[0][:d[0].find(':')]
	print(d)

begindag = cont[cont.find(':')+2:cont.find(' ',cont.find(':')+3)]
#print(begindag)

dagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag']

ind = dagen.index(begindag)

namen = [d.pop(0) for d in data]
alles = []

for i in range(5):
	#i += ind
	while i > 4: i -= 5
	#print(dagen[i])
	namenopdag = []
	for uur in range(1,8):
		namenopuur = []
		for j,naam in enumerate(namen):
			#print(j,naam)
			persoon = data[j]
			#input(persoon)
			if str(uur) in data[j][i]:
				namenopuur += [naam]
				#print(data[j])
				#print(data[j][i])
				#print(naam)
				#print(uur)
				#input()
		if not namenopuur == []:
			namenopdag += [(namenopuur,uur)]
	alles += [(namenopdag, dagen[i+ind if i+ind<=4 else i+ind-5])]

#[print(dagg[-1], *dagg[:-1]) for dagg in alles]

for dagg in alles:
	uren = []
	dag = dagg[-1]
	dagg = [*dagg[0]]
	print('\n'+dag)
	#print(dagg)
	uren = [uurr[1] for uurr in dagg]
	for i,uur in enumerate(uren):
		print(str(uur)+'e uur:')
		print(*dagg[i][0])
		#input()
