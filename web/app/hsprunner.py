import os
import time
from getpass import getuser
from shutil import move
from time import localtime, strftime
from subprocess import Popen, PIPE, STDOUT, call, check_output
from paths import Paths

class Hsprunner(object):
    def __init__(self, form):
        self.timestamp = strftime("%Y%m%d%H%M", localtime())
        self.end_type = 'p'
        self.threads = '-t8'

        self.paths = Paths(proj=form.project_path.data,
                           anc=form.anc_path.data, ref=form.ref_path.data)

        self.cmd_name = 'hspipeline'

        (self.paths.outlog,
         self.paths.outlog_final) = [os.path.join(self.paths.output,
                                                  self.timestamp + p)
                                                  for p in
                                                  ['-outlog.txt',
                                                   '-outlog-final.txt']]

        self.parts_to_run = _make_command_string(align=form.align.data,
                                                 trim=form.trim.data,
                                                 find=form.find.data,
                                                 compare=form.compare.data,
                                                 plot=form.plot.data)

        self.cmd = [self.cmd_name,
                    self.parts_to_run,
                    self.threads,
                    self.end_type,
                    self.paths.proj,
                    self.paths.ref,
                    self.paths.anc,
                    self.paths.r]

        if not os.path.exists(self.paths.output):
            os.makedirs(self.paths.output)
            time.sleep(0.5)

    def run(self):

        with open(self.paths.outlog, 'w', 0) as outfile:
            outfile.write("command: {}\n".format(" ".join(self.cmd)))

            time.sleep(0.5)

            try:
                call(self.cmd, stdout=outfile, stderr=STDOUT)
            except Exception as e:
                err = ('Hsprunner.run() failed with error code {}: {}'.
                       format(e.errno, e.strerror))
                outfile.write(err + '\n')
                outfile.flush()
                print err

        move(self.paths.outlog, self.paths.outlog_final)

def _make_command_string(align, trim, find, compare, plot):
    align = align and 'A' or ''
    trim = trim and 'x' or ''
    find = find and 'F' or ''
    compare = compare and 'C' or ''
    plot = plot and 'P' or ''
    commands = "".join([align, trim, find, compare, plot])

    if commands != "":
        commands = '-' + commands

    return commands

if __name__ == "__main__":
    pass

