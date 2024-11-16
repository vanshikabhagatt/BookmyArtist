from flask import Flask, render_template

app = Flask(__name__)

artists = {
    1: {"name": "Vanshika", "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "song_type": "Pop"},
    2: {"name": "kanishka", "video_url": "https://www.youtube.com/embed/3JZ_D3ELwOQ", "song_type": "Jazz"},
    3: {"name": "yajvi", "video_url": "https://www.youtube.com/embed/tgbNymZ7vqY", "song_type": "Rock"}
}

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Login page route
@app.route('/login')
def login():
    return render_template('login.html')

# Artists listing route
@app.route('/artists')
def artists():
    # List of artists with IDs and names (you can expand this list as needed)
    artists = [
        {'id': 1, 'name': 'Kushagra Raj'},
        {'id': 2, 'name': 'Arijit Singh'},
        {'id': 3, 'name': 'Freddie Leiba'},
        {'id': 4, 'name': 'Jennifer Lopez'},
        {'id': 5, 'name': 'John Doe'}
    ]
    return render_template('artists.html', artists=artists)

# Booking page route for each artist
@app.route('/artist/<int:artist_id>')
def book_artist(artist_id):
    return render_template('booking.html', artist_id=artist_id)


@app.route('/cart')
def cart():
    # Render the cart page template
    return render_template('cart.html')

@app.route('/help')
def help_center():
    return render_template('help.html')

@app.route('/feed')
def feed():
    return render_template('feed.html')

# Account page route
@app.route('/account')
def account():
    return render_template('account.html')


if __name__ == "__main__":
    app.run(debug=True)
