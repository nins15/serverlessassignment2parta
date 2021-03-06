from flask import Blueprint, render_template, flash, redirect,url_for,request

from website import db

Register=Blueprint('Register',__name__)


@Register.route('/SignUp',methods=['GET','POST'])
def signup():
    #reqform=RegistrationForm()
    print(request.method)
    if request.method == "POST":
        email = request.form.get('email')

        password1 = request.form.get('password')
        password2 = request.form.get('confirm_password')

        # user = User.query.filter_by(email=email).first()
        # print(user)
        # if user:
        #     print('Email already exists.')
        #     flash('Email already exists.')
        # el
        if len(email) < 4:
            flash('Email must be greater than 3 characters.')

        elif password1 != password2:
            flash('Passwords don\'t match.')
        elif len(password1) < 4:
            flash('Password must be at least  characters.')
        else:
            print('Everything is fine')
            password=password1
            email=email
            mycursor=db.cursor()
            mycursor.execute("INSERT IGNORE INTO user VALUES('"+email+"','"+password+"')")
            db.commit()

    return render_template("Register.html")