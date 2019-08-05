from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'Davie'}
    posts = [
        {'title':'论中国的崛起之路','author':'Unkonw','content':'中国之所以能够在短短一百年内崛起，最主要的原因源自于中国凝聚了上下五千年的文化底蕴。有前车之鉴，有史为鉴，纠正前进的方向必然迅速且果断，速见成效！'},
        {'title':'人民币汇率“破7”！央行火线回应：“7”不是年龄，也不是堤坝','author':'新华社','content':'在2016、2018年两度与7元关口擦肩而过之后，人民币兑美元汇率最终还是跌破了7元这个被视为重要心理关口的整数位置。'}
    ]
    return render_template('index.html', user=user,posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('{}请求登录,是否记住我?{}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='登录', form=form)