import time
import pyautogui
import pyperclip
import os

def run():
    if os.path.exists('./logs/item_list.txt'):
        os.remove('./logs/item_list.txt')
    # activate the Chrome window
    tabs = input('How many chrome tabs are open?: ')
    print('\nOpen Google Chrome')
    for i in range(10, 0, -1):
        print(f'Copying will start in {i} seconds...')
        time.sleep(1)

    # switch to the first tab
    pyautogui.hotkey('ctrl', '1')
    time.sleep(1)

    # activate the address bar and copy the URL
    pyautogui.hotkey('alt', 'd')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # store the URL in a list
    urls = [pyperclip.paste()]
    print('1 of {}, Copied {}'.format(tabs,pyperclip.paste()))

    # iterate through the rest of the tabs and repeat the process
    for i in range(1, int(tabs)):
        # switch to the next tab
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(1)
        # activate the address bar and copy the URL
        pyautogui.hotkey('alt', 'd')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        print('{} of {}, Copied {}'.format(i+1,tabs,pyperclip.paste()))

        # store the URL in a list
        urls.append(pyperclip.paste())


    # write the list of URLs to a file
    with open('./logs/item_list.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')
        f.close()

    # print a confirmation message
    print('Finished Grabbing Urls...')
