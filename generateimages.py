from random import randint
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "stylegan2"))
from stylegan2.run_generator import generate_images


network_pkl = "gdrive:networks/stylegan2-ffhq-config-f.pkl"
seeds = [randint(1, 10000)]
truncation_psi = 0.5

generate_images(network_pkl, seeds, truncation_psi)
