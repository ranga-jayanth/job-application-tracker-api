from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from .models import JobApplication
from .serializers import JobApplicationSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ("status", "location")
    search_fields = ("company_name", "role", "location", "notes")
    ordering_fields = ("applied_on", "created_at", "updated_at", "company_name", "status")
    ordering = ("-updated_at",)
