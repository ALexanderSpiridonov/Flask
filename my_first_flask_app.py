from flask import Flask, render_template, url_for

app=Flask(__name__)

posts = [
    {
        'section': 'Mastitis checkup',
        'title': 'Mastitis information',
        'content': 'Here you can see an information about mastitis', 
        'date_posted': 'Jan 01, 2020'
    },
    {
        'section': 'Ketosis checkup',
        'title': 'Ketosis information',
        'content': 'Here you can see an information about ketosis',
        'date_posted': 'Jan 01, 2020'
    }
]

@app.route("/") # home page 
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") # home page 
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)