#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>

from app import app
from database import db
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand


db.init_app(app)
manager = Manager(app)
migrate = Migrate(app,db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))


if __name__ == '__main__':
    manager.run()

