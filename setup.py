<<<<<<< HEAD
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydistrrr",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A package calculate distnaces between points",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UBC-MDS/pydistrrr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
=======
from distutils.core import setup

setup(name='pydistrrr',
      version='1.0',
      description='Distance Metrics',
      author='Shayne Andrews, Carrie Cheung, Evan Yathon, Mike Yuan',
      url='https://github.com/UBC-MDS/pydistrrr',
      packages=['pydistrrr']
     )
>>>>>>> upstream/master
