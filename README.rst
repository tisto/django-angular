==============================================================================
Django + Django Rest Framework + Angular 1.4 + Restangular
==============================================================================

Virtualenv::

  $ virtualenv .env
  $ source .env/bin/activate

Install Dependencies::

  $ pip install -r requirements.txt


Tutorial::

  http://www.django-rest-framework.org/tutorial/quickstart/

Create Superuser::

  $ python manage.py createsuperuser

Start Django::

  $ python manage.py runserver

Try request::

  $ http -a admin:admin http://127.0.0.1:8000/users/

Response::

  HTTP/1.0 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Date: Fri, 14 Aug 2015 10:18:57 GMT
  Server: WSGIServer/0.1 Python/2.7.6
  Vary: Accept, Cookie
  X-Frame-Options: SAMEORIGIN

  {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
          {
              "email": "",
              "groups": [],
              "url": "http://127.0.0.1:8000/users/1/",
              "username": "admin"
          }
      ]
  }


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
