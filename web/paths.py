import os
from getpass import getuser

class Paths(object):
    base = '/var/www/hspipeline/web'
    bins = '/home/adamw/bin'
    data = '/home/adamw/seq_data'
    output = os.path.join(data, 'output')
    r = '/var/www/hspipeline'

    def __init__(self, proj=None, anc=None, ref=None):
        self.outlog = ''
        self.outlog_final = ''

        # Put the folder with links to all the programs on the PATH
        os.environ['PATH'] += os.pathsep + Paths.bins

        (self.proj, self.anc, self.ref) = [os.path.join(Paths.data, p)
                                           for p in [proj, anc, ref]]

        # Make the output folder if it doesn't exist.
        os.mkdirs(Paths.output)
