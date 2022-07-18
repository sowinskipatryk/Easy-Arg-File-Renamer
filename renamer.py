import os
import argparse

# python renamer.py <path> -prefix <prefix> -num <num>

parser = argparse.ArgumentParser()

parser.add_argument('path',
                    help='path to source directory')

parser.add_argument('-prefix', default="",
                    help='filename prefix')

parser.add_argument('-num', type=int, default=1,
                    help='number of the first file')

args = parser.parse_args()

os.chdir(args.path)

i = args.num

for file in os.listdir(args.path):
    if os.path.isfile(file):
        _, file_extension = os.path.splitext(file)
        new_file_name = f"{args.prefix}{i}{file_extension}"
        os.rename(file, new_file_name)
        i += 1
