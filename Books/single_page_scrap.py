import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books_first_page():
    url = 'http://books.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    

    #  inspecting tells us that products are stored in article with a class named "product_pod"
    books = soup.find_all('article', class_='product_pod')


    # total books on a page are in books now
    
    book_data = []



    for book in books:
        # Title 
        title = book.h3.a['title']

        # Price
        price = book.find('p', class_='price_color').text.strip()

        # Availability
        availability = book.find('p', class_='instock availability').text.strip()

        # Star rating 
        star_tag = book.find('p', class_='star-rating')
        
        # print(star_tag['class'])
        
        # star_tag['class'] = ['star-rating', 'Three']

        star_rating = star_tag['class'][1] if star_tag else 'Not rated'

        book_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Star Rating': star_rating
        })

    # Create DataFrame and save to CSV
    df = pd.DataFrame(book_data)
    df.to_csv('books_basic.csv', index=False)
    print("Saved books_basic.csv with", len(df), "entries.")

# Run the function
scrape_books_first_page()
