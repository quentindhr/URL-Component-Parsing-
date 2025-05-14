from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


def test_health_check_url_parser():
    response = client.get("/health_url_parser")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status_url_parser": "ok"}


def test_parse_url_full_complex_url():
    full_url = (
        "https://user:password@www.example.co.uk:8080/path/to/resource.html"
        "?param1=value1&param2=value2&param1=anotherValue#section-3"
    )

    response = client.post("/parse_url", json={"url": full_url})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["original_url"] == full_url
    assert data["scheme"] == "https"
    assert data["netloc"] == "user:password@www.example.co.uk:8080"
    assert data["hostname"] == "www.example.co.uk"
    assert data["port"] == 8080
    assert data["path"] == "/path/to/resource.html"
    assert (
        data["query_string"]
        == "param1=value1&param2=value2&param1=anotherValue"
    )
    assert data["query_params"] == {
        "param1": ["value1", "anotherValue"],
        "param2": ["value2"]
    }
    assert data["fragment"] == "section-3"


def test_parse_url_simple_http_url_no_port_no_query_no_fragment():
    simple_url = "http://subdomain.example.com/somepath"
    response = client.post("/parse_url", json={"url": simple_url})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["scheme"] == "http"
    assert data["hostname"] == "subdomain.example.com"
    assert data["port"] is None
    assert data["path"] == "/somepath"
    assert data["query_string"] is None
    assert data["query_params"] is None
    assert data["fragment"] is None


def test_parse_url_with_only_query_no_path_no_fragment():
    url_query_only = "ftp://example.com?key=value"
    response = client.post("/parse_url", json={"url": url_query_only})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["scheme"] == "ftp"
    assert data["hostname"] == "example.com"
    assert data["path"] in ["", "/"]
    assert data["query_string"] == "key=value"
    assert data["query_params"] == {"key": ["value"]}
    assert data["fragment"] is None


def test_parse_url_invalid_url_format_handled_by_pydantic():
    response = client.post("/parse_url", json={"url": "this is not a url"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_parse_url_missing_url_payload():
    response = client.post("/parse_url", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_parse_mailto_url():
    url = "mailto:user@example.com"
    response = client.post("/parse_url", json={"url": url})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["scheme"] == "mailto"
    assert data["hostname"] is None
    assert data["path"] == "user@example.com"


def test_parse_ip_address_url():
    url = "http://192.168.1.1/"
    response = client.post("/parse_url", json={"url": url})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["scheme"] == "http"
    assert data["hostname"] == "192.168.1.1"
    assert data["port"] is None
    assert data["path"] == "/"
    assert data["query_params"] is None
    assert data["fragment"] is None
