from app import app, db
from app.models import Payments

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Payments': Payments}
