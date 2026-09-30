from rest_framework import status
from rest_framework.test import APITestCase
from .models import JobApplication

class JobApplicationApiTests(APITestCase):
    def test_create_application(self):
        response = self.client.post("/api/applications/", {
            "company_name": "Example Labs",
            "role": "Junior Python Developer",
            "status": "applied",
            "location": "Remote",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobApplication.objects.count(), 1)

    def test_search_applications(self):
        JobApplication.objects.create(company_name="Django Labs", role="Backend Developer")
        JobApplication.objects.create(company_name="Other Labs", role="QA Engineer")
        response = self.client.get("/api/applications/?search=django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
