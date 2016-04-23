from fabric.api import local

def test():
  local("./manage.py test")

def build():
  local("./manage.py reset_db --noinput")
  local("./manage.py migrate")
  local("./manage.py sqlflush | ./manage.py dbshell")
  local("./manage.py loaddata initial_data")
