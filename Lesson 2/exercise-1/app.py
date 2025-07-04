# Exercise 1: Flask Pizza Ordering System
# This application demonstrates a simple pizza ordering system with potential debugging challenges
# including database operations, form handling, and enum usage.
#
# Key Features:
# - Uses Flask and SQLAlchemy for web and database operations
# - Demonstrates use of Python enums for pizza sizes, crusts, and toppings
# - Handles form submissions and displays orders
# - Includes debugging print statements and comments for learning

from flask import Flask, flash, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import enum

# Initialize Flask application
app = Flask(__name__)
# Configure SQLite database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# Disable SQLAlchemy modification tracking for performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Set secret key for session management and flash messages
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Initialize database object
db = SQLAlchemy(app)

###############################################
### MODELS - Database Schema Definitions
###############################################

# Enum for pizza sizes - helps prevent invalid size values
class PizzaSize(enum.Enum):
    SMALL = '12 Inch'
    MEDIUM = '16 Inch'
    LARGE = '20 Inch'

# Enum for crust types - ensures only valid crust types are used
class CrustType(enum.Enum):
    THIN = 'Thin'
    THICK = 'Thick'
    GLUTEN_FREE = 'Gluten Free'

# Enum for available toppings - maintains consistency in topping names
class ToppingType(enum.Enum):
    SOY_CHEESE = 'Soy Cheese'
    MUSHROOMS = 'Mushrooms'
    ONIONS = 'Onions'
    SPINACH = 'Spinach'
    PINEAPPLE = 'Pineapple'

# Main pizza order model - stores order details
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each order
    order_name = db.Column(db.String(80), unique=False, nullable=False)  # Customer name
    size = db.Column(db.Enum(PizzaSize), nullable=False)  # Pizza size using enum
    crust_type = db.Column(db.Enum(CrustType), nullable=False)  # Crust type using enum
    toppings = db.relationship('PizzaTopping')  # One-to-many relationship with toppings
    fulfilled = db.Column(db.Boolean, default=False)  # Order status flag

# Topping model - stores individual toppings for each pizza
class PizzaTopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each topping
    topping_type = db.Column(db.Enum(ToppingType))  # Type of topping using enum
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))  # Reference to parent pizza

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

###############################################
### ROUTES - Application Endpoints
###############################################

@app.route('/')
def home():
    """Display homepage showing all unfulfilled pizza orders."""
    # Query database for all unfulfilled orders
    all_pizzas = Pizza.query.filter_by(fulfilled=False)
    return render_template('home.html', pizza_orders=all_pizzas)

@app.route('/order', methods=['GET'])
def pizza_order_form():
    """Display the pizza ordering form with all available options."""
    return render_template(
        'order.html',
        sizes=PizzaSize,  # Pass enum for size options
        crust_types=CrustType,  # Pass enum for crust options
        toppings=ToppingType)  # Pass enum for topping options

@app.route('/order', methods=['POST'])
def pizza_order_submit():
    """Process pizza order submission and save to database."""
    # Extract form data from request
    order_name = request.form.get('order_name')
    pizza_size_str = request.form.get('pizza_size')
    crust_type_str = request.form.get('crust_type')
    toppings_list = request.form.getlist('toppings')  # Get multiple selected toppings

    # Create new pizza order object
    pizza = Pizza(
        order_name=order_name,
        size=pizza_size_str,  # Note: This expects enum value, not enum object
        crust_type=crust_type_str)  # Note: This expects enum value, not enum object
    
    # Debug print to see what size value is being stored
    print(pizza.size)

    # Add selected toppings to the pizza order
    for toppings in toppings_list:
        pizza.toppings.append(PizzaTopping(topping_type=toppings))

    # Save order to database
    db.session.add(pizza)
    db.session.commit()
    
    # Show success message to user
    flash('Your order has been submitted!')
    
    return redirect(url_for('home'))

@app.route('/fulfill', methods=['POST'])
def fulfill_order():
    """Mark a pizza order as fulfilled."""
    # Get pizza ID from form submission
    pizza_id = request.form.get('pizza_id')
    # Find the specific pizza order in database
    pizza = Pizza.query.filter_by(id=pizza_id).one()

    # Mark order as fulfilled
    pizza.fulfilled = True
    db.session.add(pizza)
    db.session.commit()
    
    # Show confirmation message
    flash(f'The order for {pizza.order_name} has been fulfilled.')
    return redirect(url_for('home'))

# Run the application in debug mode for development
if __name__ == '__main__':
    app.run(debug=True)