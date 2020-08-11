from cleo.config.application_config import ApplicationConfig
from .got_io.style import GotStyleSet

from clikit.io import ConsoleIO as BaseConsoleIO

from cleo.io.io_mixin import IOMixin


class GotAppConfig(ApplicationConfig):
    """
    Got application configuration.
    """

    @property
    def default_style_set(self):
        return GotStyleSet()
