import jwt
import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentView(APIView):
    """Handle payments"""
    # permission_classes = (IsAuthenticated, )

    def get(self, *args, **kwargs):
        """get the stripe publishable key"""
        publishable_key = settings.STRIPE_PUBLIC_KEY
        return Response(publishable_key, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """process payment"""
        amount = request.data['amount']
        payment_token = request.data['payment_token']

        if amount:
            amount = int(amount * 100)
            try:
                decoded = jwt.decode(
                    payment_token,
                    settings.SECRET_KEY,
                    algorithms=['HS256']

                )
                payment_intent_id = decoded.get('payment_intent_id')

                payment_intent = stripe.PaymentIntent.modify(
                        payment_intent_id,
                        amount=amount
                    )

                payload = {'client_secret': payment_intent.client_secret}
            except stripe.error.StripeError:
                error = {
                    'message': 'Error modifying payment intent'
                }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)

        else:
            try:
                payment_intent = stripe.PaymentIntent.create(
                    amount=2000,
                    currency="usd",
                    payment_method_types=["card"],
                    # automatic_payment_methods={"enabled": True},
                )

                # create token with payment intent
                token = jwt.encode(
                    {'payment_intent_id': payment_intent.id},
                    settings.SECRET_KEY,
                    algorithm='HS256'
                )

                payload = {
                    'client_secret': payment_intent.client_secret,
                    'payment_token': token
                }

            except stripe.error.StripeError:
                error = {
                    'message': 'Error creating payment intent'
                }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)

        return Response(payload, status=status.HTTP_200_OK)

        # return super().post(request, *args, **kwargs)
