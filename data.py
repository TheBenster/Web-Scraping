import pandas as pd
import csv
from random import choices

book_choice = input('Pick a genre: ').title()

# declares dataframe based on user input
if book_choice == 'Horror':
    df = pd.read_csv('horror_books.csv')
elif book_choice == 'Absurdist Fiction':
    df = pd.read_csv('absurdist_books.csv')
elif book_choice == 'Philosophy':
    df = pd.read_csv('philosophy_books.csv')

genre = choices(df.Genre)
# Automates the if statement in book_chooser() so i don't have to repeat the if statement above
genre_string = ''.join(genre)

# Takes df declared above, assigns random book and prints the book title and author associated
def book_chooser(df): 
    random_title = choices(df.Title)
    book_string = ''.join(random_title)
    
    find_author = df.loc[df['Title'] == book_string].Author
    author_string = ''.join(find_author)
    
    if book_choice == genre_string:
        # df = pd.read_csv('horror_books.csv')
        print(f'Your random book is {book_string} by {author_string}')
    
book_chooser(df)
    