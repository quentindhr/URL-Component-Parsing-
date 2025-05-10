from fastapi.testclient import TestClient
from fastapi import status
from main import app # Assuming main.py is in the parent directory

client = TestClient(app)

def test_health_check_url_parser():
    response = client.get("/health_url_parser")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status_url_parser": "ok"}

def test_parse_url_full_complex_url():
    full_url = "https://user:password@www.example.co.uk:8080/path/to/resource.html?param1=value1&param2=value2&param1=anotherValue#section-3"
    
    response = client.post("/parse_url", json={"url": full_url})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    assert data["original_url"] == full_url
    # TODO: Assert `data["scheme"]` is "https".
    # TODO: Assert `data["netloc"]` is "user:password@www.example.co.uk:8080".
    # TODO: Assert `data["hostname"]` is "www.example.co.uk".
    # TODO: Assert `data["port"]` is 8080.
    # TODO: Assert `data["path"]` is "/path/to/resource.html".
    # TODO: Assert `data["query_string"]` is "param1=value1&param2=value2&param1=anotherValue".
    # TODO: Assert `data["query_params"]` is {"param1": ["value1", "anotherValue"], "param2": ["value2"]}.
    # TODO: Assert `data["fragment"]` is "section-3".
    # Example for one assertion:
    # assert data["scheme"] == "https"
    pass # Remove when assertions are added

def test_parse_url_simple_http_url_no_port_no_query_no_fragment():
    simple_url = "http://subdomain.example.com/somepath"
    response = client.post("/parse_url", json={"url": simple_url})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # TODO: Complete assertions for this simpler URL.
    #       `port` should be None.
    #       `query_string` and `query_params` should be None or empty.
    #       `fragment` should be None or empty.
    # Example:
    # assert data["scheme"] == "http"
    # assert data["hostname"] == "subdomain.example.com"
    # assert data["port"] is None
    # assert data["path"] == "/somepath"
    # assert data["query_params"] is None 
    pass # Remove when assertions are added

def test_parse_url_with_only_query_no_path_no_fragment():
    url_query_only = "ftp://example.com?key=value"
    response = client.post("/parse_url", json={"url": url_query_only})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # TODO: Complete assertions. Path might be empty string "" or "/".
    #       `query_params` should be {"key": ["value"]}.
    # Example:
    # assert data["scheme"] == "ftp"
    # assert data["hostname"] == "example.com"
    # assert data["path"] in ["", "/"] # urlparse behavior can vary slightly with no path
    # assert data["query_params"] == {"key": ["value"]}
    pass # Remove when assertions are added

def test_parse_url_invalid_url_format_handled_by_pydantic():
    # Pydantic's HttpUrl should catch fundamentally invalid URLs before they reach our logic.
    response = client.post("/parse_url", json={"url": "this is not a url"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_parse_url_missing_url_payload():
    response = client.post("/parse_url", json={}) # Missing "url"
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

# TODO: (Optional Bonus) Add a test for a URL like "mailto:user@example.com".
# TODO: (Optional Bonus) Add a test for an IP address URL "http://192.168.1.1/".