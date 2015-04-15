from __future__ import unicode_literals

from os.path import dirname
import warnings

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class SASSCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if isinstance(settings.PIPELINE_SASS_ARGUMENTS, (str, unicode)):
            warnings.warn("Use a list for settings.PIPELINE_SASS_ARGUMENTS", DeprecationWarning)
            arguments = [a for a in settings.PIPELINE_SASS_ARGUMENTS.split(' ') if a]
        else:
            arguments = list(settings.PIPELINE_SASS_ARGUMENTS)
        command = [settings.PIPELINE_SASS_BINARY] + arguments + [infile, outfile]
        return self.execute_command(command, cwd=dirname(infile))
