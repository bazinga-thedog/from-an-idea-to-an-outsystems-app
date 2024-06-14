import requests
import pytest

url_path = 'https://[your_environment_host]/PadelPersonalCoach/rest/v1/'
headers = { 'x-api-key' : '[Your_API_KEY]'}

new_match = {"started_on":"2024-06-05T10:10:00Z","duration":120,"always_same_opponent":True,"always_same_partner":False,"match_type":"Tournament","location":2,"location_description":"Airfut"}

def pytest_namespace():
    return {'id' : None}

def test_call_get_match_by_id_without_apikey():
    url = url_path + 'matches/1'
    response = requests.get(url)

    assert response.status_code == 400

    data = response.json()

    assert data['Errors'][0] == "The 'x-api-key' HTTP Header is missing in the request."

def test_call_get_match_by_id_with_wrong_apikey():
    url = url_path + 'matches/1'
    response = requests.get(url, headers= {'x-api-key' : 'dummy'})

    assert response.status_code == 401

    data = response.json()

    assert data['Errors'][0] == "API call need to be authenticated with a correct API Key."
    

def test_call_get_match_by_id_with_wrong_id():
    url = url_path + 'matches/-1'
    response = requests.get(url, headers= headers)

    assert response.status_code == 404

    data = response.json()

    assert data['Errors'][0] == "Couldn't find the match for that id."

def test_create_new_match():

    url = url_path + 'matches'
    response = requests.post(url, json=new_match, headers= headers)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)

    assert all([new_match[k] == data[k] for k in data.keys() if k != "id"]) and data["id"] > 0

    pytest.id = data["id"]


def test_get_match_by_id():
    url = url_path + 'matches/' + str(pytest.id)
    response = requests.get(url, headers = headers)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)

    expected_match = new_match
    expected_match["id"] = pytest.id

    assert all([expected_match[k] == data[k] for k in data.keys()])

def test_delete_match_by_id():
    url = url_path + 'matches/' + str(pytest.id)
    response = requests.delete(url, headers = headers)

    assert response.status_code == 200



