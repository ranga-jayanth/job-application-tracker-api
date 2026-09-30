from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="JobApplication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("company_name", models.CharField(max_length=120)),
                ("role", models.CharField(max_length=160)),
                ("status", models.CharField(choices=[("wishlist", "Wishlist"), ("applied", "Applied"), ("interview", "Interview"), ("offer", "Offer"), ("rejected", "Rejected")], default="wishlist", max_length=20)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("job_url", models.URLField(blank=True)),
                ("applied_on", models.DateField(blank=True, null=True)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-updated_at"]},
        ),
    ]
