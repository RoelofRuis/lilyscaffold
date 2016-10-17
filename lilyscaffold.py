import argparse
from templating.factory import *
from io import read

def parseArgs():
    parser = argparse.ArgumentParser(description='Setup lilypond projects and files.')
    parser.add_argument('project', metavar='Project', help='the name of the project', type=str)
    parser.add_argument('-t', nargs=1, metavar='Template', help='the project template', type=str)
    parser.add_argument('-b', action='store_true', help='build the project')
    return parser.parse_args()

if __name__ == '__main__':
    args = parseArgs()
    if args.t is not None and args.t[0] in read.getAvailableProjects():
        projectWriter = ProjectFileWriter(args.project)
        projectWriter.setupProjectStructure()
        projectWriter.setupTemplate(args.t[0])
    if args.b:
        factory = LilypondFactory(args.project)
        factory.buildProject()