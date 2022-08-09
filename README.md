# ManualForHappySoftwareEngineers

This script will create Wikimedia pages from ISBN numbers. 
Wikimedia Link: https://library.42wolfsburg.de/index.php/Manual_For_Happy_Software_Engineers

Prerequisites:
1. Git is installed: https://github.com/git-guides/install-git
2. pip3 is installed: https://www.delftstack.com/howto/python/python-install-pip3-mac/
3. Repository cloned

How to get it running
1. Install necessary packages: `pip3 install -r requirements.txt`
2. Get the credentials.json file to access the Mediawiki from 42 Wolfsburg and place it into the main folder of the app
3. Try out the edit.py to create a new wiki page for a book `python3 edit.py 9781529038347`. The number is an ISBN of your choice.
4. Try out the barcode.py to scan a book and then execute edit.py to create a wiki page automatically: `python3 barcode.py`
