from distutils.core import setup

setup(name='pydistrrr',
      version='1.0',
      description='Distance Metrics',
      author='Shayne Andrews, Carrie Cheung, Evan Yathon, Mike Yuan',
      url='https://github.com/UBC-MDS/pydistrrr',
      install_requires=[
      'pandas',
      'numpy'],
      packages=setuptools.find_packages()
     )
