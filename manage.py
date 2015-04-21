import os
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='knowhow/*')
    COV.start()

from flask_script import Manager

from knowhow import create_app

app = create_app(os.getenv('KNOWHOW_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
