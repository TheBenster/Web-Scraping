from bs4 import BeautifulSoup
import requests
import re
import csv


# Horror
horror_url = 'https://www.goodreads.com/list/show/135.Best_Horror_Novels'
result = requests.get(horror_url).text
horror_doc = BeautifulSoup(result, 'html.parser')

book_elements = horror_doc.find_all('tr', {'itemtype' : 'http://schema.org/Book'})

with open('horror_books.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Author', 'Rating', 'Genre'])
    
    for book in book_elements:
        title_uncleaned = book.find('a', {'class' :'bookTitle'})
        title = title_uncleaned.text.strip()
        author_uncleaned = book.find('a', {'class' : 'authorName'})
        author = author_uncleaned.text.strip()
        rating_uncleaned = book.find('span', {'class' : 'minirating'})
        rating = rating_uncleaned.text.strip()
    
        genre = 'Horror'
        
        writer.writerow([title, author, rating, genre])
            
            
# Philosophy
philosophy_url = 'https://www.goodreads.com/list/show/451.Best_World_Philosophy_Book'
philo_result = requests.get(philosophy_url).text
philo_doc = BeautifulSoup(philo_result, 'html.parser')

# Gathers each book labelled in the list according to the site, the table row uses the identifier of schema
book_elements = philo_doc.find_all('tr', {'itemtype' : 'http://schema.org/Book'})
    
# Writes a new CSV file with the identifiable columns Title, Author, Rating, and Genre
with open('philosophy_books.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
        
    writer.writerow(['Title', 'Author', 'Rating', 'Genre'])
        
    # Iterates through the list of books to grab the title, author, etc
    for book in book_elements:
        title_uncleaned = book.find('a', {'class' : 'bookTitle'})
        author_uncleaned = book.find('a', {'class' : 'authorName'} )
        rating_uncleaned = book.find('span', {'class' : 'minirating'})
        
        # Takes apart the html hoo hah to clean it up for the csv
        title = title_uncleaned.text.strip()
        author = author_uncleaned.text.strip()
        rating = rating_uncleaned.text.strip()
        genre = 'Philosophy'
            
        
        writer.writerow([title, author, rating, genre])
            