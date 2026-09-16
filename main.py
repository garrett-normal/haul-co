#microblog.py

import sqlalchemy as sa
import sqlalchemy.orm as so
from flaskr import app, db
from flaskr.models import User, Ticket

from flaskr import app

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Ticket': Ticket}