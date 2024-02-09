#!/usr/bin/env python

import setuptools

VER = "0.0.1"

setuptools.setup(
    name="SCAnalysis",
    version=VER,
    author="Zae Moore",
    author_email="emoore06@syr.edu",
    description="A package for analyzing data from the Single Cube at SU",
    url="https://github.com/ZaeMoore/singlecube-analysis",
    packages=setuptools.find_packages(where="src"), #"where" is needed; "include=['LarpixParser']" is not necessary 
    package_dir={"":"src"},
    package_data={"SCAnalysis": ["config_repo/*.yaml",
                                   "config_repo/dict_repo/*.pkl"]},
    install_requires=["numpy", "h5py", "fire"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    python_requires='>=3.2',
)