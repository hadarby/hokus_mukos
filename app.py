from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
# Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

# About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

# Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

# Categories
from pages.categories.categories import categories
app.register_blueprint(categories)

# sign_in_registration
from pages.sign_in_registration.sign_in_registration import sign_in_registration
app.register_blueprint(sign_in_registration)

# logout
from pages.logout.logout import logout
app.register_blueprint(logout)

# Product
from pages.product.product import product
app.register_blueprint(product)

# contact_us
from pages.contact_us.contact_us import contact_us
app.register_blueprint(contact_us)

#profile
from pages.profile.profile import profile
app.register_blueprint(profile)

###### Components
# Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
