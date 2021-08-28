from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase


class DjangoConfigTestCase(TestCase):
    def test_secret_strength(self):
        secret_key = settings.SECRET_KEY
        try:
            is_strong = validate_password(secret_key)
        except Exception as e:
            msg = f'Bad SECRET_KEY {e.messages}'
            self.fail(msg)
