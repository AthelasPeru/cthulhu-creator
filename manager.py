import os

from flask.ext.script import Manager, Server


from app import create_app


env = os.environ.get('WEBAPP_ENV', 'default')

app = create_app(env)

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(
        app=app
    )

if __name__ == "__main__":
    manager.run()