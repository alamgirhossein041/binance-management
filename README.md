# binance-management
Binance trading management

## Installing
Clone this repo
Install libs: `pip install -r requirements.txt`

## Running
Go to the root of the project
run: `uvicorn --app-dir=. app.main:app --reload`
it will be accessible from `127.0.0.1:8000`

You will need to have a Binance Testnet API key
create one here: https://testnet.binance.vision/

## Using

Docs can be found at: `http://127.0.0.1:8000/docs`

There are 4 api endpoints
- POST /users/create - Creates a user, needs email and name;
- GET /users/list - List all users, its wallets and balances and current USD balance;
- POST /wallets/create - Creates a new wallet, needs api_key, secret_key and owner_id
- GET /wallets/{id} - Show a single wallet (no balances in USD)

