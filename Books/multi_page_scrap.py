import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from logger_config import setup_logger
from summary import generate_data_summary

logger = setup_logger()

def scrape_books_multiple_pages(pages=3):
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    all_books = []
    logger.info("Scraping started.")

    for page in range(1, pages + 1):
        try:
            logger.info(f"Scraping page {page}...")
            response = requests.get(base_url.format(page))
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.find_all('article', class_='product_pod')

            for book in books:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text.strip()
                availability = book.find('p', class_='instock availability').text.strip()
                star = book.find('p', class_='star-rating')
                rating = star['class'][1] if star else 'Not rated'

                all_books.append({
                    'Title': title,
                    'Price': price,
                    'Availability': availability,
                    'Star Rating': rating
                })
            time.sleep(1)

        except Exception as e:
            logger.error(f"Error on page {page}: {e}")

    try:
        df = pd.DataFrame(all_books)
        df.to_csv('books_multipage.csv', index=False)
        logger.info("Data saved to books_multipage.csv")
        return df
    except Exception as e:
        logger.error(f"Error saving CSV: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df_books = scrape_books_multiple_pages(3)
    if not df_books.empty:
        generate_data_summary(df_books)
