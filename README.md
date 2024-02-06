A repository for full stack website coding task. Made with Django.
Before running instantiate the needed fields. Added for the sake of user customizability:
 
## Usage:
```
python manage.py shell
```

 ``` 
from your_app.models import FieldOfStudy

tehnoloski = FieldOfStudy.objects.create(name='Tehnoloski', student_count=0, quota=20)
matematicki = FieldOfStudy.objects.create(name='Matematicki', student_count=0, quota=120)
informaticki = FieldOfStudy.objects.create(name='Informaticki', student_count=0, quota=10)
 ```
```
python manage.py runserver
```
#### Administrators (professors) are to access the page by following the admin login button on the main Login page.
#### There they have all the functionalities for editing and deleting both users and administrators.
#### Administrators are create with the createsuperuser function.

## TODO:
* Add Docker file.
* Add @login_required.
* Add message for when admins switches a students degree.
* Add tests.
  
Work in progress.
