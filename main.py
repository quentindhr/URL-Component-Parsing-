from fastapi import FastAPI, Body, status, HTTPException
from pydantic import BaseModel, HttpUrl, Field
from urllib.parse import urlparse, parse_qs, ParseResult

app = FastAPI()

# --- Pydantic Models ---
class URLParseRequest(BaseModel):
    url: HttpUrl # Pydantic validates basic URL structure

class URLParseResponse(BaseModel):
    original_url: str
    scheme: str | None = None
    netloc: str | None = None
    hostname: str | None = None
    port: int | None = None
    path: str | None = None
    query_string: str | None = None # The raw query string
    query_params: dict[str, list[str]] | None = None # Parsed query parameters
    fragment: str | None = None


# --- Business Logic ---
def parse_url_components(url_to_parse: str) -> URLParseResponse:
    """
    Parses a given URL string into its components.
    STUDENTS TO COMPLETE THIS FUNCTION.
    """
    # TODO 1: Use `urllib.parse.urlparse()` on the `url_to_parse` string.
    #          This will return a `ParseResult` object (typically a named tuple).
    #          Store this result in a variable (e.g., `parsed_result`).
    # Example: parsed_result: ParseResult = urlparse(url_to_parse)
    parsed_result: ParseResult = None # Placeholder for students to implement

    # TODO 2: Extract individual components from `parsed_result`.
    #          - scheme (e.g., `parsed_result.scheme`)
    #          - netloc (e.g., `parsed_result.netloc`)
    #          - path (e.g., `parsed_result.path`)
    #          - query (this is the raw query string, e.g., `parsed_result.query`)
    #          - fragment (e.g., `parsed_result.fragment`)
    
    # Placeholder assignments
    scheme = None
    netloc = None
    path = None
    raw_query_string = None
    fragment = None
    
    # TODO 3: Extract hostname and port from the `netloc`.
    #          The `parsed_result` object (from `urlparse`) has `.hostname` and `.port` attributes
    #          that are convenient for this. They can be `None`.
    #          Store them in `hostname_val` and `port_val`.
    hostname_val = None
    port_val = None


    # TODO 4: Parse the `raw_query_string` into a dictionary of query parameters.
    #          Use `urllib.parse.parse_qs(raw_query_string)`.
    #          This function returns a dictionary where keys are parameter names
    #          and values are lists of strings (as a parameter can appear multiple times).
    #          Store this in `parsed_query_params`. If `raw_query_string` is empty,
    #          `parse_qs` will return an empty dictionary, which is fine.
    parsed_query_params = {}


    return URLParseResponse(
        original_url=url_to_parse,
        scheme=scheme, # TODO: Replace with extracted value
        netloc=netloc, # TODO: Replace with extracted value
        hostname=hostname_val, # TODO: Replace with extracted value
        port=port_val, # TODO: Replace with extracted value
        path=path, # TODO: Replace with extracted value
        query_string=raw_query_string if raw_query_string else None, # TODO: Replace with extracted value
        query_params=parsed_query_params if parsed_query_params else None, # TODO: Replace with extracted value
        fragment=fragment if fragment else None # TODO: Replace with extracted value
    )

# --- API Endpoints ---
@app.post("/parse_url", response_model=URLParseResponse, status_code=status.HTTP_200_OK)
async def parse_url_endpoint(payload: URLParseRequest = Body(...)):
    # TODO: Call `parse_url_components` with `str(payload.url)` 
    #       (Pydantic's HttpUrl needs to be converted to string for urlparse).
    #       Return the result.
    
    # Placeholder - students to implement the call
    parsed_data = parse_url_components(str(payload.url))
    return parsed_data

@app.get("/health_url_parser")
async def health_check_url_parser():
    return {"status_url_parser": "ok"}

# For running with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)