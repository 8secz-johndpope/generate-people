from numpy.random import randint
import sys, os

path = os.path.join(os.path.dirname(__file__), "stylegan2")
sys.path.append(path)

import stylegan2.dnnlib as dnnlib


def generate_images(seeds):
    sc = dnnlib.SubmitConfig()
    sc.num_gpus = 1
    sc.submit_target = dnnlib.SubmitTarget.LOCAL
    sc.local.do_not_copy_source_files = True
    sc.run_dir_root = "dist/generated-images-1"
    sc.run_desc = "generate_images"

    kwargs = {
        "network_pkl": "gdrive:networks/stylegan2-ffhq-config-f.pkl",
        "seeds": seeds,
        "truncation_psi": 0.5,
    }

    dnnlib.submit_run(sc, "run_generator.generate_images", **kwargs)


if __name__ == "__main__":
    generate_images(randint(100000000, 1000000000, 5))
