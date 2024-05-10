# Flask modules
from flask import Blueprint, request, redirect, url_for, render_template, flash

# Local modules
from app.models import Clients
from app.modules import db
from app.solutions import s1, s2

routes_bp = Blueprint('routes', __name__, url_prefix="/")


@routes_bp.route('/')
def show_all():
    return render_template('index.html', clients=Clients.query.all())


@routes_bp.route('/crud')
def crud():
    return render_template('crud.html', clients=Clients.query.all())

@routes_bp.route('/q1', methods=['GET', 'POST'])
def question_1():
    if request.method == 'POST':
        input = request.form['email']
        output = s1(input)
        if output != {}:
            flash(f'Showing Referall tree for {input}', 'success')
        else:
            flash(f'Email not found in the database', 'danger')
        return render_template('question_1.html' , output=output)
    return render_template('question_1.html')

@routes_bp.route('/q2', methods=['GET', 'POST'])
def question_2():
    if request.method == 'POST':
        print('post')
        input = request.form['email']
        client = s2(input)
        if client is None:
            flash(f'Email not found in the database', 'danger')
        else:
            flash(f'Showing details for {input}', 'success')
        return render_template('question_2.html', client=client)
    return render_template('question_2.html')

@routes_bp.route('/q3_6')
def question_36():
    return render_template('question_36.html')


@routes_bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or\
           not request.form['email']:
            flash('Please enter all the fields', 'error')
        else:
            client = Clients(
               request.form['name'],
               request.form['email'],
               request.form['referral_email'],
               request.form['points']
            )
            db.session.add(client)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('routes.crud'))
    return render_template('new.html')

@routes_bp.route('/update/<int:client_id>', methods=['GET', 'POST'])
def update(client_id):
    if request.method == 'POST':
        client=Clients.query.get(client_id)
        client.name =request.form['name']
        client.email =request.form['email']
        client.referral_email =request.form['referral_email']
        client.points =request.form['points']
        db.session.commit()
        flash('Record was successfully updated')
        return redirect(url_for('routes.crud'))

    return render_template('update.html', client=Clients.query.get(client_id))

@routes_bp.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        client_id = request.form['delete']
        print(client_id)
        client=Clients.query.get(client_id)
        db.session.delete(client)
        db.session.commit()
        flash('Record was successfully deleted')
        return redirect(url_for('routes.crud'))

