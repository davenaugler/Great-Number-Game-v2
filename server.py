from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "This is the Coding Dojo Counter Application"

@app.route('/')
def index():
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1,100)
        session['page'] = 'start'
        session['text'] = ''
        session['button'] = 'Submit'
        session['action'] = 'number'
        session['count_text'] = ''
        session['count'] = 0
        print(session['rand_num'])
    return render_template("index.html")

@app.route('/number', methods=["POST"])
def numbers():
    num = int(request.form['number'])
    # if to low
    if num < session['rand_num']:
        session['text'] = 'Too low!'
        session['color'] = 'red'
        session['count'] += 1
        session['count_text'] = 'Guess Attempts: ' + str(session['count'])
        
        print(session['page'])
        
    # if to high
    elif num > session['rand_num']:
        session['text'] = 'Too high!'
        session['color'] = 'orange'
        session['count'] += 1
        session['count_text'] = 'Guess Attempts: ' + str(session['count'])
        
    # Correct
    else:
        session['count'] += 1
        session['count_text'] = 'Guess Attempts: ' + str(session['count'])
        session['text'] = str(session['rand_num']) + ' was the number!'
        session['color'] = 'green'
        session['button'] = 'Play again'
        session['action'] = 'play-again'
    return redirect('/')

@app.route('/play-again', methods=['POST'])
def play():
    session.clear()
    return redirect('/')
    


if __name__=="__main__":
    app.run(debug=True)