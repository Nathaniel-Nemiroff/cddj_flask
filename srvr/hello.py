from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')

def hello():
	return render_template('index.html')

@app.route('/proj')

def proj():
	return render_template('proj.html')

@app.route('/about')

def about():
	return render_template('about.html')

app.run(debug=True)


