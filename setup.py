import setuptools
from os import path

here = path.abspath(path.dirname(__file__))
requires_list = []
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    for line in f:
        requires_list.append(str(line))

setuptools.setup(
    name="testpackagepower",
    version= "0.0.2",
    url="https://github.com/MauricioSalazare/testpackagepower",
    author="Mauricio Salazar",
    author_email="e.m.salazar.duque@tue.nl",
    description="This package does nothing",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=requires_list,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
)