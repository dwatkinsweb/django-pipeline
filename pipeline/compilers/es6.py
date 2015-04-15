from __future__ import unicode_literals
import warnings

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class ES6Compiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, path):
        return path.endswith('.es6')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled
        if isinstance(settings.PIPELINE_BABEL_ARGUMENTS, (str, unicode)):
            warnings.warn("Use a list for settings.PIPELINE_BABEL_ARGUMENTS", DeprecationWarning)
            arguments = [a for a in settings.PIPELINE_BABEL_ARGUMENTS.split(' ') if a]
        else:
            arguments = list(settings.PIPELINE_BABEL_ARGUMENTS)
        command = [settings.PIPELINE_BABEL_BINARY] + arguments + [infile, '-o', outfile]
        return self.execute_command(command)
