import os


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s][%(processName)s][%(threadName)s][%(filename)s:%(lineno)s] %(name)s: '
                      '%(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': os.environ.get('LOGGING_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },

    'loggers': {
        '': {
            'handlers': ['default'],
            'level': os.environ.get('LOGGING_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
