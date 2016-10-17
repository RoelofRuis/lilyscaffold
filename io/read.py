import os
from os     import walk
from config import GLOBAL_CONFIG

def getAvailableProjects():
    (_,_, files) = walk(GLOBAL_CONFIG.get('projectTemplateFolder', 'templates\\projects\\')).next()
    filenames = [os.path.splitext(f)[0] for f in files]
    return filenames