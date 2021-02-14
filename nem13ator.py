import logging
from argparse import ArgumentParser
from sys import exit

from nem13ator import nem13ator


# set log level to INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    try:
        # command line arguments
        parser = ArgumentParser(description='AEMO nem13 file processor')
        parser.add_argument(
                'nem13_file',
                type=str,
                nargs='?',
                help='nem13 file path (required)')
        parser.add_argument(
                '--database',
                type=str,
                nargs='?',
                default='./data/main.db',
                help='SQLite database file location (optional)')
        args = parser.parse_args()

        if args.nem13_file:
            # call nem13ator to process data
            processor = nem13ator.NEM13ator(
                file_path=args.nem13_file,
                database=args.database)
            print('{} records added.'.format(processor.process()))
        else:
            logging.critical('You must provide path to the nem13 file.')
            exit(2)
    except FileNotFoundError as e:
        logging.critical('Make sure nem13 file exists.')
        exit(2)
    except RuntimeError as e:
        logging.critical('Runtime error: {}'.format(e))
        exit(2)


if __name__ == '__main__':
    main()
