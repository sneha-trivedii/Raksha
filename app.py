from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from twilio.rest import Client
from geopy.geocoders import Nominatim
from config import Config
from flask_migrate import Migrate
from models import db, User, EmergencyContact
from forms import RegistrationForm, LoginForm, EmergencyContactForm

app = Flask(__name__)
app.config.from_object(Config)
#db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check email and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Clear session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))  # Redirect to login page

@app.route('/dashboard')
@login_required
def dashboard():
    contacts = EmergencyContact.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', contacts=contacts)

@app.route('/add-contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    form = EmergencyContactForm()
    if form.validate_on_submit():
        contact = EmergencyContact(name=form.name.data, phone=form.phone.data, user_id=current_user.id)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_contact.html', form=form)

@app.route('/sos')
@login_required
def sos_alert():
    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
    contacts = EmergencyContact.query.filter_by(user_id=current_user.id).all()
    location = get_gps_location()
    for contact in contacts:
        message = client.messages.create(
            body=f"Emergency! I need help. My location: {location}",
            from_=Config.TWILIO_PHONE_NUMBER,
            to=contact.phone
        )
    flash('SOS Alert sent!', 'info')
    return redirect(url_for('dashboard'))

def get_gps_location():
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode("New Delhi, India")  # Replace with real GPS data
    return f"{location.latitude}, {location.longitude}" if location else "Unknown Location"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
