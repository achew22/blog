"""
Plugin to preprocess the metainformation of a post into the proper rich type
"""

import logging

from datetime import datetime
from pelican import signals

logger = logging.getLogger(__name__)


def as_date(value):
    return datetime.strptime(value, "%Y-%m-%d")  # 2010-09-03

def preprocess_metainformation(generator, metadata):
    #print(metadata)
    for key, value in metadata.items():
        if key.find("date") != -1 and type(value) == type("2010-09-03"):
            metadata[key] = as_date(metadata[key])

    return
    if 'license' not in metadata.keys()\
        and 'LICENSE' in generator.settings.keys():
            metadata['license'] = generator.settings['LICENSE']


def register():
    """
    Listen to the appropriate signals that will allow us to properly
    generate
    """
    # import pdb
    # pdb.set_trace()

    signals.article_generator_context.connect(preprocess_metainformation)
