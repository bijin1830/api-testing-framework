# Payment API Test Scenarios

These scenarios are **synthetic portfolio examples**. They do not use real cardholder data, merchant credentials, bank endpoints or production information.

## Objective

Demonstrate structured API test design for payment-processing workflows while keeping the executable demo repository safe and vendor-neutral.

| ID | Scenario | Example expectation |
|---|---|---|
| PAY-001 | Successful sale | HTTP/API success; approved business response; transaction reference returned |
| PAY-002 | Declined sale | Decline response is handled without marking the transaction approved |
| PAY-003 | Invalid amount | Validation error for zero, negative or malformed amount |
| PAY-004 | Unsupported currency | Clear validation/business error |
| PAY-005 | Duplicate request | Duplicate/idempotent request does not create an unintended second charge |
| PAY-006 | Host timeout | Client receives deterministic timeout handling and transaction status remains traceable |
| PAY-007 | Reversal after uncertain result | Reversal references the original transaction and prevents double financial impact |
| PAY-008 | Full refund | Refund references an eligible original transaction and returns a new reference |
| PAY-009 | Refund above original amount | Request is rejected |
| PAY-010 | Invalid transaction reference | Request fails with a clear not-found/business response |
| PAY-011 | Missing authentication | 401/appropriate authentication failure |
| PAY-012 | Insufficient authorization | 403/appropriate authorization failure |
| PAY-013 | Malformed JSON | 400/validation failure with no transaction created |
| PAY-014 | Repeated settlement request | Duplicate settlement behavior is controlled and auditable |
| PAY-015 | Response-time threshold | Response remains within an agreed non-functional threshold |

## Example sale validations

For a successful synthetic sale response, validations could include:

- Transport-level status is correct.
- Business response code indicates approval.
- Transaction reference is present and non-empty.
- Amount and currency in the response match the request.
- Terminal/merchant identifiers, when applicable, map to the intended test configuration.
- Authorization data is present only when appropriate.
- No sensitive payment data is exposed in logs or response bodies.
- Response time is below the agreed threshold.

## Timeout and reversal test flow

1. Send a sale request using synthetic test data.
2. Simulate or mock an uncertain/timeout result.
3. Verify the transaction can be identified using its unique request reference.
4. Submit or observe the expected reversal flow.
5. Validate that the reversal points to the original transaction.
6. Confirm the final state does not represent two successful financial postings.
7. Verify logs contain traceable IDs but no prohibited sensitive values.

## Idempotency checks

Where an API supports an idempotency or unique request key:

1. Send a valid transaction request.
2. Repeat the identical request with the same key.
3. Verify the API does not unintentionally process a second independent transaction.
4. Confirm the response clearly indicates the original or duplicate state.
5. Repeat with a new key and verify normal processing behavior.

## Security-focused checks

- Missing token/API key
- Expired token
- Invalid signature
- Wrong merchant/terminal context
- Unexpected headers
- Oversized input
- Injection-like strings in non-financial text fields
- Sensitive-data leakage in response/error objects

## Evidence captured during execution

For a real QA cycle, evidence would normally include:

- Test case ID
- Environment
- Timestamp
- Sanitized request
- Sanitized response
- HTTP status
- Business response code
- Unique transaction/request reference
- Expected result
- Actual result
- Pass/fail
- Defect reference when applicable

Real production credentials, PANs, CVVs, access tokens and confidential bank data should never be committed to a public repository.
