from . import db


class Service(db.Model):
    __tablename__ = 'services'

    service_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.car_id'), nullable=False)
    mileage = db.Column(db.Integer, nullable=True)
    service_type = db.Column(db.Text, nullable=True)
    service_date = db.Column(db.Date, nullable=True)
    next_service_date = db.Column(db.Date, nullable=True)
    cost = db.Column(db.Numeric(10, 2), nullable=True)
    notes = db.Column(db.Text, nullable=True)

    car = db.relationship('Car', backref=db.backref('services', lazy=True)) 

    def __repr__(self):
        return f"<Service {self.service_type} for Car {self.car_id} on {self.service_date}>"

    def to_dict(self):
        return {
            'service_id': self.service_id,
            'car_id': self.car_id,
            'mileage': self.mileage,
            'service_type': self.service_type,
            'service_date': self.service_date,
            'next_service_date': self.next_service_date,
            'cost': self.cost,
            'notes': self.notes
        }
