from numpy.random import randint
from generateimages import generate_images
from convertjpg import convert_jpg
from generatepeople import generate_people
from generategeojson import generate_geojson


def main():
    seeds = randint(100000000, 1000000000, 5)
    generate_images(seeds)
    convert_jpg()
    people = generate_people()
    generate_geojson(people)


if __name__ == "__main__":
    main()
