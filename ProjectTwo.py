from flask import Flask
from flask import render_template #Last import at the beginning of the file

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/issues')
def issues():
    return render_template('issues.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
