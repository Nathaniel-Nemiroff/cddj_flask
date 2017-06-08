from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
	return "hello world"#render_template('success.html')

app.run(debug=True)
