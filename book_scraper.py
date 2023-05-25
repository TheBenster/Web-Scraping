from bs4 import BeautifulSoup
import requests
import re
import csv


# Horror
# horror_url = 'https://www.goodreads.com/list/show/135.Best_Horror_Novels'
# result = requests.get(horror_url).text
# horror_doc = BeautifulSoup(result, 'html.parser')

# book_elements = horror_doc.find_all('tr', {'itemtype' : 'http://schema.org/Book'})

# with open('horror_books.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Title', 'Author', 'Rating', 'Genre'])
    
#     for book in book_elements:
#         title_uncleaned = book.find('a', {'class' :'bookTitle'})
#         title = title_uncleaned.text.strip()
#         author_uncleaned = book.find('a', {'class' : 'authorName'})
#         author = author_uncleaned.text.strip()
#         rating_uncleaned = book.find('span', {'class' : 'minirating'})
#         rating = rating_uncleaned.text.strip()
    
#         genre = 'Horror'
        
#         writer.writerow([title, author, rating, genre])
            
            
# Philosophy
# philosophy_url = 'https://www.goodreads.com/list/show/451.Best_World_Philosophy_Book'
# philo_result = requests.get(philosophy_url).text
# philo_doc = BeautifulSoup(philo_result, 'html.parser')

# # Gathers each book labelled in the list according to the site, the table row uses the identifier of schema
# book_elements = philo_doc.find_all('tr', {'itemtype' : 'http://schema.org/Book'})
    
# # Writes a new CSV file with the identifiable columns Title, Author, Rating, and Genre
# with open('philosophy_books.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
        
#     writer.writerow(['Title', 'Author', 'Rating', 'Genre'])
        
#     # Iterates through the list of books to grab the title, author, etc
#     for book in book_elements:
#         title_uncleaned = book.find('a', {'class' : 'bookTitle'})
#         author_uncleaned = book.find('a', {'class' : 'authorName'} )
#         rating_uncleaned = book.find('span', {'class' : 'minirating'})
        
#         # Takes apart the html hoo hah to clean it up for the csv
#         title = title_uncleaned.text.strip()
#         author = author_uncleaned.text.strip()
#         rating = rating_uncleaned.text.strip()
#         genre = 'Philosophy'
            
        
#         writer.writerow([title, author, rating, genre])
            
# Absurdist
# absurdist_url = 'https://www.goodreads.com/list/show/24776.Absurdist_Fiction'
# absurd_result = requests.get(absurdist_url).text
# absurd_doc = BeautifulSoup(absurd_result, 'html.parser')

# book_elements = absurd_doc.find_all('tr', {'itemtype' : 'http://schema.org/Book'})
# with open('absurdist_books.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
    
#     writer.writerow(['Title', 'Author', 'Rating', 'Genre'])
    
#     for book in book_elements:
#         title_uncleaned = book.find('a',{ 'class' :'bookTitle' })
#         author_uncleaned = book.find('a', { 'class' : 'authorName' })
#         rating_uncleaned = book.find('span',{ 'class' : 'minirating' })
        
#         title = title_uncleaned.text.strip()
#         author = author_uncleaned.text.strip()
#         rating = rating_uncleaned.text.strip()
#         genre = 'Absurdist Fiction'
        
#         writer.writerow([title, author, rating, genre])
        
# Science Fiction
# scifi_url = 'https://www.goodreads.com/list/show/19341.Best_Science_Fiction'
# scifi_result = requests.get(scifi_url).text
# scifi_doc = BeautifulSoup(scifi_result, 'html.parser')

# book_elements = scifi_doc.find_all('tr', {'itemtype' : 'http://schema.org/Book'})

# with(open('scifi_books.csv', 'w', newline='')) as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Title', 'Author', 'Rating', 'Genre'])
    
#     for book in book_elements:
#         title_uncleaned = book.find('a', {'class' : 'bookTitle'})
#         author_uncleaned = book.find('a', {'class' : 'authorName'})
#         rating_uncleaned = book.find('span', {'class' : 'minirating'})
        
#         title = title_uncleaned.text.strip()
#         author = author_uncleaned.text.strip()
#         rating = rating_uncleaned.text.strip()
#         genre = 'Science Fiction'
        
#         writer.writerow([title, author, rating, genre])
        
# Psychological Thriller

comedy_url = 'https://www.goodreads.com/list/show/4208.Funniest_Books_Ever';
comedy_result = requests.get(comedy_url).text
comedy = BeautifulSoup(comedy_result, 'html.parser')

book_elements = comedy.find_all('tr', {'itemtype' : 'http://schema.org/Book'})

with(open('comedy_books.csv', 'w', newline='')) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Author', 'Rating', 'Genre'])
    
    for book in book_elements:
        title_uncleaned = book.find('a', {'class' : 'bookTitle'})
        author_uncleaned = book.find('a', {'class' : 'authorName'})
        rating_uncleaned = book.find('span', {'class' : 'minirating'})
        
        title = title_uncleaned.text.strip()
        author = author_uncleaned.text.strip()
        rating = rating_uncleaned.text.strip()
        genre = 'comedy'
        
        writer.writerow([title, author, rating, genre]) 