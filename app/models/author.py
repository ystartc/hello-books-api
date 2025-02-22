from app import db

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', back_populates='author')
    
    def to_dict(self):
        return {
                'id': self.id,
                'name': self.name
                }
        
    @classmethod
    def from_dict(cls, request_body):
        author = cls(
                    name=request_body['name']
                    )
        return author
