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
bin/manage runserver
```

TODO: give some curl examples here of interacting with the API

[brew]: (https://brew.sh/)
[pyenv]: (https://github.com/pyenv/pyenv)
[poetry]: (https://python-poetry.org/)
