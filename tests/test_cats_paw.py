from cats_paw import app

def test_homepage_get():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Cat's Paw" in response.data

def test_empty_search_input():
    client = app.test_client()
    response = client.post('/', data={'search': ''})
    assert response.status_code == 400