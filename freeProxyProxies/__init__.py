from .models import *
from .proxies import *
from .api import *
from .utils import *

__version__ = 'v0.1'

__doc__ = """
This is a sample module.

It provides various functions and classes for working with proxies.

- `models`: Contains proxy-related models.
- `proxies`: Provides a proxy fetching class.
- `utils`: Includes utility functions for working with proxies.
- `api`: Defines API functions for working with proxies.

Version: {version}
""".format(version=__version__)

__banner__ = """

  _____                     __________                             __________                     .__               
_/ ____\______   ____   ____\______   \_______  _______  ______.__.\______   \_______  _______  __|__| ____   ______
\   __\\_  __ \_/ __ \_/ __ \|     ___/\_  __ \/  _ \  \/  <   |  | |     ___/\_  __ \/  _ \  \/  /  |/ __ \ /  ___/
 |  |   |  | \/\  ___/\  ___/|    |     |  | \(  <_> >    < \___  | |    |     |  | \(  <_> >    <|  \  ___/ \___ \ 
 |__|   |__|    \___  >\___  >____|     |__|   \____/__/\_ \/ ____| |____|     |__|   \____/__/\_ \__|\___  >____  >
                    \/     \/                             \/\/                                   \/       \/     \/ 
                                                      
"""
