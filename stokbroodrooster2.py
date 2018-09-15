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

tekst = '''<head>
<style>
th, td {
	padding: 5px;
	text-align: left;
}
caption {
	padding: 5px;
	text-align: left;
}
</style>
</head>
'''

for dagg in alles:
	dag = dagg[-1]
	dagg = [*dagg[0]]
	print('\n'+dag)
	tekst += '<table>\n<caption>'+dag+'</caption>\n'
	uren = [uurr[1] for uurr in dagg]
	for i,uur in enumerate(uren):
		tekst += '<tr>'
		tekst += '<th>'+str(uur)+'</th>'
		tekst += '<th>'
		for ding in dagg[i][0]:
			tekst += ding + ', '
		tekst = tekst[:-2]
		tekst += '</th>'
		tekst += '</tr>\n'
		print(str(uur)+'e uur:')
		print(*dagg[i][0])
	tekst += '</table>\n'

print(tekst)
file = open('stokbrooster2.html', 'w')
file.write(tekst)
file.close()