from clikit.api.io import Input
from clikit.api.io import Output
from clikit.formatter import AnsiFormatter
from clikit.formatter import PlainFormatter
from clikit.io import ConsoleIO
from clikit.io.input_stream import StandardInputStream
from clikit.io.output_stream import ErrorOutputStream
from clikit.io.output_stream import StandardOutputStream
from cleo.io.io_mixin import IOMixin


class GotIO(ConsoleIO, IOMixin):
    """
    class for io that's no in cleo commands
    """

    def __init__(self, style_set):

        input_stream = StandardInputStream()
        input = Input(input_stream)

        output_stream = StandardOutputStream()
        if output_stream.supports_ansi():
            formatter = AnsiFormatter(style_set)
        else:
            formatter = PlainFormatter(style_set)

        output = Output(output_stream, formatter)

        error_stream = ErrorOutputStream()
        if error_stream.supports_ansi():
            formatter = AnsiFormatter()
        else:
            formatter = PlainFormatter()

        error_output = Output(error_stream, formatter)

        super(GotIO, self).__init__(input, output, error_output)
