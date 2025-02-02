from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from Profile.models import UserProfile, UserBankInfo


class UserProfileCRUDTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_profile_data = {
            "first_name": "Ali",
            "last_name": "Karimi",
            "national_code": "1234567890",
            "mobile_number": "09123456789",
        }
        self.updated_user_profile_data = {
            "first_name": "Reza",
            "last_name": "Ahmadi",
            "mobile_number": "09187654321",
        }

    def test_create_user_profile(self):
        response = self.client.post('/api/user-profiles/', self.user_profile_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], self.user_profile_data['first_name'])

    def test_update_user_profile(self):
        create_response = self.client.post('/api/user-profiles/', self.user_profile_data)
        profile_id = create_response.data['id']

        response = self.client.put(f'/api/user-profiles/id/{profile_id}/', self.updated_user_profile_data)  # تغییر مسیر
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.updated_user_profile_data['first_name'])

    def test_delete_user_profile(self):
        create_response = self.client.post('/api/user-profiles/', self.user_profile_data)
        profile_id = create_response.data['id']

        response = self.client.delete(f'/api/user-profiles/id/{profile_id}/')  # تغییر مسیر
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_user_profiles(self):
        self.client.post('/api/user-profiles/', self.user_profile_data)
        response = self.client.get('/api/user-profiles/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_user_profile_detail(self):
        self.client.post('/api/user-profiles/', self.user_profile_data)
        response = self.client.get(f"/api/user-profiles/code/{self.user_profile_data['national_code']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.user_profile_data['first_name'])


class UserBankInfoCRUDTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_profile = UserProfile.objects.create(**{
            "first_name": "Ali",
            "last_name": "Karimi",
            "national_code": "1234567890",
            "mobile_number": "09123456789",
        })
        self.bank_info_data = {
            "user": self.user_profile.id,
            "card_number": "1234567812345678",
        }
        self.updated_bank_info_data = {
            "card_number": "8765432187654321",
        }

    def test_create_user_bank_info(self):
        response = self.client.post('/api/user-bank-info/', self.bank_info_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['card_number'], self.bank_info_data['card_number'])

    def test_update_user_bank_info(self):
        create_response = self.client.post('/api/user-bank-info/', self.bank_info_data)
        bank_info_id = create_response.data['id']

        response = self.client.put(f'/api/user-bank-info/id/{bank_info_id}/', self.updated_bank_info_data)  # تغییر مسیر
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['card_number'], self.updated_bank_info_data['card_number'])

    def test_delete_user_bank_info(self):
        create_response = self.client.post('/api/user-bank-info/', self.bank_info_data)
        bank_info_id = create_response.data['id']

        response = self.client.delete(f'/api/user-bank-info/id/{bank_info_id}/')  # تغییر مسیر
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_user_bank_infos(self):
        self.client.post('/api/user-bank-info/', self.bank_info_data)
        response = self.client.get('/api/bank-info/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_user_bank_info_detail(self):
        self.client.post('/api/user-bank-info/', self.bank_info_data)
        response = self.client.get(f"/api/user-bank-info/card/{self.bank_info_data['card_number']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['card_number'], self.bank_info_data['card_number'])