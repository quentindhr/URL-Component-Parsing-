# URL Component Parser API

## Description

Cette application est une API qui prend une URL en entrée et la décompose en ses différents composants tels que le schéma, le nom d'hôte, le port, le chemin, les paramètres de requête et le fragment.

## Prerequisites

Pour exécuter ce projet localement, vous aurez besoin de :
- Python 3.8 ou supérieur
- pip

## Installation

1. Clonez ce dépôt :
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2. Créez et activez un environnement virtuel Python :
    ```bash
    python -m venv venv
    # Sur macOS/Linux :
    source venv/bin/activate
    # Sur Windows (PowerShell/cmd) :
    venv\Scripts\activate
    ```
3. Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Pour exécuter l'application FastAPI localement avec Uvicorn :
```bash
uvicorn main\:app --reload

L'application sera généralement disponible à l'adresse http://127.0.0.1:8000. La documentation interactive de l'API (Swagger UI) peut être trouvée à l'adresse http://127.0.0.1:8000/docs.

API Endpoints

POST /parse_url

Description : Analyse l'URL d'entrée en ses composants.
Request Body : {"url": "https://www.example.com:8080/path?param=value#frag"}
Exemple de réponse (200 OK) :
Copier
{
      "original_url": "https://www.example.com:8080/path?param=value#frag",
      "scheme": "https",
      "netloc": "www.example.com:8080",
      "hostname": "www.example.com",
      "port": 8080,
      "path": "/path",
      "query_string": "param=value",
      "query_params": {"param": ["value"]},
      "fragment": "frag"}
GET /health_url_parser

Description : Vérification de l'état de santé de cette API.
Réponse : {"status_url_parser": "ok"}
Project Structure

main.py : Contient la logique de l'application FastAPI pour l'analyseur d'URL.
requirements.txt : Liste les dépendances Python.
tests/ : Contient les tests automatisés.
.gitlab-ci.yml : Définit le pipeline CI/CD GitLab.
README.md : Ce fichier.