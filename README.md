# API Testing Framework

[![API Tests](https://github.com/bijin1830/api-testing-framework/actions/workflows/api-tests.yml/badge.svg)](https://github.com/bijin1830/api-testing-framework/actions/workflows/api-tests.yml)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automation-0A9EDC?logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-20232A)
![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Validation-000000)

A portfolio-grade **REST API automation framework** built with Python, `pytest`, `requests`, and JSON Schema validation.

The project demonstrates reusable API-client design, positive and negative testing, contract/schema validation, environment configuration, parametrized tests, CI execution, and HTML reporting.

> This repository uses only public demo APIs and synthetic test data. It contains no employer, bank, merchant, customer, card, production, or confidential information.

## What this project demonstrates

- REST API functional testing
- HTTP status-code validation
- JSON response/body validation
- JSON Schema contract testing
- Header and content-type validation
- Positive and negative scenarios
- Query-parameter validation
- Parametrized test execution
- Reusable request client
- Environment-based configuration
- `pytest` markers for smoke / regression / negative tests
- Automatic HTML report generation
- GitHub Actions CI on every push and pull request

## Test target

The framework uses the public [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API as a safe demo service.

Default base URL:

```text
https://jsonplaceholder.typicode.com
```

You can override it with the `BASE_URL` environment variable.

## Project structure

```text
api-testing-framework/
├── .github/
│   └── workflows/
│       └── api-tests.yml
├── src/
│   ├── __init__.py
│   ├── api_client.py
│   └── schemas.py
├── tests/
│   ├── conftest.py
│   ├── test_posts.py
│   ├── test_users.py
│   └── test_negative.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/bijin1830/api-testing-framework.git
cd api-testing-framework
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the tests

Run the full suite:

```bash
pytest
```

Run smoke tests:

```bash
pytest -m smoke
```

Run negative tests:

```bash
pytest -m negative
```

Generate an HTML report:

```bash
pytest --html=reports/api-test-report.html --self-contained-html
```

## Example coverage

| Area | Example validation |
|---|---|
| GET collection | `GET /posts` returns a non-empty list |
| GET single resource | `GET /posts/1` returns the expected resource |
| Filtering | `GET /posts?userId=1` returns only matching records |
| Create | `POST /posts` returns `201` and echoes submitted data |
| Contract | Post/User responses match JSON Schema |
| Headers | JSON content type is returned |
| Negative | Missing resources return `404` |
| Data quality | Required fields are present and correctly typed |

## Design approach

The tests do not call `requests` directly everywhere. HTTP behavior is wrapped by `ApiClient`, keeping request logic reusable and test code readable.

```python
response = api_client.get("/posts/1")
assert response.status_code == 200
```

Schema definitions are also centralized so contract checks can be reused across many tests.

## CI/CD

GitHub Actions automatically:

1. Checks out the repository
2. Installs Python
3. Installs dependencies
4. Runs the full API test suite
5. Generates an HTML test report
6. Uploads the report as a workflow artifact

This makes test results visible directly from the **Actions** tab of the repository.

## QA skills represented

`API Testing` · `REST` · `Python` · `Pytest` · `Requests` · `JSON Schema` · `Functional Testing` · `Negative Testing` · `Regression Testing` · `Test Automation` · `CI/CD` · `GitHub Actions`

## Author

**Bijin Benni**  
Software Test Engineer | QA Automation | Payments & POS Systems

- Portfolio: https://bijin1830.github.io
- LinkedIn: https://www.linkedin.com/in/bijinbenni
- GitHub: https://github.com/bijin1830
