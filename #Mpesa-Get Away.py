#Mpesa-Get Away
#Request

Headers
Key: Authorization
Value: Basic cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==
​
Body
  {
    "ShortCode": 600999,
    "ResponseType": "Completed",
    "ConfirmationURL": "https://mydomain.com/confirmation",
    "ValidationURL": "https://mydomain.com/validation"
  }


#response

{
  "ConversationID": "AG_20230729_20100fd44455fa0d1c54",
  "OriginatorConversationID": "20012-198316789-1",
  "ResponseCode": "0",
  "ResponseDescription": "Accept the service request successfully."
}
