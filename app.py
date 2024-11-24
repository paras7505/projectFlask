from flask import Flask,request,render_template
from markupsafe import escape
from models import Products,user
from database import session

app = Flask(__name__)


@app.route('/') 
def homePage():
    # add_product() 
    get_product()
    return render_template('homePage.html')


@app.route('/hello/')
@app.route('/hello/<name>/')
def greet(name=None):
    return render_template('greet.html' , name = name)


@app.get('/product/')
def details():
    return render_template("products.html",)

#  for post method
@app.post('/form/')
def form_details():
    firstName = request.form['fname']
    lastName = request.form['lname']
    print(request.form)    
    return f"<h1> user details in post method {firstName} {lastName} </h1>"
             
#  using if else 
@app.route('/ifelse/', methods=['POST', 'GET'])
def forms():
    if request.method == 'POST':       
        firstName = request.form.get('fname')
        lastName = request.form.get('lname')
        age = request.form.get('age')
        email = request.form.get('email')
        address = request.form.get('address')
        user_details()
        print(request.form)
    else:
        firstName = request.args.get('fname')
        lastName = request.args.get('lname')
        print(request.form)
    
    return f"{firstName} {lastName} {age} {email} {address}"



# chatgpt code 

@app.route('/ifelsee/', methods=['POST', 'GET'])
def formss():
    if request.method == 'POST':    
        firstName = request.form.get('fname', '')
        lastName = request.form.get('lname', '')
        print("POST data:", request.form)
    else:
        firstName = request.args.get('fname', '')
        lastName = request.args.get('lname', '')
        print("GET data:", request.args)
    
    return f"First Name: {firstName}, Last Name: {lastName}"


# def add_product():
#     product = Products(name = 'product 2' , price = 200 , quantity = 10)
#     session.add(product)
#     session.commit()

def get_product():
    return session.query(Products).all()
    

# @app.get('/product/')
# def all_product():
#     p = get_product()
#     page = "<h1> Products Get</h1>"
#     page += '<ul>'
#     for i in p:
#         page += f"<li> {i.name} , {i.price} , {i.quantity} </li>"
#         print(i.name)
#         page +='<ul>'
#     return 



