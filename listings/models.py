from django.db import models

class Listing(models.Model):
    CONDITION_CHOICES = [
        ('NEW', 'Like New'),
        ('GOOD', 'Good'),
        ('USED', 'Fair / Heavily Used'),
    ]

    title = models.CharField(max_length=200)
    dept_code = models.CharField(max_length=20, help_text="e.g., CS")
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES, default='GOOD')
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.dept_code})"