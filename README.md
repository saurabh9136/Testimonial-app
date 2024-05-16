--Testimonial Project--
This is a simple testimonial project built using Django. The project allows an admin to upload testimonials, which users can then access and view.

Features:
Admin can add, edit, and delete testimonials.
Users can view the list of testimonials.
Testimonials include a picture, name, text, and rating.

Requirements
Python 3.x
Django 3.x or later
Pillow (for handling image uploads)

Installation
Clone the repository:
git clone https://github.com/yourusername/testimonial-project.git
cd testimonial-project

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install the required packages:

pip install -r requirements.txt

If requirements.txt does not exist, manually install Django and Pillow:
pip install django pillow

Run migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser for accessing the admin site:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the admin site:
Open your browser and go to http://127.0.0.1:8000/admin/, then log in with the superuser credentials you created.

Usage
Admin Operations:

Log in to the admin site at http://127.0.0.1:8000/admin/.
Navigate to the "Testimonials" section.
Add, edit, or delete testimonials.

User Access:
Users can view the list of testimonials by navigating to the appropriate URL, e.g., http://127.0.0.1:8000/emp/testimonials/.

Project Structure
testimonials: Main app for handling testimonials.
models.py: Defines the Testimonial model.
views.py: Handles the display logic for testimonials.
urls.py: Defines the URL patterns for testimonials.
templates/testimonials: Contains the HTML templates.
admin.py: Registers the Testimonial model with the admin site.
