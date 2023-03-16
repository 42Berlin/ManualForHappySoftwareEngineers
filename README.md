# ManualForHappySoftwareEngineers

This script will create Notion pages from ISBN numbers. 
Wikimedia Link: https://www.notion.so/42wolfsburgberlin/42-Library-98be64c67c5742ffac261d0342988109?pvs=4

Prerequisites:
1. Git is installed: https://github.com/git-guides/install-git
2. pip3 is installed: https://www.delftstack.com/howto/python/python-install-pip3-mac/
3. Repository cloned

How to get it running
1. Install necessary packages: `pip3 install -r requirements.txt`
2. Get the .env file to access the Notion API from 1Password and place it into the main folder of the app
3. Try out the edit.py to create a new wiki page for a book `python3 add_book_Notion.py 9781529038347`. The number is an ISBN of your choice.
4. Try out the barcode.py to scan a book and then execute edit.py to create a wiki page automatically: `python3 barcode.py`
