"""
Webscrapping script to scrape the list of all books having Two star ratings
from website "https://books.toscrape.com"

"""

import requests
import bs4

res = requests.get('https://books.toscrape.com/catalogue/page-1.html')

soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('.star-rating.Two')
# This shows all the books on page 1 with rating 2. 

main_class = soup.select('.product_pod')

len(main_class) # this shows number of books on each page.

main_class[0].select('.star-rating.Two') #returns list with len>1 if the book is having Two stars

# for title:
title_loc = main_class[0].select('a')[1]['title']

# lets set base URL for site.
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

def two_star_book_list():

	# Website has 50 total pages to check.

    book_list = [] 	# To append book titles.

    for i in range(1,51):
        page_url = base_url.format(i)
        page_url = requests.get(page_url)
        soup = bs4.BeautifulSoup(page_url.text,'lxml')
        books = soup.select('.product_pod') # This will load all books on current page in books.
        
        for  book in books:
    
    		# As we observed books not having two star rating will return empty list.
    
            if len(book.select('.star-rating.Two')) != 0:
                book_title = book.select('a')[1]['title']
                book_list.append(book_title)
    
    return book_list

print(two_star_book_list())
