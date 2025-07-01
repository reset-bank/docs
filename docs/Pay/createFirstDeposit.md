# Create your first Deposit
## Prerequisites
- Have a **apiSignature** (refer to [How to create an apiSignature](apiSignature.md)).
- Have a **registered user** with an **active account** (refer to [Account Registration for API Usage](accountRegistration.md)).

---

### Create a Deposit (QR Code)

- Create it using the Swagger documentation: [🔗 Generate Deposit (Swagger)](https://api.pixease.reset-bank.com/api#/deposit/DepositController_create)[^1]

- When the customer completes the payment, a **confirmation webhook** will be sent to the registered URL (refer to [How to create a API key and use Webhook URLs](apiIntegration.md)).

---

## Important Information

- Refer to the input/output schemas at the end of the Swagger documentation in the `schemas` section.
- For integrations that **only generate deposits** (QR Code), it is **not necessary** to register a withdrawal webhook or API key.

### In case of webhook delivery failure:
:   
    - A retry will be attempted after **1.5 seconds**
    - Attempts will continue until delivery succeeds

[^1]: The accepted interface for this and other endpoints is listed at the bottom of the Swagger page, under the "schemas" section.