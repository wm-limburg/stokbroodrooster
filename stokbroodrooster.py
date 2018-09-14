#Created by Bas het Beest
#©CPL Code Productions

def ontleed_rooster(rooster):
		vorig_enter = 0
		regel_lijst = []
		for line in range(7):
				enter = rooster.find("\n", vorig_enter+1)
				regel = rooster[vorig_enter:enter+1]
				if regel.find("[") != -1:
						#print(regel)
						regel = regel[2:len(regel)-2]
						#print(regel)
				else:
						regel = regel[:len(regel)-2]
				vorig_enter = enter
				regel_lijst += [regel]
		userinfo = regel_lijst[0]
		eind = userinfo.find(":")
		user = userinfo[:eind]
		return regel_lijst, user

def main_loop():
		file = open("mstokbroodrooster.txt", "r")
		info = file.read()
		info_dict = {}
		user_lijst = []
		begin = 0
		while info.find("!*!", begin) != -1:
				eind = info.find("!*!", begin)
				rooster = info[begin:eind]
				begin = eind + 4
				regel_lijst, user = ontleed_rooster(rooster)
				user_lijst += [user]
				info_dict[user] = regel_lijst
		dagen = bereken_dagen(info_dict, user_lijst)
		stok_dict = vergelijk_uren(info_dict, user_lijst, dagen)
		#stok_rooster = stokbroodrooster(stok_dict, dagen, user_lijst)
		#maak_file(stok_rooster)
		return info_dict, user_lijst, dagen

def bereken_dagen(info_dict, user_lijst):
		dagen_info_lijst = []
		dagen_lijst = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
		for user in user_lijst:
				info = info_dict[user]
				user_info = info[0]
				begin = user_info.find(": ") + 2
				dagen_info = user_info[begin:]
				if dagen_info not in dagen_info_lijst and len(dagen_info_lijst) != 0:
						return "dagen niet gelijk"
				dagen_info_lijst += [dagen_info]
				spatie = dagen_info.find(" ")
				dag = dagen_info[:spatie]
				#print(dag)
		for i in range(len(dagen_lijst)):
				#print(dag, dagen_lijst[i], i)
				if dag == dagen_lijst[i]:
						dag_nummer = i
		#input("e")
		dagen_volgorde = []
		for i in range(dag_nummer, dag_nummer + 5):
				if i > 4:
						i = i - 5
				dagen_volgorde += [dagen_lijst[i]]
		dagen_volgorde += [dagen_volgorde[0]]
		#print(dag_nummer, dagen_volgorde)
		return dagen_volgorde

def vergelijk_uren(info_dict, user_lijst, dagen):
		if dagen == "dagen niet gelijk":
				return "u'r mom giey"
		verg_dict = {}
		dag_dict = {}
		for i in range(6):
				dag = dagen[i]
				if i == 5:
						dag = "next" + dag
				tu_dict = {}
				tu_totaal_lijst = []
				print("\n" + dag + "\n")
				for user in user_lijst:
						info = info_dict[user]
						tussenuren = info[i + 1]
						tu_list = split_tu(tussenuren)
						for tu in tu_list:
								try:
										tu_dict[tu] += ", " + user
								except:
										tu_dict[tu] = user
								if tu not in tu_totaal_lijst and tu != "":
									tu_totaal_lijst += [tu]
								print(user, tu, tu_dict, tu_totaal_lijst)
								input("vergelijk_uren")
				dag_dict[dag]

def split_tu(tu):
		tu_list = []
		komma = 0
		while komma != -1:
				komma = tu.find(", ")
				if komma == -1:
						tu_list += [tu]
				else:
						tu_list += [tu[0:komma]]
						tu = tu[komma+2:len(tu)]
				print(tu, tu_list)
				#input("komma")
		return tu_list

info_dict, user_lijst, dagen = main_loop()
print(info_dict, user_lijst, dagen)

input("Einde")
