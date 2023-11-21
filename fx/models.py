from django.db import models
from PIL import Image
from users.models import User

TRADE_TYPE = (
    ('B', 'buy'),
    ('S', 'sell')
)

TRADE_STATUS = (
    ('O', 'open'),
    ('C', 'complete')
)

PAYMENT_TYPE = (
    ('D', 'deposit'),
    ('W', 'withdrawal')
)

PAYMENT_STATUS = (
    ('P', 'pending'),
    ('C', 'complete')
)

PAYMENT_GATEWAY = (
    ('S', 'stripe'),
    ('P', 'paypal'),
    ('M', 'mpesa')
)

class Stock(models.Model):
    """store stocks/forex user manipulates"""
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

class Payment(models.Model):
    """Store made payment (Deposit/Withdraw)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_gateway = models.CharField(choices=PAYMENT_GATEWAY, max_length=50)
    customer_id = models.CharField(max_length=50)
    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=PAYMENT_STATUS, max_length=1)

    def __str__(self):
        return f"{self.user.username} - {self.payment_type} - {self.amount} - {self.payment_gateway}"


class Trade(models.Model):
    """Trades/transaction done by user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    trade_type = models.CharField(choices=TRADE_TYPE, max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=TRADE_STATUS, default='O', max_length=1)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock.name} - {self.timestamp}"
