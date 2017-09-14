from setuptools import setup, find_packages, Command

class test_skmvs(Command):
    pass

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='skmd',
    version='0.0.1',
    description='Sub Kepler Machine Data',
    long_description=readme,
    author='Hilaly Amine',
    author_email='hilalyamine@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'examples'))
)
