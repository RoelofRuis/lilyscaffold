import time
from watchdog.observers import Observer
from autobuild.handler import *

if __name__ == "__main__":
    path = 'out/.'
    event_handler = LilypondBuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print "The lilypond autobuilder is started and listening for changes!"
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print "Goodbye!"