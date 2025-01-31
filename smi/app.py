from flask import Flask,render_template,abort,redirect,url_for,request
app = Flask(__name__)
userList = []
class User():
    def __init__(self,email,username,password,age,number,description):
            self.email = email
            self.username = username
            self.password = password
            self.age = age
            self.number = number
            self.description = description

@app.route("/")
def home():
    return render_template("home.html",users=userList)

@app.get("/register")
def register():
    return render_template("register.html")

@app.post("/register")
def registerpost():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age')
    number = request.form.get('number')
    description = "qwertyuiopasdfghjklzxcvbnm"
    newUser = User(email,username,password,age,number,description)
    userList.append(newUser)
    return redirect("/")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        for index, i in enumerate(userList):
            if i.email == email:
                if i.password == password:
                    print('success')
                    return redirect(url_for('home'))
        abort(404)
    return render_template('login.html')

@app.route("/user")
def user():
    return render_template("user.html",users=userList)

@app.route("/userupdate")
def userupdate():
    return render_template("userupdate.html",username=userList[0].username if userList and len(userList) > 0 else '',description=userList[0].description if userList and len(userList) > 0 else '')