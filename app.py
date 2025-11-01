from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

#---------------------------------------Database Configuration---------------------------------------#
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}"
    f"@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
)
db = SQLAlchemy(app)
class Feedback(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text)

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
    if (request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        feedback=request.form.get('feedback')
        entry=Feedback(name=name,email=email,feedback=feedback)
        db.session.add(entry)
        db.session.commit()
    return render_template('contacts.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
