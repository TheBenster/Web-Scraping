# Goodreads Book Scraper and Flask Website
This project is a web scraping app that scrapes book information from Goodreads, converts it to a CSV file, and then displays the data on a Flask website with a dropdown menu for selecting genres.

# Features
Scrapes book data from Goodreads.
Converts book data to a CSV file.
Provides a user-friendly web interface.
Allows users to select a genre from the dropdown menu.
Displays a random book from the selected genre.

# Requirements
Python 3.x
Beautiful Soup (for web scraping)
Flask (for creating the web interface)

# How to Use
Clone this repository to your local machine.
`git clone https://github.com/TheBenster/Web-Scraping.git`

Install the required Python packages.
`pip install beautifulsoup4 flask`
Run the web scraping script to fetch book data from Goodreads and save it as a CSV file.
`python scraper.py`

Start the Flask web application.
`python app.py`
Open your web browser and access the website at http://localhost:5000.

Select a genre from the dropdown menu and click "Give Me a Book" to get a random book recommendation.

# File Structure
scraper.py: The script for scraping Goodreads book data and saving it as a CSV file.
app.py: The Flask web application for displaying the data and allowing users to select genres.
poetry_books.csv: The CSV file where the scraped book data is saved.
templates/: Contains HTML templates for the website.
Configuration
You can modify the scraping URL and genre in the scraper.py file to scrape books from different Goodreads lists and assign different genres.

python
`poetry_url = 'https://www.goodreads.com/list/show/107268.Best_Popular_Poetry_Books_on_Goodreads'`
`genre = 'Magical Realism'`

# Credits
This project was created by [Your Name]. You can contact me at [your email] for any questions or feedback.
