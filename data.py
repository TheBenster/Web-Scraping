import pandas as pd
import csv
from random import choices

book_choice = input('Pick a genre: ')

if book_choice == 'Horror':
    df = pd.read_csv('horror_books.csv')
elif book_choice == 'Absurdist Fiction':
    df = pd.read_csv('absurdist_books.csv')
    
genre = choices(df.Genre)

genre_string = ''.join(genre)


def book_chooser(df):
    # book_choice = input('Pick a genre')
    book_title = df.Title
    
    random_title = choices(book_title)
    book_string = ''.join(random_title)
    
    find_author = df.loc[df['Title'] == book_string].Author
    author_string = ''.join(find_author)
    
    
    if book_choice == genre_string:
        # df = pd.read_csv('horror_books.csv')
        print(f'Your random book is {book_string} by {author_string}')
    
book_chooser(df)
    



print(genre_string)
# ### ABSURDIST FICTION ###
# absurd_df = pd.read_csv('absurdist_books.csv')
# ### ABSURDIST FICTION ###


# book_title = absurd_df.Title; 
# book_author = absurd_df.Author; 

# book_choice = input('Give me a genre: ')

# # Gets random book title and returns a list object of that title, then turns it into a string using .join
# random_choice = choices(book_title)
# book_string = ''.join(random_choice)

# # Returns author of the random book described above, then turns it into a string
# auth = absurd_df.loc[absurd_df['Title'] == book_string].Author
# auth_string = ''.join(auth)

# ### HORROR ###
# horror_df = pd.read_csv('horror_books.csv')
# ### HORROR ###


# random_horror = choices(horror_df.Title)
# horror_string = ''.join(random_horror)

# horror_auth = horror_df[horror_df['Title'] == horror_string].Author
# hor_auth_string = ''.join(horror_auth)


# if book_choice == 'Absurdist Fiction':
#     print(f'Your random book is {book_string} by {auth_string}') 
# elif book_choice == 'Horror':
#     print(f'Your random book is {horror_string} by {hor_auth_string}')
    
# Whatever the KEY to the random_choice book is, we need to take that number to find the AUTHOR title
# so if it's possible, we need to search by string of the book title, to find the key of the appropriate author so something like  book_author OF random_choice