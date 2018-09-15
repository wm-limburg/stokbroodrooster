file = open('mstokbroodrooster.txt', 'r')
cont = file.read()
data = cont.split('!*!\n')[:-1]
data = [d.split('\n')[:-2] for d in data]
for d in data:
	d[0] = d[0][:d[0].find(':')]
	print(d)

begindag = cont[cont.find(':')+2:cont.find(' ',cont.find(':')+3)]

dagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag']

ind = dagen.index(begindag)

namen = [d.pop(0) for d in data]
alles = []

for i in range(5):
	namenopdag = []
	for uur in range(1,8):
		namenopuur = []
		for j,naam in enumerate(namen):
			persoon = data[j]
			if str(uur) in data[j][i]:
				namenopuur += [naam]
		if not namenopuur == []:
			namenopdag += [(namenopuur,uur)]
	alles += [(namenopdag, dagen[i+ind if i+ind<=4 else i+ind-5])]

for dagg in alles:
	uren = []
	dag = dagg[-1]
	dagg = [*dagg[0]]
	print('\n'+dag)
	uren = [uurr[1] for uurr in dagg]
	for i,uur in enumerate(uren):
		print(str(uur)+'e uur:')
		print(*dagg[i][0])
