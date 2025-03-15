# Portfolio_TW

myproject/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py  # This is important for production deployments
│   ├── asgi.py  # Optional if you want to use ASGI for async
│
├── apps/  # Your custom apps (e.g. users, blog, etc.)
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│
├── requirements.txt  # All your dependencies
└── static/  # Static files (will be served by a web server)
└── templates/  # Templates (if any)
