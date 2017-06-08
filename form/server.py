from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/users',methods=['POST'])
def create_user():
	print "New User:"

	name = request.form['name']
	email = request.form['email']

	print "   Name: " + name
	print "   Email: " + email
	print request.form

	return redirect('/')
app.run(debug=True)
