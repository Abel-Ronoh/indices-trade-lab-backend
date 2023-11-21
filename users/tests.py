import pytest
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from users.models import User, Affiliate, Portfolio
from PIL import Image
from io import BytesIO
import os
from django.conf import settings

@pytest.mark.django_db
class TestUsersModels(TestCase):
    """encompases all models in the users model module"""
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='testuser',
            id_number='12345678',
            email='test@test.com'
        )

    def test_user_model_creation(self):
        """test if user is created"""
        assert self.user.id is not None
        assert self.user.username == 'testuser'
        assert self.user.email == 'test@test.com'
        assert self.user.id_number == '12345678'

    def test_affiliate_model_creation(self):
        """test if affiliate is created"""
        affiliate = Affiliate.objects.filter(user=self.user).first()
        assert affiliate.id is not None
        assert affiliate.user == self.user
        assert affiliate.referral_link == 'https://forextradesacco.com/?ref=testuser'


    def test_portfolio_model_creation(self):
        """Test if portfolio is created"""
        self.portfolio = Portfolio.objects.filter(user=self.user).first()
        assert self.portfolio.id is not None
        assert self.portfolio.user == self.user
        assert self.portfolio.balance == 0

    def test_portfolio_model_image_resizing(self):
        """Test image resize function"""
        img = Image.new('RGB', (400, 400), color='red')
        file = BytesIO()
        img.save(file, 'png')
        file.seek(0)
        user_photo = SimpleUploadedFile('test.png', file.getvalue())

        self.test_portfolio_model_creation()
        assert self.portfolio.photo.width <= 300
        assert self.portfolio.photo.height <= 300

        # Delete the test image after testing
        file = os.path.join(settings.BASE_DIR, 'media_root/profile_pics/test.png')
        if os.path.exists(file):
            os.remove(file)
        else:
            print(f"File '{file}' does not exist.")

