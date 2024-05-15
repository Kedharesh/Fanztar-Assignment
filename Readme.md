# Mobile Factory API

This API allows you to create an order for a mobile phone by providing a list of component codes. The API calculates the total price of the ordered components and returns the order details.

## Input Format
Send a POST request to `/orders` with the following JSON payload:
```json
{
    "components": ["I", "A", "D", "F", "K"]
}
```
Components: A list of component codes representing the Screen, Camera, Port, OS, and Body of the mobile phone.
How to Run
Clone the repository:

git clone https://github.com/your-repo/mobile-factory-api.git
cd mobile-factory-api
Install dependencies:

pip install -r requirements.txt
Start the server:

python main.py
Send a POST request to http://localhost:8000/orders using tools like Postman with the input format mentioned above.

Unit Tests
To run the unit tests:

python test.py
API Response
If the order is valid, the API will respond with a status code of 201 and the order details in JSON format.
If the order is invalid, the API will respond with a status code of 400 and an error message.
