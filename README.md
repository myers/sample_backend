# Myers Carpenter's CrowdStreet Backend Take Home Exercise

Implements a small API for interacting with a callback based third-party service.

## Setup

1. Clone repo
    ```
    git clone https://github.com/myers/crowdstreet_backend.git
    cd crowdstreet_backend
    ```
1. Install [pyenv].  On macOS with brew you can install via
    ```
    brew install pyenv
    ```
2. Install the version of python specified in `.python-version`
    ```
    pyenv install
    ```
3. Install [poetry] for package management
    ```
    pip install poetry
    ```
4. Install this app's dependencies
    ```
    poetry install
    ```

## Running tests

```
bin/manage test
```

## Running app

```
bin/manage migrate
bin/manage runserver
```

## Interact with CURL

```
$ curl -d '{"body": "cheese gromit!"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/request
8c5d4c8f-60d0-41fb-ad37-9cea38a03118
$ curl http://127.0.0.1:8000/status/8c5d4c8f-60d0-41fb-ad37-9cea38a03118
{"status": "", "body": "{\"body\": \"cheese gromit!\"}", "detail": ""}
$ curl -X POST -d 'STARTED' http://127.0.0.1:8000/callback/8c5d4c8f-60d0-41fb-ad37-9cea38a03118
$ curl -X PUT -d '{"status": "ERROR", "detail": "Not cheesy enough"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/callback/8c5d4c8f-60d0-41fb-ad37-9cea38a03118
$ curl http://127.0.0.1:8000/status/8c5d4c8f-60d0-41fb-ad37-9cea38a03118
{"status": "ERROR", "body": "{\"body\": \"cheese gromit!\"}", "detail": "Not cheesy enough"}
```


## Code Standards

- All code should be formatted with [black]


[brew]: (https://brew.sh/)
[pyenv]: (https://github.com/pyenv/pyenv)
[poetry]: (https://python-poetry.org/)
[black]: (https://github.com/psf/black)
