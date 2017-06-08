from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
	print 'home'
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

@app.route('/users/<username>')
def show_usr(username):
	print username
	return render_template("usr.html")

@app.route('/times')
def times():
	return render_template("times.html", h="hello",t=5)

app.run(debug=True)
