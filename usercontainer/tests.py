from django.test import TestCase
from usercontainer.models import User

# Create your tests here.

class UserModelTests(TestCase):
    def test_user_model(self):
        user = User.objects.get(
            username='john',
            password='john',
        )

        user.save()

        self.assertEqual(user.username, 'john')
        # self.assertTrue(user.is_active)
        # self.assertFalse(user.is_staff)
        # self.assertFalse(user.is_superuser)
