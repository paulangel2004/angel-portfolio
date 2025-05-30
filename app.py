# app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main landing page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Renders the projects page."""
    return render_template('projects.html')

if __name__ == '__main__':
    # Run the Flask app
    # In a production environment, you'd use a production-ready WSGI server like Gunicorn or uWSGI
    app.run(debug=True) # debug=True allows for auto-reloading and helpful error messages
