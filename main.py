from fastapi import FastAPI, Body, status
from pydantic import BaseModel, AnyUrl
from urllib.parse import urlparse, parse_qs, ParseResult

app = FastAPI()


# --- Pydantic Models ---
class URLParseRequest(BaseModel):
    url: AnyUrl


class URLParseResponse(BaseModel):
    original_url: str
    scheme: str | None = None
    netloc: str | None = None
    hostname: str | None = None
    port: int | None = None
    path: str | None = None
    query_string: str | None = None
    query_params: dict[str, list[str]] | None = None
    fragment: str | None = None


# --- Business Logic ---
def parse_url_components(url_to_parse: str) -> URLParseResponse:
    parsed_result: ParseResult = urlparse(url_to_parse)

    scheme = parsed_result.scheme
    netloc = parsed_result.netloc
    path = parsed_result.path
    raw_query_string = parsed_result.query
    fragment = parsed_result.fragment

    hostname_val = parsed_result.hostname
    port_val = parsed_result.port

    parsed_query_params = parse_qs(raw_query_string)
    parsed_query_params = (
        parsed_query_params if parsed_query_params else None
    )

    return URLParseResponse(
        original_url=url_to_parse,
        scheme=scheme,
        netloc=netloc,
        hostname=hostname_val,
        port=port_val,
        path=path,
        query_string=raw_query_string or None,
        query_params=parsed_query_params,
        fragment=fragment or None
    )


# --- API Endpoints ---
@app.post(
    "/parse_url",
    response_model=URLParseResponse,
    status_code=status.HTTP_200_OK
)
async def parse_url_endpoint(payload: URLParseRequest = Body(...)):
    parsed_data = parse_url_components(str(payload.url))
    return parsed_data


@app.get("/health_url_parser")
async def health_check_url_parser():
    return {"status_url_parser": "ok"}


# For running with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
