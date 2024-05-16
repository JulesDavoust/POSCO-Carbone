from Database.init_database import db

class plateforms(db.Model):
    namePlateform = db.Column(db.String(50), primary_key=True)

    def __repr__(self):
        return f'{self.namePlateform}'
