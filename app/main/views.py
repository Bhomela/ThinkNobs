from flask import render_template, session, redirect, url_for, current_app, flash, request
from .. import db
from .forms import NameForm
from ..email import send_email
from . import main
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def main():
    form = NameForm()
    if form.validate_on_submit():        
        user = User(name=form.name.data,
                    email = form.email.data,
                    phone_number = form.phone_number.data,
                    message = form.message.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank You. Message Sent.')
        session['known'] = False
        # add personal email once configured
        emails = [user.email,'bhomelaj@gmail.com']
        for email in emails:
            send_email(email, 'New User','mail/template', user=user, name = user.name)
        form.name.data = ''
        form.email.data = ''
        form.phone_number.data = ''
        form.message.data = ''
        session['known'] = True
        session['name'] = user.name
        redirect(url_for('main.main'))
    return render_template('main.html', form=form, name=session.get('name'))

