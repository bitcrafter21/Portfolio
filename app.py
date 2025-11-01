from flask import Flask,render_template
import os

app=Flask(__name__)

#---------------------------------------Front Page---------------------------------------#
@app.route('/')
def index():
    return render_template('index.html')

#---------------------------------------About Page---------------------------------------#
@app.route('/about')
def about():
    return render_template('about.html')

#---------------------------------------Experience Page---------------------------------------#
@app.route('/experience')
def experience():
    return render_template('experience.html')

#---------------------------------------Projects Page---------------------------------------#
@app.route('/projects')
def projects():
    return render_template('projects.html')

#---------------------------------------Skills Page---------------------------------------#
@app.route('/skills')
def skills():
    return render_template('skills.html')

#---------------------------------------Certifications Page---------------------------------------#
@app.route('/certification')
def certification():
    return render_template('certification.html')

#---------------------------------------Contact and Feedback Page---------------------------------------#
@app.route('/contacts',methods=['GET','POST'])
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
