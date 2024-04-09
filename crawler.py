import os
from dotenv import load_dotenv
from pyzotero import zotero

load_dotenv()
API_KEY = os.environ['API_KEY']
LIB_ID = os.environ['LIB_ID']
zot = zotero.Zotero(LIB_ID, 'user', API_KEY)

items = zot.top(limit=5)
for item in items:
    print('Item Type: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
