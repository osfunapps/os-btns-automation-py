Introduction
------------

This script is designed to provide intuitive buttons automation kit.

NOTICE: it's heavily relied on pyautogui

## Installation
Install via pip:

    pip install os-btns-automation


## Usage       
Require btns_automation:
        
    from os_btns_automation import btns_automation
    
    btns_automation.paste()  # will paste any copied text
    btns_automation.copy()  # will copy the currently selected content
    btns_automation.select_all()  # will select all in the current context
    btns_automation.press('esc')  # will press a button
    btns_automation.hot_key(['ctrl', 'c'])  # will perform instrumental combo of buttons
    btns_automation.key_down('esc')  # will hold a key down
    btns_automation.key_up('esc')  # will release a key



And more...


## Links
[GitHub - osapps](https://github.com/osfunapps)

## Licence
ISC