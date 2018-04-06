
from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/UserSubmit", methods=['GET'])
def getUserInfo():
    uname=request.args.get("username")
    password=request.args.get("password")
    verifypassword=request.args.get("verifypassword")
    errormsg=""

    if  len(uname) < 3 or  len(uname) > 20  or uname.find('@')==-1 or  uname.find('.')==-1 or uname.find(' ')!=-1 :
        errormsg=" Invalid username "
        return render_template('index.html',username=uname,unamemsg=errormsg) 
    #if len(uname)==0:        
     #  return render_template('index.html',username=uname,unamemsg=errormsg)
    elif len(password)==0:
        errormsg="Password is Blank"
        return render_template('index.html',username=uname,passwordmsg=errormsg)
    elif len(verifypassword)==0:       
        errormsg="verifyPassword is Blank"
        return render_template('index.html',username=uname,cpasswordmsg=errormsg)
    elif password != verifypassword:
        errormsg="Password and Confirm password mismatch! "
        return render_template('index.html',username=uname,passwordmsg=errormsg)
       
    elif len(password) < 3 or  len(password) > 20:
        errormsg="Password length can't be less than 3 and greater than 20 characters "
        return render_template('index.html',username=uname,passwordmsg=errormsg)
    else:
        welcomemsg="Welcome"
        return render_template('welcome.html',username=uname,welcomemsg=welcomemsg)


@app.route("/")
def index():
   
    return render_template('index.html')

app.run()