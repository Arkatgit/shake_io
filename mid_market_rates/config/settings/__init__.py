"""
Settings used by the orders project
This consists of the general produciton settings, with an
optional import of any local
settings.
"""
from mid_market_rates.config.settings.production import *  # noqa

try:
    from config.settings.local import *  # noqa

except ImportError:
    pass
