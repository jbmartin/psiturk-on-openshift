#<% G %>/usr/bin/env python
import os
import sys
from flask import Flask

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def hello_world():
    return "Hello World!"

PYCART_DIR = ''.join(['python-', '.'.join(map(str, sys.version_info[:2]))])

try:
   zvirtenv = os.path.join(os.environ['OPENSHIFT_HOMEDIR'], PYCART_DIR,
                           'virtenv', 'bin', 'activate_this.py')
   execfile(zvirtenv, dict(__file__ = zvirtenv) )
except IOError:
   pass

# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#


#
#  main():
#
if __name__ == '__main__':
   ip   = os.environ['OPENSHIFT_PYTHON_IP']
   port = 8080
   print 'Starting WSGIServer on %s:%d ... ' % (ip, port)
   try:
      app.run(debug=True, host=ip, port=port)
   except:
      print 'Installation problems, server failed to start'
