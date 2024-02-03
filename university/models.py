from django.db import models

class Student(models.Model):
    study_choices = [
        ('Informatički', 'Informatički'),
        ('Tehnički', 'Tehnički'),
        ('Matematički', 'Matematički')]
    
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
    # doc = models.FileField()
    smijer = models.CharField(max_length=50, choices=study_choices)


    def __str__(self):
        return f"Student: {self.ime} {self.prezime}"

