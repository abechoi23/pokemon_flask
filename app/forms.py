# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
# from wtforms.validators import DataRequired, EqualTo, Email



# class RegisterForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must Match!')])
#     submit = SubmitField('Register')

# class SignInForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')

# class BlogForm(FlaskForm):
#     title = StringField('Title')
#     body =  TextAreaField('Body')
#     submit = SubmitField('Submit')

# class PokemonForm(FlaskForm):
#     submit = SubmitField('Catch Pokemon')
    
    
    