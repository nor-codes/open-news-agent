# Crawler Service

Crawler Service is part of the **Open News Agent** platform.  
It is responsible for crawling news sources, extracting article data, and exposing endpoints to trigger or monitor crawling operations.

The service is built using **FastAPI** and uses **Pipenv** for dependency management and virtual environments.

---

## Tech Stack

- Python 3.10+
- Pip

## Prerequisites

- Python 3.10+
- Pip installed

Install Pipenv:

```bash
pip install pipenv
```

Install dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```


## Running the Service

Start the FastAPI server using Uvicorn:

```bash
pipenv run uvicorn app.main:app --reload
```