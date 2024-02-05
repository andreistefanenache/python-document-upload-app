import pytest
import os, io
from main import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client

def test_upload_file_missing_file(client):
    response = client.post('/')
    assert response.status_code == 422
    assert response.data == b'File missing'

def test_upload_file_missing_filename(client):
    response = client.post('/', data={'file': (io.BytesIO(b''), '')})
    assert response.status_code == 422
    assert response.data == b'Filename missing'

def test_upload_file_allowed_file(client):
    response = client.post('/', data={'file': (io.BytesIO(b'some content'), 'test.txt')})
    
    assert response.status_code == 200
    assert response.data == b'Uploaded!'

def test_upload_file_increases_file_count(client):
    initial_file_count = get_file_count_in_cwd()

    response = client.post('/', data={'file': (io.BytesIO(b'some content'), 'test.txt')})
    
    assert response.status_code == 200
    assert response.data == b'Uploaded!'
    
    updated_file_count = get_file_count_in_cwd()

    assert updated_file_count == initial_file_count + 1
    

def get_file_count_in_cwd():
    files_in_cwd = [f for f in os.listdir(os.getcwd())]
    return len(files_in_cwd)

if __name__ == "__main__":
    pytest.main()
