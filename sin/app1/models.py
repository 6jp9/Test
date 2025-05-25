from django.db import models

class Login(models.Model):
    first = models.CharField(max_length=140)
    middle = models.CharField(max_length=140, blank=True)
    last = models.CharField(max_length=140)
    dob = models.DateField()
    email = models.EmailField(max_length=140)
    mobile = models.CharField(max_length=15)
    skills = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=10)
    file = models.FileField(upload_to='resumes/', blank=True, null=True)

    class Meta:
        db_table = 'Login'  # This will set your table name explicitly

    def __str__(self):
        return self.first + " " + self.last

print("models.py is loaded")
