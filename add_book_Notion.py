#!/usr/bin/python3

"""
    edit.py

    MediaWiki API Demos
    Demo of `Edit` module: POST request to edit a page
    MIT license
"""

import requests
import re
import sys
import json
import getpass
import os
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

def create_entry(isbn):
    # Set up Notion API endpoint and database ID
    database_id = os.environ['NOTION_LIBRARY_ID']
    notion_api_endpoint = "https://api.notion.com/v1/pages"


    # Set up the request headers
    headers = {
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}"
    }
 #Get data from google API
    S2 = requests.Session()
    R2 = S2.get(url='https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn)
    DATA2= R2.json()
    bookinfo = DATA2['items'][0]['volumeInfo']
    print(bookinfo)
    title = bookinfo['title']
    titleURL = re.sub(r'[^a-zA-Z,^" "]', '', title)
    if 'subtitle' in bookinfo:
        subtitle = bookinfo['subtitle']
    else:
        subtitle = ""
    if 'authors' in bookinfo:
        authors = str(bookinfo['authors']).strip("[]").replace("\'","")
    else:
        authors = ""
    if 'publisher' in bookinfo:
        publisher = bookinfo['publisher']
    else:
        publisher = ""
    if 'publishedDate' in bookinfo:
        published_date = bookinfo['publishedDate']
    else:
        published_date = ""
    if 'imageLinks' in bookinfo:
        image = bookinfo['imageLinks']['thumbnail']
    else:
        image = ""
    for identifier in bookinfo['industryIdentifiers']:
        if identifier['type'] == "ISBN_13":
            isbn = identifier['identifier']
    if 'description' in bookinfo:
        description = str(bookinfo['description']).split(' ________________________________________ ')
        if len(description) > 1:
            description = description[1]
        else:
            if len(description[0]) > 1999:
                description = description[0][:1996] + '...'
            else:
                description = description[0]
    else:
        description = ""
    # Define the properties for the new page
    new_page_properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": title
                    }
                }
            ],
        },
        "Author": {
            "rich_text": [
                {
                    "text": {
                        "content": authors
                    }
                }
            ]
        },
        "ISBN": {
            "rich_text": [
                {
                    "text": {
                        "content": isbn
                    }
                }
            ]
        },
        "Publisher": {
            "rich_text": [
                {
                    "text": {
                        "content": publisher
                    }
                }
            ]
        },
        "Subtitle": {
            "rich_text": [
                {
                    "text": {
                        "content": subtitle
                    }
                }
            ]
        },
        "Summary": {
            "rich_text": [
                {
                    "text": {
                        "content": description
                    }
                }
            ]
        },
        "Published": {
            "rich_text": [
                {
                    "text": {
                        "content": published_date
                    }
                }
            ]
        }
    }
    book_cover = {
        "type": "external",
        "external": {
            "url": image
        }
    }

    # Define the new page
    if 'imageLinks' in bookinfo:
        new_page = {
            "parent": {
                "database_id": database_id
            },
            "properties": new_page_properties,
            "cover": book_cover
        }
    else:
        new_page = {
            "parent": {
                "database_id": database_id
            },
            "properties": new_page_properties,
        }

    # Send the request to create the new page
    response = requests.post(notion_api_endpoint, headers=headers, json=new_page)

    # Print the response
    pprint(response.json())
# def create_entry(isbn):
#     with open('credentials.json', 'r') as f:
#             credentials = json.load(f)

#     S = requests.Session()

#     URL = "https://library.42wolfsburg.de/api.php"

# # Step 1: GET request to fetch login token
#     PARAMS_0 = {
#         "action": "query",
#         "meta": "tokens",
#         "type": "login",
#         "format": "json"
#     }

#     R = S.get(url=URL, params=PARAMS_0)
#     DATA = R.json()

#     LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# # Step 2: POST request to log in. Use of main account for login is not
# # supported. Obtain credentials via Special:BotPasswords
# # (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
# #pw = getpass.getpass()
#     PARAMS_1 = {
#         "action": "login",
#         "lgname": credentials["user"],
#         "lgpassword": credentials["pw"],
#         "lgtoken": LOGIN_TOKEN,
#         "format": "json"
#     }

#     R = S.post(URL, data=PARAMS_1)

# # Step 3: GET request to fetch CSRF token
#     PARAMS_2 = {
#         "action": "query",
#         "meta": "tokens",
#         "format": "json"
#     }

#     R = S.get(url=URL, params=PARAMS_2)
#     DATA = R.json()

#     CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# #Get data from google API
#     S2 = requests.Session()
#     R2 = S2.get(url='https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn)
#     DATA2= R2.json()
#     bookinfo = DATA2['items'][0]['volumeInfo']
#     print(bookinfo)
#     title = bookinfo['title']
#     titleURL = re.sub(r'[^a-zA-Z,^" "]', '', title)
#     if 'subtitle' in bookinfo:
#         subtitle = bookinfo['subtitle']
#     else:
#         subtitle = ""
#     authors = str(bookinfo['authors']).strip("[]").replace("\'","")
#     if 'publisher' in bookinfo:
#         publisher = bookinfo['publisher']
#     else:
#         publisher = ""
#     if 'published_date' in bookinfo:
#         published_date = bookinfo['publishedDate']
#     else:
#         published_date = ""
#     if 'imageLinks' in bookinfo:
#         image = bookinfo['imageLinks']['thumbnail'] + ".jpeg"
#     else:
#         image = ""
#     for identifier in bookinfo['industryIdentifiers']:
#         if identifier['type'] == "ISBN":
#             isbn = identifier['identifier']
#     if 'description' in bookinfo:
#         description = bookinfo['description']
#     else:
#         description = ""
#     appendtext = "{{{{Book|title={}|subtitle={}|authors={}|published_date={}|image={}|publisher={}|isbn={}|description={}}}}}".format(title,subtitle,authors,published_date,image,publisher,isbn,description)

# # Step 4: POST request to edit a page
#     PARAMS_3 = {
#         "action": "edit",
#         "title": titleURL,
#         "token": CSRF_TOKEN,
#         "format": "json",
#         "appendtext": appendtext
#     }

#     R = S.post(URL, data=PARAMS_3)
# # Step 5: Create link
#     PARAMS_4 = {
#         "action": "edit",
#         "title": "Manual For Happy Software Engineers",
#         "token": CSRF_TOKEN,
#         "format": "json",
#         "appendtext": "\n*[[{}]]".format(titleURL)
#     }

#     R = S.post(URL, data=PARAMS_4)
#     DATA = R.json()

#     print(DATA)

if __name__ == '__main__':
    isbn = sys.argv[1]
    create_entry(isbn)
