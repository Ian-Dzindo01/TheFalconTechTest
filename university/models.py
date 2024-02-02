from django.db import models

class Student(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    smijerOdab = models.CharField(max_length=50)
    skola = models.CharField(max_length=50)
    prosjekOc = models.FloatField()
    datumRodj = models.DateField()
    maturaOc = models.FloatField()
    mjestoRodj = models.CharField(max_length=100)
    molba = models.CharField(max_length=500)
    doc = models.FileField()

    def __str__(self):
        return f"Student: {self.fName} {self.lName}"
    
class FieldOfStudy(models.Model):
    name = models.CharField(max_length=100, default='Tehnicki')
    description = models.TextField(default='Smijer obrazovanja')
    quote = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name


# Add finished school document field
