import pyautogui as py
import time

f = open('./logs/cleaned_list.txt','r')

def addItemsToVendor():
    cleaned = open('./logs/cleaned_list.txt','r')
    print('items will be added in 10 seconds')
    for i in range(10, 0, -1):
        print(f'{i} seconds left...')
        time.sleep(1)
    print('Starting commands...')
    
    lines = cleaned.readlines()
    
    for line in lines:
        py.press('enter')
        x = ".npc additem {}".format(line)
        
        for i in x:
            py.press(i)

    cleaned.close()
 
def addItemsToChar():
    cleaned = open('./logs/cleaned_list.txt','r')
    print('items will be added in 10 seconds')
    for i in range(10, 0, -1):
        print(f'{i} seconds left...')
        time.sleep(1)
    print('Starting commands...')
    
    lines = cleaned.readlines()
    
    for line in lines:
        py.press('enter')
        x = ".additem {}".format(line)
        
        for i in x:
            py.press(i)
    cleaned.close()
    
