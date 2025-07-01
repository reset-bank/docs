# How to create a API key and use Webhook URLs
## Prerequisites
- Have a **registered user** with an **active account** (refer to [Account Registration for API Usage](accountRegistration.md)).

---

## API and Webhook integration

1. Go to the **Integrations** menu and click `Register (Cadastrar)`.
:   
    ![][image1]
    ![][image2]
2. In the form, provide:
: 
    1. Name and ID (for reference only) 
    2. Type: `webhook for deposits`, `webhook for withdrawals`, or `API key`
    3. Webhook URL (if it is a webhook)
    4. Enable/Disable the integration
    ![][image4]

---

**Notes:**

- After registration, the **api-secret** will be displayed. **Copy and store it securely**, as **it will not be shown again**.

### About the api-secret
- The `api-secret` is used to **validate webhook messages** via a **unique signature**.
- To learn more about signing authenticated requests, see [How to create an apiSignature](apiSignature.md)

[image1]: /docs/images/Pay/configs-user-integration/1-menu-integracao.png
[image2]: /docs/images/Pay/configs-user-integration/2-integracao-cadastrar.png
[image3]: /docs/images/Pay/configs-user-integration/3-tipo-integracao.png
[image4]: /docs/images/Pay/configs-user-integration/4-cadastrar-chave-integracao.png
