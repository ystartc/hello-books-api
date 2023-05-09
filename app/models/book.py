from app import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('Author', back_populates='books')
    
    def to_string(self):
        return f'{self.id}: {self.title}. Description: {self.description}.'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'author_id': self.author_id
            }
       
    @classmethod 
    def from_dict(cls, request_body):
        book = cls(
                title=request_body["title"],
                description=request_body['description'],
                author_id=request_body['author_id']
                )
        return book