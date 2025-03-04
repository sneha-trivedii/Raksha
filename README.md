# Raksha
Overview

Raksha is a web-based safety application designed to provide women with a quick and effective way to reach out for help in emergency situations. The application enables users to store emergency contacts, track and share their live GPS location, send SOS alerts via SMS, and simulate a fake call to escape threatening situations.

The system is built using Flask as the backend framework, SQLite for database management, and Bootstrap for a user-friendly and responsive interface. The Twilio API is integrated for sending emergency SMS alerts, and Google Maps API is used to provide accurate location tracking.

Key Features
User Authentication (Signup & Login)
Raksha includes a secure authentication system that allows users to create an account and log in to access its features. User credentials, including username, email, and password, are securely stored in the database using Flask-Login and password hashing mechanisms.

Emergency Contacts Management
Users can add multiple emergency contacts by providing names and phone numbers. These contacts are stored in the database and displayed on the dashboard, allowing users to quickly access their information. Each contact has a call button that enables users to initiate a call with a single click.

Live GPS Tracking
The application uses the browser's Geolocation API to fetch the user's real-time latitude and longitude coordinates. When the GPS tracking button is clicked, the user's current location is displayed on Google Maps, allowing them to monitor their position accurately. This feature ensures that users can easily share their location with emergency contacts when needed.

SOS Alert via SMS
In emergency situations, users can trigger an SOS alert, which sends an SMS message containing their live GPS location to all saved emergency contacts. The Twilio API is used to send these messages. The application ensures that messages are formatted correctly using the E.164 phone number standard, which helps prevent delivery failures.

Fake Call Simulation
To help users escape uncomfortable or dangerous situations, Raksha includes a fake call feature. When activated, the app triggers an alert that mimics an incoming phone call from an emergency number. This feature can be used to create a distraction or excuse to leave a threatening environment.
