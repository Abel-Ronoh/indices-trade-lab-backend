from django.urls import path
from fx import views

urlpatterns =[
    path('stripe_config/', views.PaymentView.as_view(),name='payment_intent'),
    path('stripe_payment_intent/', views.PaymentView.as_view(),name='payment_intent')
]
