from flask import url_for,render_template,flash,redirect,request,Blueprint
from flask_login import current_user,login_user,logout_user,login_required

from companyblog import db
from companyblog.models import User,BlogPost
from companyblog.users.forms import LoginForm,RegistrationForm,UpdateUserForm

from companyblog.users.picturehandler import addProfilePic

users = Blueprint('users',__name__)


# Regiter
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

# Login
@users.route('/register',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.checkPassword(form.password.data) and user is not None:
            login_user(user)
            flash('User Login Sucessfully')

            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html',form=form)

# Logout 
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

# Account
@users.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data :
            username = current_user.username
            pic = addProfilePic(form.picture.data, username)
            current_user.profile_iamge = pic
        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()

        flash('User account updated')
        return redirect(url_for('users.account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    profileImg = url_for('static',filename = "profile_pics/" + current_user.profile_iamge)
    return render_template('account.html',profile_image=profileImg, form=form)

# Users Account of blog posts
@users.route('/<username>')
def userPosts(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
     return render_template('user_blog_posts.html',blog_posts=blog_posts,user=user) 
