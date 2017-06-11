from flask import Flask,render_template,request,redirect,session,flash
import random

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


@app.route('/random')
def rand():
	if not 'rand' in session:
		session['rand']=random.randrange(0,101)
	return render_template('rand.html',answer='none')

@app.route('/random',methods=['POST'])
def randchk():
	rettext=""
	if int(session['rand']) == int(request.form['answer']):
		rettext='right'
	elif int(session['rand']) < int(request.form['answer']):
		rettext='high'
	else:
		rettext='low'
	return render_template('rand.html',answer=rettext)

@app.route('/resetrand',methods=['POST'])
def resetrand():
	session.pop('rand')
	return redirect('/random')


@app.route('/ninjamoney')
def ninjamoney():
	session['wealth']=0
	session['log']=''
	session['css']=random.randrange(0,10000000000000000000)
	return redirect('/ninjamoneygame')

@app.route('/ninjamoneygame')
def ninjamoneygame():
	return render_template('ninjamoney.html',gold=session['wealth'],log=session['log'])

@app.route('/process_action',methods=['POST'])
def processaction():
	addmoney=0#random.randrange(0, 101)
	action=request.form['building']

	if action == 'farm':
		addmoney = random.randrange(10,20)
	elif action == 'cave':
		addmoney = random.randrange(5,10)
	elif action == 'house':
		addmoney = random.randrange(2,5)
	elif action == 'casino':
		r = random.randrange(0,2)
		print r
		if r:
			addmoney = random.randrange(0,50)
		else:
			addmoney = - random.randrange(0,50)

	session['log']+="Earned "
	session['log']+=str(addmoney)
	session['log']+=" golds from the "
	session['log']+=action
	session['log']+="!"
	session['log']+='\n'
	print session['log']

	session['wealth']+=addmoney
	return redirect('/ninjamoneygame')


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
