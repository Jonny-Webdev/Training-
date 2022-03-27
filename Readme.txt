c:/portfolio/Pythonstuff/fitness_project/virt/Scripts/Activate.ps1
pip

git bash 
cd /c/portfolio
python -m venv virt
source virt/Scripts/activate
pip install django
ls
cd fitness_project
python manage.py runserver



Python -m pip install virtualenv

python3 -m virtualenv <env_name>
python3 -m virtualenv priyaenv

source <env_name>/bin/activate
source priyaenv/bin/activate

source env_Jonnyfit/bin/activate

pip install Django

cd <filepath>
cd C:/Downloads/fitness_project

cd ~/Downloads/fitness_project

python manage.py runserver

http:127.0.0.1:8000/jfit/
http:127.0.0.1:8000/admin/

Admin credentials?


python manage.py createsuperuser


python manage.py shell

from fitness_project.models import Article
from covid_blog.models import Exercise
from fitness_project.models import Exercise
from jfit.models import Exercise

Exercise.objects.all()

exercise1 = Exercise(exercise_type="Yoga", duration= 10, datetime="2021-10-01")

exercise1.save()

 admin
123456