from flask import Flask, render_template
#HTML - язык гипертекстовой информации (разметка)
#CSS - каскадные таблицы стилей

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')



app.run(debug=True)