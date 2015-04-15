from __future__ import unicode_literals

from os.path import dirname
import warnings

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class LessCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith('.less')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        # Pipe to file rather than provide outfile arg due to a bug in lessc
        if settings.PIPELINE_LESS_ARGUMENTS and isinstance(settings.PIPELINE_LESS_ARGUMENTS, (str, unicode)):
            warnings.warn("Use a list for settings.PIPELINE_LESS_ARGUMENTS", DeprecationWarning)
            arguments = [a for a in settings.PIPELINE_LESS_ARGUMENTS.split(' ') if a]
        else:
            arguments = list(settings.PIPELINE_COFFEE_SCRIPT_ARGUMENTS)
        command = [settings.PIPELINE_LESS_BINARY] + arguments + [infile]
        stdout = open(outfile, 'w+')
        return self.execute_command(command, cwd=dirname(infile), stdout=stdout)
