from xyz_blog import app, login_manager
import datetime
from flask import Flask, render_template, request, flash, session, url_for, redirect
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import SignupForm, PublishForm, LoginForm
from models import db, User, Entries, ROLE_USER, ROLE_ADMIN
import os


@login_manager.user_loader
def load_user(uid):
    return User.query.filter_by(uid = session['uid']).first()


# LOGIN USER
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if 'email' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('login.html', form=form)
        else:
            session['email'] = form.email.data
        return redirect(url_for('profile'))

    elif request.method == 'GET':
        return render_template('login.html', form=form)


# SIGN-UP
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'email' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            return redirect(url_for('profile'))

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


# LOGOUT
@app.route('/signout')
def signout():

    if 'email' not in session:
        return redirect(url_for('login'))

    session.pop('email', None)
    return redirect(url_for('home'))


# PROFILE / CREATE A POST - MEMBERS
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = PublishForm()

    if 'email' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(email = session['email']).first()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('profile.html', form=form, user=user)
        else:
            newentry = Entries(form.topic.data, form.article.data, session['email'], user.firstname, user.lastname, datetime.datetime.now())
            db.session.add(newentry)
            db.session.commit()

            return redirect(url_for('home'))

    elif request.method == 'GET':
        if user.role == ROLE_ADMIN:
            return redirect(url_for('admin'))
        if user.role == ROLE_USER:
            return render_template('profile.html', form=form, user=user)


# HOME
@app.route('/')
def home():

    bpost = Entries.query.order_by(Entries.pub_id.desc()).first()

    post_tag = Entries.query.filter_by(topic = Entries.topic, pub_date =Entries.pub_date, pub_id = Entries.pub_id).all()
    return render_template('index.html', bpost=bpost, post_tag = post_tag)

# tag posts
@app.route('/tag/<pub_id>',)
def tag_entry(pub_id):
    form = PublishForm()
    bpost = Entries.query.filter_by( pub_id=pub_id).first()

    post_tag = Entries.query.filter_by(topic = Entries.topic, pub_date =Entries.pub_date, pub_id = Entries.pub_id).all()
    return render_template('index.html', bpost=bpost, post_tag =post_tag)


# ABOUT
@app.route('/about')
def about():
  return render_template('about.html')


# ADMIN PANEL
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = PublishForm()

    if 'email' not in session:
        return redirect(url_for('login'))

    bpost = Entries.query.filter_by(pub_id = Entries.pub_id).all()

    return render_template('admin.html', bpost=bpost, form = form)

@app.route('/delete/<pub_id>',)
def delete_entry(pub_id):
    post_delete = Entries.query.filter_by( pub_id=pub_id).first()
    db.session.delete(post_delete )
    db.session.commit()

    return redirect(url_for('admin'))

@app.route('/edit/<pub_id>', methods=['GET', 'POST'])
def edit_entry(pub_id):
    post_edit = Entries.query.filter_by( pub_id=pub_id).first()
    form = PublishForm(request.form, post_edit)
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('admin.html', form=form)
        else:
            form.populate_obj(post_edit)
            db.session.add(post_edit)
            db.session.commit()
            return redirect(url_for('admin'))
    return render_template('admin.html', form=form)

@app.route('/add/', methods=['GET', 'POST'])
def add_post_admin():
    form = PublishForm()

    user = User.query.filter_by(email = session['email']).first()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('admin.html', form=form, user=user)
        else:
            new_entry = Entries(form.topic.data, form.article.data, session['email'], user.firstname, user.lastname, datetime.datetime.now())
            db.session.add(new_entry)
            db.session.commit()

            return redirect(url_for('admin'))

    elif request.method == 'GET':
        return render_template('admin.html', form=form, user=user)

# test connection
'''@app.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken.' '''


#if __name__ == '__main__':


    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)




