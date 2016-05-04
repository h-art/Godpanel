from fabric.api import local, run, execute, env

# use ssh config (necessary for ssh keys)
env.use_ssh_config = True


def git_pull():
    run("cd $PROJECT_DIR && git pull")


def collectstatic():
    run("cd $PROJECT_DIR && python manage.py collectstatic --noinput")


def test():
    run("cd $PROJECT_DIR && python manage.py test")


def restart_app():
    run("cd $PROJECT_DIR && touch hart/$WSGI_SCRIPT")

def deploy():
    execute(git_pull)
    execute(collectstatic)
    execute(restart_app)
