import pyautogui as py
import time
import os

itemList = []
de_duped = []
f = 'item_list.txt'
if not os.path.exists(f):
    f = open('item_list.txt','w')
cleaned = open('cleaned_list.txt','a')

g = int(input('Add Wowhead urls to "item_list.txt"\n1. Done\n2. Not yet\n'))
while g != 1:
    g = int(input('\nAre you finished adding items to "item_list.txt"?\n1. Yes\n2. No'))

for i in f:
    x = i.strip('https://www.wowhead.com/classic/item=')
    x = i.strip('https://www.wowhead.com/tbc/item=')
    x = i.strip('https://www.wowhead.com/wotlk/item=')
    x = x.strip('\n')
    v = x.split('/')
    itemList.append(v[0])

s = False
while not s:
    c = input('\n1. Add Item(s)\n2. Delete Item(s)\n')
    if int(c) == 1:
        for c in itemList:
            if c not in de_duped:
                cleaned.write(".npc additem {} 0 0 0 \n".format(c))
                de_duped.append(c)
        break
    
    if int(c) == 2:
        for c in itemList:
            if c not in de_duped:
                cleaned.write(".npc delitem {} 0 0 0 \n".format(c))
                de_duped.append(c)
        break
    
cleaned.close()    

print('\nSwitch to your World of Warcraft client and target the NPC\nCommands will run in 10 seconds...')

for i in range(10, 0, -1):
    print(f'{i} seconds left...')
    time.sleep(1)

print('Starting commands...')

cleaned = open('cleaned_list.txt', 'r')

lines = cleaned.readlines()
for line in lines:
    py.press('enter')
    print(line)
    for char in line.strip():
        py.press(char)
    py.press('enter')

cleaned.close()
os.remove("cleaned_list.txt")

