import importlib
import sys, os
from glob import glob
import subprocess
import csv
import names
from .generatelocation import get_coord


def runModel(checkpoint, target, class_type):
    subprocess.run(
        [
            sys.executable,
            "rude-carnie/guess.py",
            "--model_type",
            "inception",
            "--model_dir",
            f"checkpoints/{checkpoint}",
            "--class_type",
            class_type,
            "--filename",
            "dist/generated-images-1.txt",
            "--target",
            target,
            "--single_look",
        ]
    )


def generate_people():
    recentDir = max(
        glob(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "dist",
                "generated-images-1",
                "*/",
            )
        ),
        key=os.path.getmtime,
    )

    images = glob(os.path.join(recentDir, "*.png"))

    with open("dist/generated-images-1.txt", "w") as file:
        file.write("\n".join(images))

    runModel(22801, "dist/generated-images-1-ages.csv", "age")

    with open("dist/generated-images-1-ages.csv", newline="\r\n") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            overTwenty = eval(row[1])[1] > 20
            if not overTwenty:
                filename = row[0]
                os.remove(filename)
                images.remove(filename)

    with open("dist/generated-images-1.txt", "w") as file:
        file.write("\n".join(images))

    runModel(21936, "dist/generated-images-1-genders.csv", "gender")

    genders = {"M": "male", "F": "female"}

    people = []

    with open("dist/generated-images-1-genders.csv", newline="\r\n") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            gender = genders[row[1]]
            name = names.get_full_name(gender=gender)
            location = get_coord()
            pathPart = os.path.splitext(os.path.basename(row[0]))[0][4:]
            people.append(
                {"gender": gender, "name": name, "location": location, "id": pathPart}
            )

    return people
