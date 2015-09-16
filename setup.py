import os
from setuptools import setup


def read(*path):
    """Use this to read files from source directory"""
    with open(
            os.path.join(os.path.dirname(__file__), *path),
            encoding="utf8"
    ) as fp:
        return fp.read()


setup(

    # Name must be lowercase and use '-' as separator like this: rucola-something
    name="rucola-yamlfm",
    version='0.0.1',
    license="MIT",

    description="A Rucola plugin used to load YAML frontmatters.",
    long_description=read("README.rst"),

    author="Kasper Minciel",
    author_email="kasper.minciel@gmail.com",

    url="https://github.com/lecnim/rucola-yamlfm",

    py_modules=['rucola_yamlfm'],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',

    classifiers=[
        "Environment :: Plugins"
    ],

    # Remember to add all required packages!
    install_requires=["rucola", "pyyaml"]
)
