from __future__ import unicode_literals
import warnings

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class LiveScriptCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, path):
        return path.endswith('.ls')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled
        if isinstance(settings.PIPELINE_LIVE_SCRIPT_ARGUMENTS, (str, unicode)):
            warnings.warn("Use a list for settings.PIPELINE_LIVE_SCRIPT_ARGUMENTS", DeprecationWarning)
            arguments = [a for a in settings.PIPELINE_LIVE_SCRIPT_ARGUMENTS.split(' ') if a]
        else:
            arguments = list(settings.PIPELINE_LIVE_SCRIPT_ARGUMENTS)
        command = [settings.PIPELINE_LIVE_SCRIPT_BINARY, '-cp'] + arguments + [infile]
        stdout = open(outfile, 'w+')
        return self.execute_command(command, stdout=stdout)
