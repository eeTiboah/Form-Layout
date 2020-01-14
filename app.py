from flask import Flask, render_template, session, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email



app=Flask(__name__)

app.config['SECRET_KEY']='secretkeyyy'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

class RegistrationForm(FlaskForm):
	first_name=StringField('First Name', validators=[DataRequired()])
	last_name=StringField('Last Name', validators=[DataRequired()])
	birthday=DateField('Birthday',validators=[DataRequired()], format="%m/%d/%Y")
	gender=RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
	email=StringField('Email', validators=[DataRequired(), Email()])
	phone_number=IntegerField('Phone Number', validators=[DataRequired()])
	subject=SelectField('Subject', choices=[('subject1', 'Subject 1'),('subject2', 'Subject 2'), ('subject3', 'Subject 3')])
	submit=SubmitField('Submit')


@app.route('/', methods=['POST', 'GET'])
def home():

	form=RegistrationForm()
	print(form.data)
	if form.validate_on_submit():
		session['firstName'] = form.first_name.data
		session['lastName'] = form.last_name.data
		session['birthday'] = form.birthday.data
		session['gender'] = form.gender.data
		session['email'] = form.email.data
		session['phone_number'] = form.phone_number.data
		session['subject'] = form.subject.data

		return redirect(url_for('show'))
	return render_template('home.html', form=form)


@app.route('/show')
def show():
	form=RegistrationForm()
	return render_template('show.html', form=form)

@app.after_request
def after_request(response):
	response.headers["Cache-Control"] = "no-cache,no-store, must-revalidate, public, max-age=0"
	response.headers["Expires"] = '0'
	response.headers["Pragma"] = "no-cache"
	return response

if __name__=='__main__':
	app.run(debug=True)
	