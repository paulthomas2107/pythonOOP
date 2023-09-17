import logging

logging.basicConfig(level=logging.DEBUG, filename='example.log',
                    filemode='w', format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')

logging.debug('Ignore me')
logging.info('I will be logged')
logging.warning('And this too....')

