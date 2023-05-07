from app import db

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    
    def to_dict(self):
        return {
                'id': self.id,
                'name': self.name
                }
    
