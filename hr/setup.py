from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
   readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Worker for user management',
    long_description=readme,
    author='Mark Fieldhouse',
    author_email='Mark.Fieldhouse@mafitconsulting.co.uk',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
)

