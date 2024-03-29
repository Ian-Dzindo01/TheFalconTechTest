from django.db import models
from django.contrib.auth.models import User

class FieldOfStudy(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # Available seats in given course
    quota = models.IntegerField(default=0)                     
    student_count = models.IntegerField(default=0)
    
    # Pretty printing
    def __str__(self):
        return self.name

class Student(models.Model):
    broj = models.PositiveIntegerField()
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    skola = models.CharField(max_length=50)
    prosjek = models.FloatField()
    datum = models.DateField()
    ocijena_mature = models.FloatField()
    mjesto = models.CharField(max_length=100)
    molba = models.CharField(max_length=500)
    smijer = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)
    doc = models.FileField(upload_to='pdf_documents/', blank=True, null=True)
    # For further development
    # user = models.OneToOneField(User, on_delete=models.CASCADE)     

    def __str__(self):
        return f"Student: {self.ime} {self.prezime}"