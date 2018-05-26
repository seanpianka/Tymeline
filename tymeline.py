#!/usr/bin/env python
import exifread
import datetime
import imghdr
import os
import errno
import sys
import shutil


def date_taken_info(filename):
    # Read file
    open_file = open(filename, 'rb')

    # Return Exif tags
    tags = exifread.process_file(open_file, stop_tag='Image DateTime')

    # Grab date taken
    try:
        datetaken_string = tags['Image DateTime']
    except KeyError:
        print(filename)
        return None
    datetaken_object = datetime.datetime.strptime(datetaken_string.values, '%Y:%m:%d %H:%M:%S')

    return {k: str(getattr(datetaken_object, k)).zfill(2) for k in 'month,day,year,hour,minute,second'.split(',')}


def mkdir_p(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def main(directory='.'):
    pictures = [d for d in [{'name': file, 'exif': date_taken_info(os.path.join(directory, file))} for file in os.listdir(directory) if not os.path.isdir(os.path.join(file)) and imghdr.what(os.path.join(directory, file))] if d['exif']]

    for picture in pictures:
        mkdir_p(os.path.join(directory, picture['exif']['year']))
        dest = os.path.join(directory, picture['exif']['year'], picture['exif']['month'])
        mkdir_p(dest)
        shutil.move(os.path.join(directory, picture['name']), os.path.join(dest, picture['name']))

    unsorted = [os.path.join(directory, f) for f in os.listdir(directory) if not os.path.isdir(os.path.join(directory, f)) and os.path.join(directory, f) not in (sys.argv[0], 'unsorted')]

    for file in unsorted:
        mkdir_p(os.path.join(directory, 'unsorted'))
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'unsorted', file))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append('.')
    main(sys.argv[1])
