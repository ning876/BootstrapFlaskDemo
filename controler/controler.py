# -*- coding: utf-8 -*-
from wtforms.fields import simple,choices,datetime,numeric
#from wtforms.fields import *
from wtforms.validators import DataRequired, Length,NumberRange,InputRequired
from flask_wtf import FlaskForm

from utils.dbSqlite3 import *

class CourseForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        # 从数据库或其他地方获取选项
        result_t,_=GetSql2('select distinct tno ,name from teacher')
        self.tno.choices = [(item[0], item[1]) for item in result_t]

    cno= numeric.IntegerField(u'课程编码' ,validators=[DataRequired(),NumberRange(1, 10000)])
    cname= simple.StringField(u'课程名称' ,validators=[DataRequired(),Length(1, 10)])
    tno = choices.SelectField(u'教师编码')
    submit = simple.SubmitField(u'新增')

class IndexForm(FlaskForm):
    select = choices.SelectField(u'操作类型', choices=[('login', 'Login'), ('register', 'Register'),('course', 'Course')])
    submit = simple.SubmitField(u'跳转')

class LoginForm(FlaskForm):
    userid = numeric.IntegerField(u'用户账号', validators=[DataRequired(),NumberRange(min=2000000, max=202499999, message='Please enter a value between 2000000 and 202499999.')])
    password = simple.PasswordField(u'密码', validators=[Length(0, 10)])
    select = choices.SelectField(u'身份', choices=[('student', 'Student'), ('teacher', 'Teacher')])
    submit = simple.SubmitField(u'登录')

class Register_tmpForm(FlaskForm):
    select = choices.SelectField(u'身份', choices=[('student', 'Student'), ('teacher', 'Teacher')])
    submit = simple.SubmitField(u'去注册')

class Register_StudentForm(FlaskForm):
    userid = numeric.IntegerField(u'用户账号', validators=[DataRequired(),NumberRange(min=202400000, max=202499999, message='Please enter a value between 202400000 and 202499999.')])
    username = simple.StringField(u'用户名', validators=[DataRequired(), Length(1, 20)])
    userprofie = simple.FileField(u"头像",validators=[InputRequired()])
    gender =choices.SelectField(u'性别',choices=[('男','男'),('女','女')])
    birth = datetime.DateField(u"生日",validators=[DataRequired()],format="%Y-%m-%d")
    major = simple.StringField(u'专业', validators=[DataRequired(), Length(1, 50)])
    password = simple.PasswordField(u'密码', validators=[DataRequired(), Length(0, 10)])

    #password_again = simple.SubmitField.
    submit = simple.SubmitField(u'注册')

class Register_TeacherForm(FlaskForm):
    userid = numeric.IntegerField(u'用户账号', validators=[DataRequired(), NumberRange(min=2000000,max=2009999,message='Please enter a value between 2000000 and 2009999.')])
    username = simple.StringField(u'用户名', validators=[DataRequired(), Length(1, 50)])
    password = simple.PasswordField(u'密码', validators=[Length(0, 10)])
    #password_again = simple.SubmitField.
    submit = simple.SubmitField(u'注册')


class AccountForm(FlaskForm):
    secret = simple.PasswordField(u'旧密码', validators=[DataRequired(), Length(0, 10)], render_kw={'placeholder': '旧密码'})
    password = simple.PasswordField(u'新密码', validators=[DataRequired(), Length(0, 10)], render_kw={'placeholder': '新密码'})
    submit = simple.SubmitField(u'修改密码')


class SelectForm(FlaskForm):
    title = simple.StringField(u'课程号', render_kw={'placeholder': '课程号'})
    submit = simple.SubmitField(u'选课')


class DeleteForm(FlaskForm):
    title = simple.StringField(u'课程号', render_kw={'placeholder': '课程号'})
    submit = simple.SubmitField(u'退课')


class ScoreForm(FlaskForm):
    title_sno = simple.StringField(u'学生号', render_kw={'placeholder': '学生号'})
    title_cno = simple.StringField(u'课程号', render_kw={'placeholder': '课程号'})
    title_score = simple.StringField(u'分数', render_kw={'placeholder': '分数'})
    submit = simple.SubmitField(u'录入')