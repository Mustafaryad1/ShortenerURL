import os

from flask_script import Manager

from shortener_url import app 

manager  = Manager(app)

if __name__ == '__main__':
    manager.run()