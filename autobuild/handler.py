import os
import time
from watchdog.events import FileSystemEventHandler
from subprocess import Popen, PIPE

def getfrompath(filename, type):
    if type == 'ext':
        return os.path.splitext(filename)[-1].lower()
    elif type == 'dir':
        return os.path.dirname(filename).lower()
    elif type == 'fname':
        return os.path.splitext(filename)[0].lower()
    
def build(filename):
    fname = getfrompath(filename, 'fname')
    print fname
    process = Popen(["lilypond", "-s", "-o", fname, filename], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    print 'builder for file %s exited with code %d' % (filename, exit_code)
    
class LilypondBuildHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        ext = getfrompath(event.src_path, 'ext')
        if ext == '.ly':
            build(event.src_path)