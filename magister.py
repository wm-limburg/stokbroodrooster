#Created by Bas het Beest
#©CPL Code Productions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

def s(t=1):
	time.sleep(t)

def wait_find_id(d,i, waittime=10):
	element = WebDriverWait(d, waittime).until(
		EC.presence_of_element_located((By.ID, i))
		)
	return element

def login(user, passw):
	chrome_options = Options() 
	chrome_options.add_argument("--headless") 
	d = webdriver.Chrome(chrome_options=chrome_options)
	s()
	d.get("https://ghc.magister.net")
	username = wait_find_id(d, "username")
	username.send_keys(user + "\n")
	password = wait_find_id(d, "password")
	password.send_keys(passw + "\n")
	return d

def make_soup(d):
	agenda = wait_find_id(d, "menuKnopAgenda", 15)
	agenda.click()
	s(3)
	soup = BeautifulSoup(d.page_source, "html.parser")
	return d, soup

def soup_analyse(d, soup):
	TPOSE = soup.find_all("tbody")[0]
	TROWs = TPOSE.find_all("tr")
	infodict = {}
	urenlijst = []
	dagenlijst = []
	dag = None
	for r in TROWs:
		TCOLs = r.find_all("td")
		if len(TCOLs) == 1:
			infodict[dag] = urenlijst
			dag = extract_dag(TCOLs[0])
			dagenlijst += [dag]
			urenlijst = []
		else:
			pass
			uur = extract_uur(TCOLs)
			if uur != "niet valide":
				urenlijst += [uur]
	infodict[dag] = urenlijst
	return infodict, dagenlijst

def extract_dag(info):
	strong = info.find("strong")
	dag = strong.string
	return dag

def extract_uur(cols):
	lescol = cols[2]
	spans = lescol.find_all("span")
	if len(spans) == 4:
		uurspan = spans[1]
		uur = uurspan.string
		return uur
	else:
		return "niet valide"

def make_file(inf, dagen, username):
	inf = remove_streepjes(inf, dagen)
	inv_rooster = invert_rooster(inf, dagen)
	newrooster = make_new_rooster(inv_rooster, dagen, username)
	try:
		file = open("mstokbroodrooster.txt", "r")
		rooster = file.read()
		userplace = rooster.find(username)
		if userplace != -1:
			vervang_oud_rooster(rooster, newrooster, userplace)
		else:
			add_rooster(newrooster)
	finally:
		file.close()

def make_new_rooster(inf, dagen, username):
	newrooster = ""
	newrooster += username + ": " + dagen[0] + "t/m " + dagen[-1] + "\n"
	for dag in dagen:
		uren = inf[dag]
		newrooster += str(uren) + "\n"
	newrooster += "!*!\n"
	return newrooster

def vervang_oud_rooster(rooster, newrooster, userplace):
	userend = rooster.find("!*!", userplace)
	ouduserrooster = rooster[userplace:userend]
	restvoor = rooster[:userplace]
	restna = rooster[userend + 4:]
	wfile = open("mstokbroodrooster.txt", "w")
	wfile.write(restvoor + newrooster + restna)
	wfile.close()

def add_rooster(newrooster):
	afile = open("mstokbroodrooster.txt", "a")
	afile.write(newrooster)
	afile.close()

def invert_rooster(rooster, dagen):
	invrooster = {}
	for dag in dagen:
		tussenuren = []
		uren = rooster[dag]
		eerste_uur = int(uren[0])
		laatste_uur = int(uren[-1])
		for i in range(eerste_uur, laatste_uur):
			if str(i) not in uren:
				tussenuren += [i]
		invrooster[dag] = tussenuren
	return invrooster

def remove_streepjes(inf, dagen):
	for dag in dagen:
		uren = inf[dag]
		new_uren = []
		for uur in uren:
			streepje = uur.find("-")
			if streepje != -1:
				new_uren += uur[:streepje]
				new_uren += uur[streepje +1:]
			else:
				new_uren += uur
		inf[dag] = new_uren
	return inf

def enter_info():
	username = input("username: ")
	password = input("password: ")
	os.system("cls")
	return username, password

def logout(d):
	logout_button = d.find_element_by_id("uitloggen")
	logout_button.click()

file = open("ww.txt", "r")
infos = file.read().split("\n")
infos = [info.split(",") for info in infos][:-1]

for [username,password] in infos:
	#username, password = enter_info()
	d = login(username, password)
	d, soup = make_soup(d)
	logout(d)
	infodict, dagenlijst = soup_analyse(d, soup)
	print(infodict, dagenlijst)
	make_file(infodict, dagenlijst, username)

	d.quit()
	
#ik heb iets gedaan

