from clikit.api.formatter import Style
from clikit.api.formatter import StyleSet


class GotStyleSet(StyleSet):
    """
    The got style set
    """

    def __init__(self):  # type: () -> None
        styles = [
            Style("info").fg("green"),
            Style("comment").fg("cyan"),
            Style("question").fg("blue"),
            Style("error").fg("red").bold(),
            Style("b").bold(),
            Style("u").underlined(),
            Style("c1").fg("cyan"),
            Style("bc1").fg("cyan").bold(),
            Style("c2").fg("yellow"),
            Style("success").fg("white").bg("blue").bold(),
        ]

        super(GotStyleSet, self).__init__(styles)
