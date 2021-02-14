"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

###
# Routing for your application.
###

def format_date_joined(date):
    
    date_joined = datetime.date(2016, 2, 7)
    return date_joined.strftime("%B, %Y")

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Kyle Burke")

@app.route('/profile/')
def profile():
    params = {}
    #name = "Kyle Burke", tag = "@kburke629", addr = "Kingston, Jamaica", joined = format_date_joined("02/14/2016")
    params['name'] = "Kyle Burke"
    params['tag'] = "@kburke629"
    params['addr'] = "Kingston, Jamaica"
    params['joined'] = format_date_joined("02/14/2016")
    params['num_posts'] = 700
    params['num_following'] = 425
    params['num_followers'] = 600
    params['bio'] = "My name is Kyle Burke, I like to code and play instruments. I have no clue what to write lol cowboy emoji. Lorem ipsum dolor sit amet I am trying to fill out space so the paragraph looks bigger lorem ipsum haha"
    return render_template('profile.html', params = params)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
