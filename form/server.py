from flask import Flask,render_template,request,redirect,session,flash
import random,re,datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
BDAY_REGEX = re.compile(r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9]')

app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
	session['regvld']=""
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
def reg():
	session['css']='sty.css?q='+str(random.randrange(0,10000000000000000000))
	session['reg']=False
	
	return redirect('/register', code=307)

@app.route('/register', methods=['POST'])
def register():

	if not session['reg']:
		session['reg']=True
		return render_template('reg.html')

	email = request.form['email']
	first = request.form['first']
	last = request.form['last']
	pswd = request.form['pass']
	conf = request.form['conf']

	check=True
	for itm in request.form:
		print request.form[itm]
		if len(request.form[itm]) < 1:
			flash('Cannot leave any feild empty!')
			check=False
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Submit a valid email!')
		check=False
	if(re.search(r'\d', first)):
		flash('First name cannot contain numbers!')
		check=False
	if(re.search(r'\d', last)):
		flash('Last name cannot contain numbers!')
		check=False
	if len(pswd) < 8:
		flash('Password must be at least 8 characters long!')
		check=False
	if not re.search(r'\d',pswd):
		flash('Password must have at least one number!')
		check=False	
	if pswd.islower():
		flash('Password must have at least one capital letter!')
		check=False
	if not pswd==conf:
		flash('Passwords must match!')
		check=False

	date = 0
	now = datetime.datetime.now()

	if not BDAY_REGEX.match(request.form['bday']):
		flash('Date must be valid (mm/dd/yy)')
		check=False
	else:
		date = datetime.datetime.strptime(request.form['bday'],"%m/%d/%y")
		if date.year > 2017:
			flash('Date must not be after today!')
			check=False
		elif date.year == 2017:
			if date.month > now.month:
				flash('Date must not be after today!')
				check=False
			elif date.month == now.month:
				if date.day > now.day:
					flash('Date must not be after today!')
					check=False
	

	if not check:
		return render_template('reg.html')
	return redirect('/user',code=307)

@app.route('/user',methods=['POST'])
def create_user():	

	return render_template('usr.html')





app.run(debug=True)
