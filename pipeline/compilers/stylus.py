from __future__ import unicode_literals

from os.path import dirname
import warnings

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class StylusCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith('.styl')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if isinstance(settings.PIPELINE_STYLUS_ARGUMENTS, (str, unicode)):
            warnings.warn("Use a list for settings.PIPELINE_STYLUS_ARGUMENTS", DeprecationWarning)
            arguments = [a for a in settings.PIPELINE_STYLUS_ARGUMENTS.split(' ') if a]
        else:
            arguments = list(settings.PIPELINE_STYLUS_ARGUMENTS)
        command = [settings.PIPELINE_STYLUS_BINARY] + arguments + [infile]
        return self.execute_command(command, cwd=dirname(infile))
