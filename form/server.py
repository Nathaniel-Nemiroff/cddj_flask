from flask import Flask,render_template,request,redirect,session
app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
	if not 'hits' in session:
		session['hits']=0
	session['hits']+=1
	print 'HITS: ' + str(session['hits'])
	return render_template("index.html")#,hits=session['hits'])

@app.route('/hitsinc',methods=['POST'])
def inchits():
	session['hits']+=1
	return redirect('/')

@app.route('/hitsreset',methods=['POST'])
def resethits():
	session['hits']=0
	return redirect('/')




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
		


@app.route('/reg', methods=['POST'])
def register():
	return render_template('reg.html')

@app.route('/user',methods=['POST'])
def create_user():
	print "New User:"

	session['name'] = request.form['name']
	session['pswd'] = request.form['pswd']


	prtpwd = ''
	for i in range(0,len(session['pswd'])):
		prtpwd+='*'


	print "   Name: " + session['name']
	print "   pass: " + prtpwd

	return redirect('/')





app.run(debug=True)
