from django.db import models

class Student(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    smijerOdab = models.CharField(max_length=50)
    skola = models.CharField(max_length=50)
    prosjekOc = models.FloatField()
    maturaOc = models.FloatField()
    datumRodj = models.DateField()
    mjestoRodj = models.CharField(max_length=100)
    molbaUpis = models.CharField(max_length=500)

    def __str__(self):
        return f"Student {self.fName} {self.lName}"
# Add finished school document field
