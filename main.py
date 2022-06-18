import os
import logging

logging.basicConfig(level=logging.INFO)

MAX_GROUP_SIZE = 15  # arg
INPUT_FILENAME = 'input.txt'
OUTPUT_FILENAME = 'output.txt'
APPENDER = '^'
data = []


def clear():
    data = []
    if os.path.exists(OUTPUT_FILENAME):  # const
        os.remove(OUTPUT_FILENAME)
    else:
        print('The file does not exist')


def load():
    f = open(INPUT_FILENAME, "r")
    for line in f.readlines():
        data.append(line.rstrip('\n'))


def run():
    logging.info('Starting')

    while data:
        output = data[:MAX_GROUP_SIZE]
        del data[:MAX_GROUP_SIZE]

        logging.info('Writing line...')

        f = open(OUTPUT_FILENAME, 'a')
        f.write(APPENDER.join(output))
        f.write('\n')
        f.close()

    logging.info('Finished')


clear()
load()
run()
