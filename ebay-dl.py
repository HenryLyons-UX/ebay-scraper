import argparse
import requests
from bs4 import BeautifulSoup
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument('--search', required=True)
parser.add_argument('--pages-dir', required=False)
args = parser.parse_args()
output = []
url = 'https://www.ebay.com/sch/i.html?_nkw=' + args.search + "&_pgn=1"
response = ""
headers = {'User-Agent': 'Mozilla/5.0'}
for i in range(1, 11):
    if args.pages_dir: 
        with open(args.pages_dir + "/page-" + str(i) + '.html', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), "html.parser")
    else:
        response = requests.get(url, headers = headers, timeout=10)
        response.raise_for_status()
        url = 'https://www.ebay.com/sch/i.html?_nkw=' + args.search + "&_pgn=" + str(i+1)
        soup = BeautifulSoup(response.text, "html.parser")
        time.sleep(1)
    for listing in soup.select('.s-item'):
        item = {}
        if listing.select_one(".s-item__title") == None:
            item['name'] = None
        else:
            item['name'] = listing.select_one(".s-item__title").text.strip()
        if listing.select_one(".s-item__price") == None:
            item['price'] = None
        else:
            item['price'] = int(listing.select_one(".s-item__price").text.strip().replace('$', "").replace(".","").replace(",","").split()[0])
        if listing.select_one(".SECONDARY_INFO") == None:
            item['status'] = None
        else:
            item['status'] = listing.select_one(".SECONDARY_INFO").text.strip()
        if listing.select_one(".s-item__shipping") == None:
            item['shipping'] = None
        
        else:
            if listing.select_one(".s-item__shipping").text.strip() == "Free shipping":
                item['shipping'] = 0
            else:
                item['shipping'] = int(listing.select_one(".s-item__shipping").text.strip().replace("$","").replace(".","").replace(",","").split()[0])
        if listing.select_one(".s-item__free-returns") == None:
            item['free_returns'] = None
        else:
            if listing.select_one(".s-item__free-returns").text.strip() == "Buyer pays return shipping":
                item['free_returns'] = False
            else:
                item['free_returns'] = True
        if listing.select_one(".s-item__hotness") == None:
            item['items_sold'] = None
        else:
            item['items_sold'] = int(listing.select_one(".s-item__hotness").text.strip().replace(",","").split()[0])
        output.append(item)

with open(args.search + '.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)
    print('Saved products.json')