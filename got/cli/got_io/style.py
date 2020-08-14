from clikit.api.formatter import Style
from clikit.api.formatter import StyleSet


class GotStyleSet(StyleSet):
    """
    The got style set
    """

    def __init__(self):  # type: () -> None
        styles = [
            Style("info").fg("white").bold(),
            Style("comment").fg("cyan").bold(),
            Style("question").fg("magenta").bold(),
            Style("success").fg("green").bold(),
            Style("warning").fg("yellow").bold(),
            Style("error").fg("red").bold(),
            Style("b").bold(),
            Style("blink").blinking(),
            Style("u").underlined(),
            Style("c1").fg("cyan"),
            Style("bc1").fg("cyan").bold(),
            Style("c2").fg("yellow"),
        ]

        super(GotStyleSet, self).__init__(styles)
