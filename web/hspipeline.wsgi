import sys, os
from paths import Paths

activate_this = os.path.join(Paths.base, 'env', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path = [Paths.base, Paths.bins] + sys.path
from app import app as application
