# API Testing Framework

[![API Tests](https://github.com/bijin1830/api-testing-framework/actions/workflows/api-tests.yml/badge.svg)](https://github.com/bijin1830/api-testing-framework/actions/workflows/api-tests.yml)
![Postman](https://img.shields.io/badge/Postman-API%20Testing-FF6C37?logo=postman&logoColor=white)
![Newman](https://img.shields.io/badge/Newman-CLI%20Runner-6B4FBB)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?logo=githubactions&logoColor=white)

A practical REST API testing portfolio built with **Postman, Newman and GitHub Actions**.

The project demonstrates the type of validation used in real QA work: functional checks, negative scenarios, request/response validation, environment-driven execution, response-time checks and repeatable CI test runs.

> The repository uses only public demo APIs and synthetic data. It contains no employer, bank, merchant, cardholder, production or confidential information.

## Highlights

- GET, POST, PUT, PATCH and DELETE coverage
- Positive and negative API scenarios
- Status-code validation
- JSON field and data-type validation
- Header/content-type checks
- Query-parameter validation
- Environment variables for reusable execution
- Response-time threshold validation
- Newman command-line execution
- JUnit and HTML test reports
- GitHub Actions CI
- Payment-domain test design examples

## Test target

The executable collection uses the public JSONPlaceholder API:

```text
https://jsonplaceholder.typicode.com
```

JSONPlaceholder simulates writes rather than permanently storing them, which makes it suitable for a safe portfolio test suite.

## Project structure

```text
api-testing-framework/
├── .github/
│   └── workflows/
│       └── api-tests.yml
├── docs/
│   └── payment-api-test-scenarios.md
├── postman/
│   ├── JSONPlaceholder_API_Tests.postman_collection.json
│   └── Demo.postman_environment.json
├── package.json
├── .gitignore
└── README.md
```

## Covered executable scenarios

| Method | Scenario | Key validations |
|---|---|---|
| GET | Get single post | 200, JSON content type, ID, required fields, types, response time |
| GET | Filter by userId | 200, array response, non-empty result, filter correctness |
| POST | Create post | 201, echoed request data, generated ID |
| PUT | Replace post | 200, updated values, ID consistency |
| PATCH | Partial update | 200, patched field, ID consistency |
| DELETE | Delete post | 200, valid JSON response |
| GET | Missing resource | 404, response-time threshold |

## Environment variables

| Variable | Purpose |
|---|---|
| `base_url` | API endpoint |
| `post_id` | Valid resource ID |
| `user_id` | Query/body test value |
| `invalid_post_id` | Negative-test resource ID |
| `response_time_limit_ms` | Performance threshold |

## Run locally

Install dependencies:

```bash
npm install
```

Run CLI + JUnit reporting:

```bash
npm run test:api
```

Run CLI + HTML reporting:

```bash
npm run test:api:html
```

Reports are written under `reports/`.

## GitHub Actions

The workflow runs automatically for pushes and pull requests to `main`.

It:

1. Checks out the repository
2. Sets up Node.js 20
3. Installs dependencies
4. Executes the Newman suite
5. Generates JUnit and HTML reports
6. Uploads the reports as workflow artifacts

## Payment-domain test design

The executable suite intentionally stays on a public API. A separate synthetic scenario document demonstrates how I approach payment API testing, including:

- Sale approval and decline
- Duplicate transaction handling
- Timeout and reversal
- Refund
- Settlement
- Invalid amount/currency
- Idempotency
- Authentication/authorization
- Response-code mapping

See `docs/payment-api-test-scenarios.md`.

## QA skills represented

`Postman` · `Newman` · `REST API Testing` · `Functional Testing` · `Negative Testing` · `Integration Testing` · `Response Validation` · `Environment Variables` · `CI/CD` · `GitHub Actions` · `Payments QA`

## Author

**Bijin Benni**  
Software Test Engineer | Payments & POS Systems | API Testing

- Portfolio: https://bijin1830.github.io
- LinkedIn: https://www.linkedin.com/in/bijinbenni
- GitHub: https://github.com/bijin1830
