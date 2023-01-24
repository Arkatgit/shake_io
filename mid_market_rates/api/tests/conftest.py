import sys, os

# Make sure that the application source directory (this directory's parent) is
# on sys.path.

#here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.insert(0, here)

from os.path import dirname, realpath

filepath = realpath(__file__)

dir_of_file = dirname(filepath)
parent_dir_of_file = dirname(dir_of_file)
parents_parent_dir_of_file = dirname(parent_dir_of_file)
parents_parent_parent_of_file = dirname(parents_parent_dir_of_file)
sys.path.insert(0, parents_parent_parent_of_file)
