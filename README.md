this is repository for 2go.nyc and I will work on this

activate venv on windows local
.\virt\Scripts\activate

debug mone on on windows
$env:FLASK_ENV = "development"


$env:FLASK_APP="application.py"

>>> from app.models import User
>>> u = User(username='susan', email='susan@example.com')