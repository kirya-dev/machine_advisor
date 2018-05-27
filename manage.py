#!/usr/bin/env python
from backend.app import manager


@manager.command
def hello(arg):
    print("Hello command says {0}".format(arg))


manager.run()
