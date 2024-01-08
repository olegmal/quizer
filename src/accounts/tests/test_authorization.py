import unittest
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class TestAuthCustomer(TestCase):
    def setUp(self):
        self.client = Client()

        self.user_password = "12345678"

        self.user = get_user_model().objects.create(email="customer@example.com")
        self.user.set_password(self.user_password)
        self.user.save()

        self.manager_password = "12345678"
        self.manager = get_user_model().objects.create(email="manager@example.com", is_staff=True)
        self.manager.set_password(self.manager_password)
        self.manager.save()

    def test_user_login_wrong_email(self):
        user_login = self.client.login(email="wrong@test.com", password=self.user_password)
        self.assertFalse(user_login)

    def test_user_login_wrong_password(self):
        user_login = self.client.login(email=self.user.email, password="wrong_password")
        self.assertFalse(user_login)

    def test_user_access_admin(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_manager_access_admin(self):
        self.client.force_login(self.manager)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @unittest.skip("The index page will be added later")
    def user_access_index_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    @unittest.expectedFailure
    def test_user_access_index_page_failure(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)
