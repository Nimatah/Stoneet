# Madan

[![Build Status](https://phbuild.planhub.ir/api/badges/PlanHUB/madan/status.svg)](https://phbuild.planhub.ir/PlanHUB/madan)

## Development

### Windows
if it's your first time configuring the project, you'll need the following tools:

- git
- python3.8


go to your desired directory and open up git bash (right click on screen)

run ```git clone https://git.planhub.ir/PlanHUB/madan.git```

provide credentials and wait for download to finish.

once done, go to the project directory and open up a powershell window (shift + right click on screen)

run the following commands in order

```pip install -r requirements.txt```

```python manage.py migrate```

```python manage.py collectstatic```

```python manage.py runserver```

server is now configured and is running on http://localhost:8000

this concludes first time configuration.

---

to continue using the service you need only to run:

```python manage.py runserver```

on a powershell window in your project directory.


### Linux
If you're using Linux, you know what you're doing. nothing to see here, move along.

---
if you have any questions, contact @tajious