# How to create an API signature

## What is an API signature?

An `API signature` is a digital signature generated from the data of your request and the secret key associated with your API account. It is used to verify that the request is authentic and has not been modified during transmission.

## How to create an API signature?

1. **Gather Request Data:**
:   
    - HTTP method (GET, POST, etc.)
    - API URL Path (e.g., `/api/users`)
    - Request expiration time (in seconds since the Unix Epoch)
    - Request body (if any)
2. **Concatenate the data into a single string.**
3. **Create the API signature** by using a hash algorithm (like SHA-256) and your API secret key to calculate the signature of the combined string.

## How to make the Request?

1. **Add the following headers:**
:   
    - `api-key`: Your API key provided by the API.
    - `api-signature`: The `API signature` you created.
    - `api-expires`: The expiration time of the request in seconds since the Unix Epoch.

2. **Send the Request**. Use your favorite HTTP library (like Axios in JavaScript) to send the request to the API server.

## Complete example in JavaScript (Node.js)

```ts
const axios = require('axios');
const crypto = require('crypto');

const apiKey = 'YourApiKey';
const apiSecret = 'YourApiSecret';
const path = '/auth/profile';
const method = 'GET';
const expires = Math.floor(Date.now() / 1000) + (10 * 60); // 10 minutes from now
const body = {};
const data = JSON.stringify(body);

const dataToSign = method + path + expires + data;
const signature = crypto.createHmac('sha256', apiSecret).update(dataToSign).digest('hex');

const headers = {
  'api-key': apiKey,
  'api-signature': signature,
  'api-expires': expires
};

const url = `https://{{ PAY_API_URL }}${path}`;

axios.get(url, { headers })
  .then(response => {
    console.log('API Response:', response.data);
  })
  .catch(error => {
    console.error('Request Error:', error.message);
  });
```
