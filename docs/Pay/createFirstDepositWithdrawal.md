# Create your first Deposit and Withdrawal
## Prerequisites
- Have a **apiSignature** (refer to [How to create an apiSignature](apiSignature.md)).
- Have a **registered user** with an **active account** (refer to [Account Registration for API Usage](accountRegistration.md)) or a **API key and secret** (refer to [How to create a API key and use Webhook URLs](apiIntegration.md)).

---

### Create a Deposit (QR Code)

- Create it using the Swagger documentation: [🔗 Generate Charge (Swagger)](https://api.pixease.reset-bank.com/api#/deposit/DepositController_create)[^1]

- When the customer completes the payment, a **confirmation webhook** will be sent to the registered URL.

---

### Request Payment (Pix Withdrawal)

- Create it using the Swagger documentation: [🔗 Request Payment (Swagger)](https://api.pixease.reset-bank.com/api#/withdrawal/WithdrawalController_create)[^1]
- Some endpoints require **authentication**, which can be done in two ways:
:   
    - Providing a **Bearer Token**
    - Using an **API key + signature**

Obtain the token through [🔗 Login (Swagger)](https://api.pixease.reset-bank.com/api#/auth/AuthController_signIn)[^1].

Refer to the input/output schemas at the end of the Swagger documentation in the `schemas` section.

---

## Important Information

### In case of webhook delivery failure:
:   
    - A retry will be attempted after **1.5 seconds**
    - Attempts will continue until delivery succeeds

[^1]: The accepted interface for this and other endpoints is listed at the bottom of the Swagger page, under the "schemas" section.