from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TahConfig(AppConfig):
    name = "journal.tah"
    verbose_name = _("Tah")

    def ready(self):
        try:
            import journal.tah.signals  # noqa F401
        except ImportError:
            pass
