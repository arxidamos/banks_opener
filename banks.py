#! python3
# openBanks.py - Automatically open 4 financial management banks.

import winsound
import pyautogui, time
from selenium import webdriver

browser = webdriver.Chrome()

# Clicks we need to perform to get into each bank's credentials field.
piraeusClick = (325, 70)
alphaClick = (740, 538)
alphaClick2 = (500, 937)
euroClick = (350, 440)
euroClick2 = (62, 483)
ethnikiClick = (100, 365)

# Remember to update credentials, each time a password changes
i = {
'Piraeus': 'https://www.winbank.gr/sites/corporate/el/Pages/default.aspx', 'UsernameP': '123', 'PasswordP': '123',
'Alpha': 'https://www.alpha.gr/el/epixeiriseis/myalpha', 'UsernameA': '234', 'PasswordA': '234',
'Eurobank': 'https://ebanking.eurobank.gr/#/login', 'UsernameE': '345', 'PasswordE': '345',
'Ethniki': 'https://ibankretail.nbg.gr/sts/Account/Login/web', 'UsernameI': '456', 'PasswordI': '456'
}

pyautogui.PAUSE = 0.5

# Give user a chance to stop the script.
print('-----1 seconds delay to let user press Ctrl-C-----')
time.sleep(0)

#################################################################### ΠΕΙΡΑΙΩΣ ##########################
pyautogui.click(piraeusClick[0], piraeusClick[1])
pyautogui.typewrite(i['Piraeus'] + '\n')
	
# Wait till Piraeus has loaded...
time.sleep(8)

# In Piraeus, cursor moves to credentials so no need for us to move it

# Insert Piraeus credentials
pyautogui.typewrite(i['UsernameP'] + '\t')
pyautogui.typewrite(i['PasswordP'] + '\t' + '\n')

pyautogui.PAUSE = 0.5

# Ctrl-t to open new tab
pyautogui.hotkey('ctrl', 't')

#################################################################### Alpha ##########################
pyautogui.typewrite(i['Alpha'] + '\n')

# Wait till Alpha has loaded...
time.sleep(10)

# Move cursor to Alpha's credentials field
pyautogui.click(alphaClick[0], alphaClick[1])

# Insert Alpha credentials
pyautogui.typewrite(i['UsernameA'] + '\t')
pyautogui.typewrite(i['PasswordA'] + '\t' + '\n')

# Wait for Alpha to load, press Esc to avoid annoying message
pyautogui.PAUSE = 14
pyautogui.click(alphaClick2[0], alphaClick2[1])
pyautogui.click(alphaClick2[0], alphaClick2[1])

pyautogui.PAUSE = 1.0

# Ctrl-t to open new tab
pyautogui.hotkey('ctrl', 't')

#################################################################### Eurobank ##########################
pyautogui.typewrite(i['Eurobank'] + '\n')

# Wait till Eurobank has loaded...
time.sleep(13)

# Move cursor to Eurobank credentials' field
pyautogui.click(euroClick[0], euroClick[1])

# Insert Euro credentials
pyautogui.typewrite(i['UsernameE'] + '\t')
pyautogui.typewrite(i['PasswordE'] + '\t' + '\n')

# Wait for Eurobank to load, move to Balance page
pyautogui.PAUSE = 7
pyautogui.click(85, 429)
pyautogui.click(euroClick2[0], euroClick2[1], 2)

pyautogui.PAUSE = 0.5
pyautogui.hotkey('ctrl', 't')	# ctrl-t to open new tab

#################################################################### Ethniki ##########################
pyautogui.typewrite(i['Ethniki'] + '\n')

# Wait till Ethniki has loaded...
time.sleep(8)

# Move cursor to Ethniki credentials' field
pyautogui.click(ethnikiClick[0], ethnikiClick[1])

# Insert Ethniki credentials
pyautogui.typewrite(i['UsernameI'] + '\t')
pyautogui.typewrite(i['PasswordI'] + '\t' + '\n')

###### Ring to inform the Manager #####################################################################
winsound.PlaySound('magic.wav', winsound.SND_FILENAME)