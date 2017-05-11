"""
rvtracker setup / installation script

See README.rst for more information
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rvtracker',
    version='0.0.0',

    description='Toolkit for monitoring recreational vehicles (RV)',
    long_description=long_description,
    url='https://github.com/schluntz/rvtracker',
    author='Sean Schluntz',
    author_email='sean@schluntz.com',
    license='MIT',
    keywords='rv monitoring travel',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: MIT License',
        # Intended for lightweight devices like Raspberry Pi
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # Compatibility for 3 is a target
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['bin', 'data', 'docs', 'tests']),
    package_data{'rvtracker':'data'}, 

    # install_requires=[
    #    'jsonrpclib',
    #    'httplib2',
    # ],

    entry_points={
        'scripts': [
            'bin/rvt',
        ],
    },
)

