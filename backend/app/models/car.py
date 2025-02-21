from . import db


class Car(db.Model):
    __tablename__ = 'cars'

    car_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    vin = db.Column(db.String(17), nullable=False, unique=True)

    user = db.relationship('User', backref=db.backref('cars', lazy=True)) 

    def __repr__(self):
        return f"<Car {self.name} {self.model} ({self.year})>"

    def to_dict(self):
        return {
            'car_id': self.car_id,
            'user_id': self.user_id,
            'name': self.name,
            'model': self.model,
            'year': self.year,
            'vin': self.vin
        }
