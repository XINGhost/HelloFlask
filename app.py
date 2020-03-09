from flask import Flask, url_for, redirect,request,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/html')
def learnhtml():
    return render_template('learn/learnhtml.html')

@app.route('/css')
def learncss():
    return render_template('learn/learncss.html')

@app.route('/bootstrap')
def learnbootstrap():
    return render_template('learn/learnbootstrap.html')

@app.route('/javascript')
def learnjavascript():
    return render_template('learn/learnjavascript.html')


if __name__ == '__main__':
    app.run(
        debug= True
    )
