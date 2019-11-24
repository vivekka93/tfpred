from setuptools import setup, find_packages
from codecs import open
from os import path
import os
import ssl

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), 'r') as tx:
    requirements = tx.read().split()


setup(
    name='tfpred',
    version='0.1.0',
    description='',
    long_description=long_description,
    url='https://github.com/vivekka93/tfpred',
    author='Vivek Karna',
    author_email='vivek.ka93@gmail.com',
    keywords=['tensorflow', 'predict'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: Other/Proprietary License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.7',
    ],
    download_url='https://github.com/vivekka93/tfpred/archive/0.1.0.tar.gz',
    license='Other/Proprietary License',
    platforms='any',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    test_suite="tests",
    install_requires=requirements,
    include_package_data=True
)
