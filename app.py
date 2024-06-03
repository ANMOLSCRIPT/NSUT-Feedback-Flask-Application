from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

feedback_list = []

@app.route('/')
def hello_world():
    return render_template('index.html', feedback_list=feedback_list)

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    title = request.form.get('title')
    desc = request.form.get('desc')
    
    feedback = {
        'title': title,
        'desc': desc,
        'date_created': datetime.utcnow()
    }
    
    feedback_list.append(feedback)
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
