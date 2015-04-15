from __future__ import unicode_literals

import warnings

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class CoffeeScriptCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, path):
        return path.endswith('.coffee') or path.endswith('.litcoffee')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled
        if isinstance(settings.PIPELINE_COFFEE_SCRIPT_ARGUMENTS, (str, unicode)):
            warnings.warn("Use a list for settings.PIPELINE_COFFEE_SCRIPT_ARGUMENTS", DeprecationWarning)
            arguments = [a for a in settings.PIPELINE_COFFEE_SCRIPT_ARGUMENTS.split(' ') if a]
        else:
            arguments = list(settings.PIPELINE_COFFEE_SCRIPT_ARGUMENTS)
        command = [settings.PIPELINE_COFFEE_SCRIPT_BINARY, '-cp'] + arguments + [infile]
        stdout = open(outfile, 'w+')
        return self.execute_command(command, stdout=stdout)
