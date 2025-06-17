# How to integrate our API
## Prerequisites
- Have a **registered user** with an **active account**.

---

## Account Registration for API Usage

1. Log in to the platform with your **username** and **password**.
2. Navigate to the **Accounts** menu and click the `Register` button.
3. In the registration form:
   - Provide a **reference name** f or the account.
   - Provide a **valid Pix key** (from another institution).
   - This Pix key will be used for **account validation**.

After registration, the user will have access to the **account identifier**, which will be used in requests for:

- Generating charges (QR Code)
- Pix payments

---

## User Integration Settings

### Webhook Registration

1. Go to the **Integrations** menu and click `Register`.
2. In the form, provide:
   - Type: `webhook for deposits`, `webhook for withdrawals`, or `API key`
   - Enable/Disable the integration
   - Name and ID (for reference only)

**Notes:**
- For integrations that **only generate charges** (QR Code), it is **not necessary** to register a withdrawal webhook or API key.
- After registration, the **api-secret** will be displayed.
**Copy and store it securely**, as **it will not be shown again**.

### About the api-secret
- The `api-secret` is used to **validate webhook messages** via a **unique signature**.
- For integrations with **withdrawals via API**, it is mandatory to:
  - Register the **withdrawal webhook URL**
  - Create an **API key**
- Refer to: [How to generate the signature](https://api.pixease.reset-bank.com/how-to-sign)

---

## API Integration

### Generate Charge QR Code

- Test it using the Swagger documentation:
  [🔗 Generate Charge (Swagger)](https://api.pixease.reset-bank.com/api#/deposit/DepositController_create)

- When the customer completes the payment, a **confirmation webhook** will be sent to the registered URL.

---

### Request Payment (Pix Withdrawal)

- Test it using the Swagger documentation:
  [🔗 Request Payment (Swagger)](https://api.pixease.reset-bank.com/api#/withdrawal/WithdrawalController_create)

- Some endpoints require **authentication**, which can be done in two ways:
  - Providing a **Bearer Token**
  - Using an **API key + signature**

Obtain the token through login:
[🔗 Login (Swagger)](https://api.pixease.reset-bank.com/api#/auth/AuthController_signIn)

Refer to the input/output schemas at the end of the Swagger documentation in the `schemas` section.
For this case, see the schema: `CreateWithdrawalDto`.

---

## Important Information

- In case of webhook delivery failure:
  - A retry will be attempted after **1.5 seconds**
  - Attempts will continue until delivery succeeds

### How the signature (api-signature) is generated

```js
const content = JSON.stringify(data);
const signature = crypto
  .createHmac('sha256', user.api_secret)
  .update(content)
  .digest('hex');
```

- The signature must be sent in the **header** `api-signature`
