from app import db 

class Products(db.Model):
    __tableneame__='Products'
    id = db.Column("id", db.Integer, primary_key=True)
    value = db.Column(db.Float)
    status = db.Column(db.String(12), default='in progress')

    def __repr__(self):
        return '<Payment {}>'.format(self.id)

        