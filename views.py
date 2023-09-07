from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

@api_view(["POST"])
@permission_classes([AllowAny])  # Allow anyone to register
def register(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        name = request.data.get("name")

        if email and password and name:
            user, created = CustomUser.objects.get_or_create(email=email, name=name)
            user.set_password(password)
            user.save()
            
            token, _ = Token.objects.get_or_create(user=user)  # Create a token for the user
            
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "Email, password, and name are required fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    if email and password and name:
        user, created = CustomUser.objects.get_or_create(email=email, name=name)
        user.set_password(password)
        user.save()
        
        # Create a wallet for the user
        Wallet.objects.get_or_create(user=user)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)
    else:
        return Response(
            {"error": "Email, password, and name are required fields."},
            status=status.HTTP_400_BAD_REQUEST,
        )

@api_view(["POST"])
@permission_classes([AllowAny])  # Allow anyone to log in
def login_view(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                token, _ = Token.objects.get_or_create(user=user)  # Get or create a token
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Invalid credentials."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"error": "Email and password are required fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def initiate_deposit(request):
    # Get the user making the deposit
    user = request.user
    
    # Get the deposit amount from the request data
    deposit_amount = request.data.get("amount")
    
    # Perform validation on the deposit amount and other input data
    if not deposit_amount:
        return Response({"error": "Deposit amount is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    if mpesa_response.get("success"):
        # Process the successful deposit and update the user's wallet balance
        user.wallet.balance += deposit_amount
        user.wallet.save()
        return Response({"message": "Deposit successful."}, status=status.HTTP_200_OK)
    else:
        # Handle the case of a failed deposit
        return Response({"error": "Deposit failed."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Here, you would integrate with the M-Pesa API using your API keys and credentials
    # Make an HTTP request to the M-Pesa API to initiate the deposit
    # You'll need to construct the request data according to the M-Pesa API documentation
    # For example:
    mpesa_response = make_mpesa_deposit_request(user, deposit_amount)
    
    # Check the response from M-Pesa for success or failure
    if mpesa_response.get("success"):
        # Process the successful deposit and update the user's wallet balance
        user.wallet.balance += deposit_amount
        user.wallet.save()
        return Response({"message": "Deposit successful."}, status=status.HTTP_200_OK)
    else:
        # Handle the case of a failed deposit
        return Response({"error": "Deposit failed."}, status=status.HTTP_400_BAD_REQUEST)

# views.py

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def initiate_deposit(request):
    # ...

    if mpesa_response.get("success"):
        # Process the successful deposit and update the user's wallet balance

        # Trigger a WebSocket notification
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{user.id}",  # You can use a unique identifier for the user
            {"type": "notify.deposit", "message": "Deposit successful."},
        )

        return Response({"message": "Deposit successful."}, status=status.HTTP_200_OK)
    else:
        # Handle the case of a failed deposit
        return Response({"error": "Deposit failed."}, status=status.HTTP_400_BAD_REQUEST)



