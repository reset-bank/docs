# Create your first Withdrawal
## Prerequisites
- Have a **apiSignature** (refer to [How to create an apiSignature](apiSignature.md)).
- Have a **registered user** with an **active account** (refer to [Account Registration for API Usage](accountRegistration.md)) **and a API key and secret** (refer to [How to create a API key and use Webhook URLs](apiIntegration.md)).
- Have a **withdrawal webhook** (refer to [How to create a API key and use Webhook URLs](apiIntegration.md)).

---

### Request Payment (Pix Withdrawal)

- Create it using the Swagger documentation: [🔗 Request Payment (Swagger)](https://api.pixease.reset-bank.com/api#/withdrawal/WithdrawalController_create)[^1]
- Some endpoints require **authentication**, which can be done in two ways:
:   
    - Providing a **Bearer Token** (Obtain the token through [🔗 Login (Swagger)](https://api.pixease.reset-bank.com/api#/auth/AuthController_signIn)[^1].)
    - Using an **API key + signature**

---

## Important Information

- Refer to the input/output schemas at the end of the Swagger documentation in the `schemas` section.

### In case of webhook delivery failure:
:   
    - A retry will be attempted after **1.5 seconds**
    - Attempts will continue until delivery succeeds

[^1]: The accepted interface for this and other endpoints is listed at the bottom of the Swagger page, under the "schemas" section.