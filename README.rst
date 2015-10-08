==============================================================================
A Django Hypermedia API with an AngularJS Frontend
==============================================================================

Technology Stack
----------------

Backend:

- Django (https://www.djangoproject.com)
- Django REST Framework (http://www.django-rest-framework.org)

REST API:

- JSON-LD (http://json-ld.org)
- Hydra (http://www.hydra-cg.com/spec/latest/core)
- JSON Schema (http://json-schema.org)

Frontend:

- Angular 1.4 (https://angularjs.org)
- Restangular (https://github.com/mgonto/restangular)
- Angular New Router (https://angular.github.io/router)
- Angular Schema Form (http://schemaform.io)


Requirements
------------

Fields/Widgets:

  - Text (Line, Textarea, RichText)
  - Numeric (Int, Bool, Float, Boolean)
  - Date and Time (Time, Date, DateTime)
  - Upload (File, Image)
  - Autocomplete (Fixed list, relation)

Validation:

  - Simple field validation
  - Form validation

Form:

  - Fieldsets
    -> attachment / image
  - Conditional fields (that show up dependent on another choice)
    -> first_time_application / first_time_application_reason
  - Subforms
  - External validation
  - Multi-form validation
  - Relational subforms (create another object within a form)

Customization:

  - Overriding single widgets


Setup Backend
-------------

Virtualenv::

  $ virtualenv .env
  $ source .env/bin/activate

Install Dependencies::

  $ pip install -r requirements/dev.txt

Create Database::

  $ python manage.py migrate

Create Superuser::

  $ echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

Or manually::

  $ python manage.py createsuperuser

Start Django::

  $ python manage.py runserver

JSON Request::

  $ http -a admin:admin GET http://127.0.0.1:8000/application/ Accept:application/json

Or::

  $ http -a admin:admin GET http://127.0.0.1:8000/application/?format=json

JSON LD Response::

  HTTP/1.0 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json; charset=utf-8
  Date: Fri, 18 Sep 2015 08:07:11 GMT
  Server: WSGIServer/0.1 Python/2.7.6
  Vary: Accept, Cookie
  X-Frame-Options: SAMEORIGIN

  {
      "@context": "http://www.w3.org/ns/hydra/context.jsonld",
      "@id": "http://127.0.0.1:8000/application/?format=json",
      "@type": "PagedCollection",
      "firstPage": null,
      "itemsPerPage": "10",
      "lastPage": null,
      "member": [],
      "nextPage": null,
      "operation": [
          {
              "@type": "CreateResourceOperation",
              "expects": "",
              "method": "POST",
              "returns": "",
              "title": "Creates a new user"
          },
          {
              "@type": "ReplaceResourceOperation",
              "method": "PUT",
              "title": "Updates an existing user"
          },
          {
              "@type": "DeleteResourceOperation",
              "method": "DELETE",
              "title": "Removes an existing user"
          }
      ],
      "previousPage": null,
      "totalItems": null
  }

JSON Schema Request::

 $ http -a admin:admin GET http://127.0.0.1:8000/application/ Accept:application/json_schema

or::

 $ http -a admin:admin GET http://127.0.0.1:8000/application/?format=json_schema

JSON Schema Response::

  HTTP/1.0 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/schema+json
  Date: Fri, 18 Sep 2015 08:08:00 GMT
  Server: WSGIServer/0.1 Python/2.7.6
  Vary: Accept, Cookie
  X-Frame-Options: SAMEORIGIN

  {
      "properties": {
          "age": {
              "description": "Your age",
              "key": "age",
              "title": "age",
              "type": "integer"
          },
          "attachment": {
              "description": "",
              "key": "attachment",
              "title": "attachment",
              "type": "string"
          },
          "date": {
              "description": "",
              "format": "datepicker",
              "key": "date",
              "title": "date",
              "type": "string"
          },
          "datetime": {
              "description": "",
              "format": "datetimepicker",
              "key": "datetime",
              "title": "datetime",
              "type": "string"
          },
          "description": {
              "description": "Description of the application",
              "key": "description",
              "title": "description",
              "type": "string"
          },
          "email": {
              "description": "Your email address",
              "key": "email",
              "title": "Email address",
              "type": "string"
          },
          "first_time_application": {
              "description": "",
              "key": "first_time_application",
              "title": "first_time_application",
              "type": "boolean"
          },
          "firstname": {
              "description": "",
              "key": "firstname",
              "title": "First name",
              "type": "string"
          },
          "gender": {
              "description": "",
              "key": "gender",
              "title": "gender",
              "type": "string"
          },
          "id": {
              "description": "",
              "key": "id",
              "title": "ID",
              "type": "integer"
          },
          "image": {
              "description": "",
              "key": "image",
              "title": "image",
              "type": "string"
          },
          "lastname": {
              "description": "",
              "key": "lastname",
              "title": "Last name",
              "type": "string"
          },
          "time": {
              "description": "",
              "format": "timepicker",
              "key": "time",
              "title": "time",
              "type": "string"
          },
          "title": {
              "description": "Title of the application",
              "key": "title",
              "title": "title",
              "type": "string"
          },
          "url": {
              "description": "",
              "key": "url",
              "title": "URL",
              "type": "string"
          },
          "uuid": {
              "description": "",
              "key": "uuid",
              "title": "UUID",
              "type": "string"
          }
      },
      "title": "Application(id, title, description, firstname, lastname, email, age, date, datetime, time, attachment, image, url, uuid, gender, first_time_application)",
      "type": "object"
  }


OPTIONS Request::

  $ http -a admin:admin OPTIONS http://localhost:8000/application/

OPTIONS Response::

  HTTP/1.0 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Date: Fri, 28 Aug 2015 13:22:42 GMT
  Server: WSGIServer/0.1 Python/2.7.10
  Vary: Accept, Cookie
  X-Frame-Options: SAMEORIGIN

  {
      "actions": {
          "POST": {
              "email": {
                  "label": "Email address",
                  "max_length": 254,
                  "read_only": false,
                  "required": false,
                  "type": "email"
              },
              "groups": {
                  "choices": [
                      {
                          "display_name": "mygroup",
                          "value": "http://localhost:8000/groups/1/"
                      }
                  ],
                  "help_text": "The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                  "label": "Groups",
                  "read_only": false,
                  "required": false,
                  "type": "field"
              },
              "operation": {
                  "label": "Operation",
                  "read_only": true,
                  "required": false,
                  "type": "field"
              },
              "url": {
                  "label": "Url",
                  "read_only": true,
                  "required": false,
                  "type": "field"
              },
              "username": {
                  "help_text": "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                  "label": "Username",
                  "max_length": 30,
                  "read_only": false,
                  "required": true,
                  "type": "string"
              }
          }
      },
      "description": "API endpoint that allows users to be viewed or edited.",
      "name": "User List",
      "parses": [
          "application/json",
          "application/x-www-form-urlencoded",
          "multipart/form-data"
      ],
      "renders": [
          "application/json",
          "text/html"
      ]
  }


Setup Frontend
--------------

Install dependencies::

  $ cd app
  $ npm install

Start Gulp dev server::

  $ gulp


SQL Migrations
--------------

Create migrations after each model change::

  $ python manage.py makemigrations

Apply migrations to you SQL db::

  $ python manage.py migrate


PyTest Django
-------------

Installation::

  $ pip install pytest-django

pytest.ini::

  [pytest]
  DJANGO_SETTINGS_MODULE=yourproject.settings

test_user.py::

  from django.contrib.auth.models import User

  import pytest


  @pytest.mark.django_db
  def test_my_user(admin_user):
      me = User.objects.get(username='admin')
      assert me.is_superuser
