A repository for full stack website coding task. Made with Django.
Before running instantiate the needed fields. Added for the sake of user customizability:

python manage.py shell

from your_app.models import FieldOfStudy

tehnoloski = FieldOfStudy.objects.create(name='Tehnoloski', student_count=0, quota=100)
matematicki = FieldOfStudy.objects.create(name='Matematicki', student_count=0, quota=120)
informaticki = FieldOfStudy.objects.create(name='Informaticki', student_count=0, quota=80)

Work in progress.
