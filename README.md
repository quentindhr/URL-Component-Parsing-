# URL Component Parser API

## Description

(TO BE COMPLETED BY STUDENTS: Briefly describe the project - e.g., an API that takes a URL string as input and breaks it down into its constituent parts like scheme, hostname, port, path, query parameters, and fragment.)

## Prerequisites

(TO BE COMPLETED BY STUDENTS: List what is needed to run this project locally, e.g., Python 3.8+, pip.)

## Installation

1.  Clone this repository:
    ```bash
    # git clone <repository_url>
    # cd <repository_name>
    ```
2.  Create and activate a Python virtual environment:
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows (PowerShell/cmd):
    # venv\Scripts\activate
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the FastAPI application locally using Uvicorn:
```bash
uvicorn main:app --reload
```

The application will typically be available at http://127.0.0.1:8000. The interactive API documentation (Swagger UI) can be found at http://127.0.0.1:8000/docs.


## API Endpoints
(TO BE COMPLETED BY STUDENTS: Describe each API endpoint, its purpose, request body, and an example of the expected JSON response.)

* POST /parse_url
  * Description: (Students to describe: e.g., Parses the input URL into its components.)
  * Request Body: {"url": "https://www.example.com:8080/path?param=value#frag"}
  * Example Response (200 OK):
  ```json
    {
        "original_url": "https://www.example.com:8080/path?param=value#frag",
        "scheme": "https",
        "netloc": "www.example.com:8080",
        "hostname": "www.example.com",
        "port": 8080,
        "path": "/path",
        "query_string": "param=value",
        "query_params": {"param": ["value"]},
        "fragment": "frag"
    }
  ```

* GET /health_url_parser
  * Description: (Students to describe: Health check for this API.)
  * Response: {"status_url_parser": "ok"}

## Project Structure
(Optional: Students can briefly describe the main files if they wish)

* main.py: Contains the FastAPI application logic for the URL parser.
* requirements.txt: Lists the Python dependencies.
* tests/: Contains the automated tests.
* .gitlab-ci.yml: Defines the GitLab CI/CD pipeline.
* README.md: This file.
