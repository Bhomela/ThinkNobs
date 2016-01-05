from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, TextAreaField ,SubmitField
from wtforms.validators import Required, Email, Length


class NameForm(Form):
    name = StringField('Name', validators=[Required()])
    email = StringField('Email Address', validators = [Required(),Email()])
    phone_number = StringField('Phone Number')
    message = TextAreaField('Message')
    submit = SubmitField('Send')
