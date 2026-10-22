1. Explanation of ebay-dl.py
This file starts by intaking a search time from the command line. It adds this search term into an ebay URL. It also checks if the command states to use the practice pages or the live ebay URL. If the command does not specifiy to use the practice pages, it will run a for loop 10 times. This loop takes the ebay url and gathers all of the html of that page using BeautifulSoup. It then go though the saved html for that page, and creates a dicitonory of infomration for each item listed on the ebay page. The dicitionary includes certain the names of certain characteristics as keys, and has the returns the apporatite value for each listed item. For exmaple it will include, the item name, its price, and other certain characteristics. If the characteristic is missing from the listing it will just inlcude the value None. It appends the dictionary for each item to list that has every listing within the first 10 pages of the ebay results. If the command line specifies to use the pracitce pages the code will create the same dicitonaries but just use the information listed in the practice pages instead. Lastly the code will return output or list in a JSON file with the search term in the name of the file.

2. Instrucitons for running ebay-dl.py
## Usage
    to run code:
    python ebay-dl.py --search (search term)
    to run code with practice files:
    python ebay-dl.py --search (search term) --pages-dir practice-pages
    to run code with CSV:
    python ebay-dl.py --search (search term) --pages-dir practice-pages --csv
    example with CSV:
    python ebay-dl.py --search "stuffed animal" --pages-dir practice-pages --csv
3. Project page
link: https://csci40.rtealwitter.com/projects/02_webscraping/project.html