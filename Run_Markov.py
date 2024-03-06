import sys
sys.path.append('/Users/james/Desktop/file_cabinet/work/bioinformatics/github/Markov/MarkovProprietary/pipelinestages')
from fetch_from_mount import *
import subprocess
import os
import shutil

os.chdir('../MarkovProprietary/pipelinestages/app/mount/input')
names = open("names.txt")
print("success")

names_lines = names.readlines()
names.close()
names1 = names_lines[0]
names2 = names_lines[1]

os.chdir('../../..')

# fetch receptor name
PDB_ID = search_pdb_by_protein_name(names1)
first_file_path = cifDownload(PDB_ID)
first_file = shutil.move(first_file_path, '../../markov_opensource')
print(first_file_path)

PDB_ID = search_pdb_by_protein_name(names2)
second_file_path = cifDownload(PDB_ID)
second_file = shutil.move(second_file_path, '../../markov_opensource')
print(second_file)
