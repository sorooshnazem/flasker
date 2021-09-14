from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
#def index():
#	return "<h1>Hello World!</h1>"

def index():
	first_name= 'Samira'
	family_name= '<strong>Hadidi</strong>'
	favorite_pizza= ['Margherita','Gorgo Cipolla', 'Prosciutto','Funghi']
	return render_template('index.html', first_name=first_name,
	 family_name=family_name, favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', user_name=name)

# Invalid URL Error
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Internal Server Eoor
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500