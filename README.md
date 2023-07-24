# indices-trade-lab-backend

# My Serverless Web App

This is a serverless web app that allows users to perform forex trades. The backend is implemented using AWS Lambda, and the API is exposed using AWS API Gateway.

## Getting Started

These instructions will help you set up and deploy the serverless web app on AWS.

### Prerequisites

- An AWS account (if you don't have one, sign up at <https://aws.amazon.com/>)
- AWS CLI installed and configured with access to your AWS account (<https://aws.amazon.com/cli/>)
- Python 3.x installed on your local machine

### Backend Functionality

The backend functionality is implemented using Python and AWS Lambda. The backend functions handle user authentication, process trades, and fetch market data.

#### User Authentication

- User registration and login functionality are implemented using Flask and Flask-JWT-Extended.
- New users can register by sending a POST request to `/register` with `username` and `password` JSON parameters.
- Existing users can log in by sending a POST request to `/login` with their credentials, and a JWT token will be returned upon successful login.
- The protected route `/protected` requires a valid JWT token for access.

#### Processing Trades

- Trade processing functionality is exposed through a POST method on `/trade`.
- The frontend can send trade data as a JSON payload to `/trade` for processing.
- Implement the trade processing logic in the respective AWS Lambda function.

#### Fetching Market Data

- Market data can be fetched by sending a GET request to `/market_data` with the `currency_pair` query parameter (e.g., `/market_data?currency_pair=EURUSD`).
- The AWS Lambda function handling this request should interact with external APIs or services to fetch the market data.

### Setting Up API Gateway and Deploying Backend

1. Create an API Gateway using the AWS SDK for Python (Boto3) or the AWS Management Console.
2. Set up resources, methods, and integrations to link API Gateway endpoints with the respective AWS Lambda functions.
3. Deploy the API to make it publicly accessible.

### Frontend Implementation

- The frontend of the web app can be built using HTML, CSS, and JavaScript.
- Use JavaScript's `fetch` API to send HTTP requests to the API Gateway endpoints for trade processing and market data retrieval.
- Host the frontend as static content using AWS S3 or other serverless content hosting services.

## Testing

- Test the serverless web app by deploying the frontend and backend.
- Make sure the frontend communicates with the API Gateway endpoints correctly.
- Verify that the backend functions handle user authentication, process trades, and fetch market data as expected.
