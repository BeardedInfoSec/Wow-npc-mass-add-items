import pyautogui as py
import time
import os
import datetime
import supporting_scripts.get_urls as get_urls
import supporting_scripts.add_items_to_char as add_items
import mysql.connector
import getpass4

date = datetime.datetime.now()
date = date.strftime("%Y-%m-%d %H_%M")
date = str(date).replace(':', '_')
x = './logs/cleaned_list.txt'
s = './logs/spell_list_{}.json'
itemList = []
spellList = []
spell_de_duped = []
    
if os.path.exists(s):
    os.remove(s)


if not os.path.exists('/logs/spell_list.json'):
    s = open('./logs/spell_list.json','w')
s = open('./logs/spell_list.json','r')

if not os.path.exists('./logs/cleaned_list.txt'):
    cleaned = open("./logs/cleaned_list.txt",'w')
cleaned = open('./logs/cleaned_list.txt','a')

def extractItem(i):
    x = i.replace('https://www.wowhead.com/classic/item=', '')
    x = x.replace('https://www.wowhead.com/tbc/item=', '')
    x = x.replace('https://www.wowhead.com/wotlk/item=', '')
    x = x.strip('\n')
    v = x.split('/')
    itemList.append(v[0])
    
def extractSpell(i):
    x = i.replace('https://www.wowhead.com/classic/spell=', '')
    x = x.replace('https://www.wowhead.com/tbc/spell=', '')
    x = x.replace('https://www.wowhead.com/wotlk/spell=', '')
    x = x.replace('-',' ')
    x = x.strip('\n')
    v = x.split('/')
    spellList.append(v)
    
def cleanUrls():
    f = open('./logs/item_list.txt', 'r')
    for i in f:
        if i.rfind("spell=") != -1:
            extractSpell(i)
        elif i.rfind("item=") != -1:
            extractItem(i)
    removeDups(itemList,spellList)
   
def removeDups(itemList,spellList):
    v = list(set(itemList))
    s = spellList
    for i in v:
        cleaned.write(i + '\n')
        
    for i in s:
        if i not in spell_de_duped:
            spell_de_duped.append(i)   
       
def SpellToDB(): 

	_username = input("Enter DB username: ")
	_password = getpass4('Password: ')

	try:
		mydb = mysql.connector.connect(
			host="192.168.50.6",
			user=_username,
			password=_password,
			database="tbcmangos",
			port="3310"
			)
		mycursor = mydb.cursor()
		print("Connected...")
		x = int(input('Enter the entry you want to start at:\n'))
		sql = "INSERT INTO item_template (entry,subclass,name,displayid,Flags,BuyPrice,SellPrice,AllowableClass,Allo	wableRace,ItemLevel,delay,spellid_1,spellcooldown_1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	
		for i in spell_de_duped:
			x = x + 1
			name = i[1]
			spellId = i[0]
			val = (x,"8", name, "48859","64","5","5","-1","-1","70","0",spellId,"1000")
			mycursor.execute(sql, val)	
			mydb.commit()
			print(f'Added Entry: {x} Name: {name} SpellId: {spellId}')

	except mysql.connector.Error as err:print("Unable to connect: {}".format(err))

def GearSelection():
    gear = int(input('Who do you want to add the items to?:\n1. Vendor\n2. Character\n3. Back\n'))
    if gear == 1:
        print('Open World of Warcraft and target the VENDOR you wish to add the items to.')
        add_items.addItemsToVendor()
    elif gear == 2:
        print('Open World of Warcraft and target the CHARACTER you wish to add the items to')
        add_items.addItemsToChar()

_run = True
while _run:
    choice = int(input('Enter selection\n1. Copy Wowhead URLs\n2. Add items to char/vendor\n3. Add spells to DB\n4. exit\n'))
    if choice == 1:
        get_urls.run()
        cleanUrls()
        cleaned.close()
    elif choice == 2:
        GearSelection()
    elif choice == 3:
        SpellToDB()
    elif choice == 4:
        exit()
    else:
        print('Please enter a valid selection\n')
    