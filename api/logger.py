import logging.config
import sys

def Logger():
    LOGGING = {
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'stream': sys.stdout,
            }
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }

    logging.config.dictConfig(LOGGING)
    return logging

