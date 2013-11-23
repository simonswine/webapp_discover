__author__ = 'christian'

import sys
import os

def setup():
    """Set correct module directory"""
    module_dir = os.path.realpath(
        os.path.join(
            os.path.dirname(
                os.path.realpath(__file__)
            ),
            '..'
        )
    )

    sys.path.insert(0,module_dir)
