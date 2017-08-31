from setuptools import setup, find_packages, Command


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='skm-data',
    version='1.0.0',
    description='Sub Kepler Machine Data',
    long_description=readme,
    author='Imperial Alpha laboratories',
    author_email='hilalyamine@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'sample', 'build'))
)
