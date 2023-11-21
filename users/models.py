from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from PIL import Image


class User(AbstractUser):
    """custom user model"""
    id_number = models.CharField(max_length=8, unique=True, verbose_name='Kenyan ID Number')
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username


class Affiliate(models.Model):
    """Store the affiliate system"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_link = models.CharField(max_length=100, unique=True)
    referrals = models.ManyToManyField(User, blank=True, related_name='referrals')

    def __str__(self) -> str:
        return f"Affiliate: {self.user.username}"


@receiver(post_save, sender=User)
def create_affiliate(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'affiliate'):
            referral_link = f'https://forextradesacco.com/?ref={instance.username}'
            affiliate, _ = Affiliate.objects.get_or_create(user=instance, defaults={'referral_link': referral_link})


class Portfolio(models.Model):
    """This acts as the user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics', null=True, blank=True)
    affiliate = models.OneToOneField(Affiliate, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Portfolio, self).save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"


@receiver(post_save, sender=User)
def create_portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_portfolio(sender, instance, **kwargs):
    instance.portfolio.save()
