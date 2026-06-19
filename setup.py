import sys
from setuptools import setup
from subprocess import call
from setuptools.command.build import build

class Build(build):
    def run(self):
        cmd = ["make", "-C", "./SJARACNe"]
        if call(cmd) != 0:
            sys.exit(-1)
        super.run()

setup(
    cmdclass={
        'build': Build,
    }
)
