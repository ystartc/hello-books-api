def test_get_all_books_for_empty_data(client):
    response = client.get('/books')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == []

def test_get_book_by_id(client, add_two_books):
    response = client.get('/books/1')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {'id': 1, 'title': 'Warriors', 'description': 'best team ever'}
    
def test_create_book(client):
    response = client.post('/books', json={'title': 'A Book', 'description': 'testing'})
    # response_body = response.get_data(as_text=True)
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {'msg': 'Book A Book created'}