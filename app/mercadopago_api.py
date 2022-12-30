import mercadopago
import json
import os

CLIENT_TOKEN = os.getenv('MERCADO_PAGO_KEY')

sdk = mercadopago.SDK(CLIENT_TOKEN)

def mp_payment(req, **kwargs):
    product = kwargs['product']
    preference_data = {
        "items": [
            {
                "title": "Product",
                "quantity": 1,
                "unit_price": product.value
            }
        ],
        "back_urls": {
          "success": "http://127.0.0.1:5000/success/" + product.id,
          "failure": "http://127.0.0.1:5000/failure/" + product.id
        },
        "auto_return": "approved",
        "binary_mode": True
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    
    return preference['init_point']