from app import db 

class Payments(db.Model):
    __tableneame__='Payments'
    id = db.Column("id", db.Integer, primary_key=True)
    value = db.Column(db.Float)
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Payment {}>'.format(self.id)

        