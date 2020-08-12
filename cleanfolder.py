import os
from shutil import rmtree


def clean_folder(folder):
    if os.path.exists(folder) and os.path.isdir(folder):
        rmtree(folder)

    if not os.path.exists(folder):
        os.makedirs(folder)
