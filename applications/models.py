from django.db import models

class JobApplication(models.Model):
    class Status(models.TextChoices):
        WISHLIST = "wishlist", "Wishlist"
        APPLIED = "applied", "Applied"
        INTERVIEW = "interview", "Interview"
        OFFER = "offer", "Offer"
        REJECTED = "rejected", "Rejected"

    company_name = models.CharField(max_length=120)
    role = models.CharField(max_length=160)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.WISHLIST)
    location = models.CharField(max_length=120, blank=True)
    job_url = models.URLField(blank=True)
    applied_on = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.role} at {self.company_name}"
