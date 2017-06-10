from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def proc():
	name = request.form['name']
	print name
	return render_template('process.html',name=request.form['name'],loc=request.form['loc'],lang=request.form['lang'],com=request.form['comment'])

@app.route('/ninja')
def ninjas():
	return render_template("ninja.html",link="/static/Ninjas/tmnt.png")

@app.route('/ninja/<color>')
def ninja(color):
	ret = 'notapril.jpg'
	n = {'blue':'leonardo.jpg','orange':'michelangelo.jpg','red':'raphael.jpg','purple':'donatello.jpg'}
	if color in n:
		ret = n[color]
	print"{{url_for('static',filename='Ninjas/" + ret + "')}}"
	return render_template('ninja.html',link="/static/Ninjas/"+ret)
		

@app.route('/dojos/new')
def dn():
	return render_template("dojos.html")

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
