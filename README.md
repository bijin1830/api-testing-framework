# API Testing Showcase

[![API Tests](https://github.com/bijin1830/api-testing-framework/actions/workflows/api-tests.yml/badge.svg)](https://github.com/bijin1830/api-testing-framework/actions/workflows/api-tests.yml)
![Postman](https://img.shields.io/badge/Postman-API%20Testing-FF6C37?logo=postman&logoColor=white)
![Newman](https://img.shields.io/badge/Newman-CLI%20Runner-6B4FBB)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?logo=githubactions&logoColor=white)

A practical **REST API testing showcase using Postman and Newman**.

This project is designed to reflect my real hands-on QA experience more accurately: validating API responses, status codes, request/response data, positive and negative scenarios, environment variables and repeatable test execution.

> This repository uses only a public demo API and synthetic test data. It contains no employer, bank, merchant, card, production or confidential information.

## What this project demonstrates

- REST API functional testing
- Postman collections and environments
- HTTP status-code validation
- JSON response validation
- Header/content-type checks
- Positive and negative scenarios
- Query-parameter validation
- Basic response-time validation
- Running Postman tests using Newman
- GitHub Actions CI for repeatable execution
- Test-result artifact generation

## Test target

The collection uses the public [JSONPlaceholder](https://jsonplaceholder.typicode.com/) demo API.

Default base URL:

```text
https://jsonplaceholder.typicode.com
```

## Project structure

```text
api-testing-framework/
├── .github/
│   └── workflows/
│       └── api-tests.yml
├── postman/
│   ├── JSONPlaceholder_API_Tests.postman_collection.json
│   └── Demo.postman_environment.json
├── package.json
├── .gitignore
└── README.md
```

## Covered scenarios

| Scenario | Validation |
|---|---|
| Get single post | 200 status, JSON content type, expected id and required fields |
| Filter by userId | 200 status, non-empty response, all rows match the filter |
| Create post | 201 status, submitted title returned, response contains id |
| Missing post | 404 status and basic response-time check |

## Run in Postman

1. Import `postman/JSONPlaceholder_API_Tests.postman_collection.json`
2. Import `postman/Demo.postman_environment.json`
3. Select the **Demo** environment
4. Run the collection using Postman Collection Runner

## Run with Newman

Install dependencies:

```bash
npm install
```

Run the collection:

```bash
npm run test:api
```

The command runs the same Postman tests from the command line and writes a JUnit-style result file under `reports/`.

## GitHub Actions

The workflow automatically:

1. Checks out the repository
2. Sets up Node.js
3. Installs Newman
4. Runs the Postman collection
5. Uploads the test-result report as an artifact

This demonstrates how a manual/API tester can make repeatable API checks part of a CI workflow without presenting the project as advanced software-development experience.

## My experience level

My strongest API testing experience is with **Postman, REST validation, integration testing and production/UAT troubleshooting**.

I am also learning automation concepts. Python and Selenium are currently at a **beginner/basic level**, so this repository intentionally focuses on tools and workflows I can confidently explain in an interview.

## QA skills represented

`Postman` · `Newman` · `REST API Testing` · `Functional Testing` · `Negative Testing` · `Integration Testing` · `Response Validation` · `Environment Variables` · `GitHub Actions`

## Author

**Bijin Benni**  
Software Test Engineer | Payments & POS Systems | API Testing

- Portfolio: https://bijin1830.github.io
- LinkedIn: https://www.linkedin.com/in/bijinbenni
- GitHub: https://github.com/bijin1830
