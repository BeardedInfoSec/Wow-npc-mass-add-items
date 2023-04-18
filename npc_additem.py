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
gmcommand = input("\nenter the gm command (.additem)\n")
review = input('The command you entered was:\n {}\n was this correct?:\n1. Yes\n2. No(retype command)\n')
while int(review) != 1:
    review = input('Please re-enter your gm command:\n')
gmcommand = review
for i in f:
    x = i.strip('https://www.wowhead.com/classic/item=')
    x = i.strip('https://www.wowhead.com/tbc/item=')
    x = i.strip('https://www.wowhead.com/wotlk/item=')
    x = x.strip('\n')
    v = x.split('/')
    itemList.append(v[0])
for c in itemList:
    if c not in de_duped:
        cleaned.write("{} {} 0 0 0 \n".format(gmcommand,c))
        de_duped.append(c) 
cleaned.close()    
start = input('Are you targeting npc?\n1. Yes\n2. No\n')
while int(start) != 1:
    print("\nplease target the NPC then press 1 to continue: ")
print('\nCommands will run to add items in 10 seconds...')
time.sleep(10)
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

