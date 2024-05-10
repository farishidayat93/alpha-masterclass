from app.modules import db


class Clients(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    referral_email = db.Column(db.String(200))
    points = db.Column(db.Integer, default=0)

    def __init__(self, name, email, referral_email, points):
        self.name = name
        self.email = email
        self.referral_email = referral_email
        self.points = points
