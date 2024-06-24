from flask import Flask, render_template, request, redirect, url_for
import pdfkit
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/resume', methods=['POST'])
def generate_resume():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    education = request.form['education']
    experience = request.form['experience']
    skills = request.form['skills']

    rendered = render_template('resume.html', name=name, email=email, phone=phone, education=education, experience=experience, skills=skills)

    pdfkit.from_string(rendered, 'resume.pdf')

    return redirect(url_for('static', filename='resume.pdf'))

if __name__ == '__main__':
    app.run(debug=True)
