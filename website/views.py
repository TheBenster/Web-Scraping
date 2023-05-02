from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
from genres import GENRE_FILES


views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        
        genre = request.form.get('genre')
        
        filename = GENRE_FILES.get(genre)
        
        books = pd.read_csv(filename, encoding='unicode_escape')
        
        book = books.sample(n=1).iloc[0]
        
        return render_template('result.html',  title=book['Title'], author=book['Author'])
    
    
    return render_template('home.html')
    # return "Hello World"

@views.route('/button-clicked')
def button_clicked():
    return redirect(url_for('views.home'))
