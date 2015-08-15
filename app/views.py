from flask import render_template, flash, redirect,url_for,session,request,g
from flask.ext.login import login_user,logout_user,current_user,login_required
from app import app,db,lm,oid
from .forms import LoginForm
from .models import User

@app.before_request
def before_request():   
	print('break 0-------------------------- %r -----------------------------------' % current_user)
	g.user = current_user

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler   #a new decorator
def login():
	print('break 1--------------------------------------------------------------')
	if g.user is not None and g.user.is_authenticated():  #是否已认证
		print('break 2--------------------------------------------------------------')
		return redirect(url_for('index'))         #是的话直接进入Index
	form = LoginForm()             
	if form.validate_on_submit():
		print('break 3--------------------------------------------------------------')
		session['remember_me'] = form.remember_me.data  #把remember_me的勾选状态保存到session
		return oid.try_login(form.openid.data, ask_for=['nickname', 'email']) #使用flsk-openid认证
	print('break 4--------------------------------------------------------------')
	return render_template('login.html',
		title = 'Sign In',
		form = form,
		providers = app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index/')
def index():
	print('break 5--------------------------------------------------------------')
	user = g.user
	posts = [
		{
			'author':{'nickname':'john'},
			'body': 'Beautifu day'
		},
		{
			'author':{'nickname':'susan'},
			'body':'fuck you lady'
		}
	]
	return render_template('index.html',title = 'Home',user = user,posts = posts)
		
@lm.user_loader
def load_user(id):         #从数据库中取出这个id的数据
	print('break 6--------------------- %r ----------------------------------------' % id)
	return User.query.get(int(id))
	
@oid.after_login
def after_login(resp):
    print('break 7--------------------------------------------------------------')
    if resp.email is None or resp.email == "":     #需要一个合法的邮箱地址
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()   #到数据库中找这个邮箱地址
    print('break 8--------------------------------------------------------------')
    if user is None:             #如果找不到
        print('break 9--------------------------------------------------------------')
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email) #注册新用户
        db.session.add(user)
        db.session.commit()
        print('break4-------------------------------------------------------')
        remember_me = False
    if 'remember_me' in session:           #读取session里的remember_me
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    print('break 10--------------------------------------------------------------')
    login_user(user, remember = remember_me)    #登陆
    return redirect(request.args.get('next') or url_for('index'))   #如果在 next 页没有提供的情况下，我们会重定向到首页，否则会重定向到 next 页。


@app.route('/logout')
def logout():
    print('break 11--------------------------------------------------------------')
    logout_user()
    return redirect(url_for('login'))