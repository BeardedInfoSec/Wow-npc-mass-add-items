import pyautogui as py
import time
import os
import json
import datetime
import supporting_scripts.get_urls as get_urls
import supporting_scripts.add_items_to_char as add_items

date = datetime.datetime.now()
date = date.strftime("%Y-%m-%d %H_%M")
date = str(date).replace(':', '_')
x = './logs/cleaned_list.txt'
s = './logs/spell_list_{}.json'
itemList = []
spellList = []
spell_de_duped = []
spellsToAdd = {
	"table": "item_template",
	"rows":
	[
	]
    }   
    
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
        print(f'{i}')
        if i.rfind("spell=") != -1:
            print(f'inside spell {i}')
            extractSpell(i)
        elif i.rfind("item=") != -1:
            print(f'inside item {i}')
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
       
def SpellToJson():
    
    newRow = {
	"rows":
	[
		{
			"entry": 35458,
			"class": 0,
			"subclass": 8,
			"unk0": -1,
			"name": "Enchant Weapon - Mongoose",
			"displayid": 48859,
			"Quality": 1,
			"Flags": 64,
			"BuyCount": 1,
			"BuyPrice": 0,
			"SellPrice": 650,
			"InventoryType": 0,
			"AllowableClass": -1,
			"AllowableRace": -1,
			"ItemLevel": 70,
			"RequiredLevel": 0,
			"RequiredSkill": 0,
			"RequiredSkillRank": 0,
			"requiredspell": 0,
			"requiredhonorrank": 0,
			"RequiredCityRank": 0,
			"RequiredReputationFaction": 0,
			"RequiredReputationRank": 0,
			"maxcount": 0,
			"stackable": 1,
			"ContainerSlots": 0,
			"stat_type1": 0,
			"stat_value1": 0,
			"stat_type2": 0,
			"stat_value2": 0,
			"stat_type3": 0,
			"stat_value3": 0,
			"stat_type4": 0,
			"stat_value4": 0,
			"stat_type5": 0,
			"stat_value5": 0,
			"stat_type6": 0,
			"stat_value6": 0,
			"stat_type7": 0,
			"stat_value7": 0,
			"stat_type8": 0,
			"stat_value8": 0,
			"stat_type9": 0,
			"stat_value9": 0,
			"stat_type10": 0,
			"stat_value10": 0,
			"dmg_min1": 0,
			"dmg_max1": 0,
			"dmg_type1": 0,
			"dmg_min2": 0,
			"dmg_max2": 0,
			"dmg_type2": 0,
			"dmg_min3": 0,
			"dmg_max3": 0,
			"dmg_type3": 0,
			"dmg_min4": 0,
			"dmg_max4": 0,
			"dmg_type4": 0,
			"dmg_min5": 0,
			"dmg_max5": 0,
			"dmg_type5": 0,
			"armor": 0,
			"holy_res": 0,
			"fire_res": 0,
			"nature_res": 0,
			"frost_res": 0,
			"shadow_res": 0,
			"arcane_res": 0,
			"delay": 0,
			"ammo_type": 0,
			"RangedModRange": 0,
			"spellid_1": 46536,
			"spelltrigger_1": 0,
			"spellcharges_1": -1,
			"spellppmRate_1": 0,
			"spellcooldown_1": 1000,
			"spellcategory_1": 0,
			"spellcategorycooldown_1": -1,
			"spellid_2": 0,
			"spelltrigger_2": 0,
			"spellcharges_2": 0,
			"spellppmRate_2": 0,
			"spellcooldown_2": -1,
			"spellcategory_2": 0,
			"spellcategorycooldown_2": -1,
			"spellid_3": 0,
			"spelltrigger_3": 0,
			"spellcharges_3": 0,
			"spellppmRate_3": 0,
			"spellcooldown_3": -1,
			"spellcategory_3": 0,
			"spellcategorycooldown_3": -1,
			"spellid_4": 0,
			"spelltrigger_4": 0,
			"spellcharges_4": 0,
			"spellppmRate_4": 0,
			"spellcooldown_4": -1,
			"spellcategory_4": 0,
			"spellcategorycooldown_4": -1,
			"spellid_5": 0,
			"spelltrigger_5": 0,
			"spellcharges_5": 0,
			"spellppmRate_5": 0,
			"spellcooldown_5": -1,
			"spellcategory_5": 0,
			"spellcategorycooldown_5": -1,
			"bonding": 0,
			"description": "",
			"PageText": 0,
			"LanguageID": 0,
			"PageMaterial": 0,
			"startquest": 0,
			"lockid": 0,
			"Material": 8,
			"sheath": 0,
			"RandomProperty": 0,
			"RandomSuffix": 0,
			"block": 0,
			"itemset": 0,
			"MaxDurability": 0,
			"area": 0,
			"Map": 0,
			"BagFamily": 0,
			"TotemCategory": 0,
			"socketColor_1": 0,
			"socketContent_1": 0,
			"socketColor_2": 0,
			"socketContent_2": 0,
			"socketColor_3": 0,
			"socketContent_3": 0,
			"socketBonus": 0,
			"GemProperties": 0,
			"RequiredDisenchantSkill": -1,
			"ArmorDamageModifier": 0,
			"ScriptName": "",
			"DisenchantID": 0,
			"FoodType": 0,
			"minMoneyLoot": 0,
			"maxMoneyLoot": 0,
			"Duration": 0,
			"ExtraFlags": 0
		    }
	    ]
    }
    
    x = int(input('Enter the entry you want to start at:\n'))
    for i in spell_de_duped:
        x = x + 1
        newRow['rows'][0]['entry'] = x
        newRow['rows'][0]['name'] = i[1]
        newRow['rows'][0]['spellid_1'] = i[0]
        spellsToAdd['rows'].append(newRow["rows"])
        with open('./logs/spell_list_{}.json'.format(date), 'a') as s_file:
            s_file.write(json.dumps(newRow,indent=2))
            s_file.write(',')
            s_file.close()
    
def GearSelection():
    gear = int(input('Who do you want to add the items to?:\n1. Vendor\n2. Character\n3. Exit!\n'))
    if gear == 1:
        print('Open World of Warcraft and target the VENDOR you wish to add the items to.')
        add_items.addItemsToVendor()
    elif gear == 2:
        print('Open World of Warcraft and target the CHARACTER you wish to add the items to')
        add_items.addItemsToChar()


get_urls.run()
cleanUrls()
cleaned.close()
GearSelection()
quit()