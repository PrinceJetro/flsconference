from django.test import TestCase
from django.urls import reverse
from home.models import Registration

class RegistrationTestCase(TestCase):
    def test_registration_success(self):
        url = reverse('registration')
        data = {
            'title': 'Dr',
            'name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '+234 801 234 5678',
            'institution': 'University of Lagos',
            'category': 'Academic & Regular Delegate',
            'track': 'Emerging and re-emerging infectious diseases',
            'dietary_requirements': 'None',
            'payment_reference': 'REF12345',
            'technical_preferences': ['Morning plenary sessions', 'Scientific poster sessions']
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        
        # Verify Registration object was created
        reg = Registration.objects.get(email='test@example.com')
        self.assertEqual(reg.phone_number, '+234 801 234 5678')
        self.assertEqual(reg.name, 'Test User')
        self.assertTrue(reg.pref_plenary)
        self.assertTrue(reg.pref_poster)
        self.assertFalse(reg.pref_dinner)
        
    def test_registration_validation_error_missing_phone(self):
        url = reverse('registration')
        data = {
            'title': 'Dr',
            'name': 'Test User',
            'email': 'test@example.com',
            # 'phone_number': missing
            'institution': 'University of Lagos',
            'category': 'Academic & Regular Delegate',
            'track': 'Emerging and re-emerging infectious diseases',
        }
        response = self.client.post(url, data)
        self.assertIn('registration_errors', response.context)
        self.assertIn('Your phone number is required.', response.context['registration_errors'])
