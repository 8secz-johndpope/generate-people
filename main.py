from numpy.random import default_rng
from numpy import unique
from generateimages import generate_images
from convertjpg import convert_jpg
from generatepeople import generate_people
from generategeojson import generate_geojson
from generatejson import generate_json


def main(maxN=5):
    seeds = unique(randint(100000000, 1000000000, maxN))
    generate_images(seeds)
    convert_jpg()
    people = generate_people()
    generate_geojson(people)
    generate_json(people)
    print(f"Done generating {len(people)} out of {len(maxN)} people.")


if __name__ == "__main__":
    main()
