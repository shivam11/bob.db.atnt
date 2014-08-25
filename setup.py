#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Manuel Guenther <manuel.guenther@idiap.ch>

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='bob.db.atnt',
    version='2.0.0a0',
    description='ATNT/ORL Database Access API for Bob',
    url='http://github.com/bioidiap/bob.db.atnt',
    license='GPLv3',
    author='Manuel Guenther',
    author_email='manuel.guenther@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'bob.db.base',
      'bob.db.verification.utils' # defines a set of utilities for face verification databases like this one.
    ],

    namespace_packages = [
      'bob',
      'bob.db',
    ],

    entry_points={

      # declare database to bob
      'bob.db': [
        'atnt = bob.db.atnt.driver:Interface',
      ],

      # declare tests to bob
      'bob.test': [
        'atnt = bob.db.atnt.test:ATNTDatabaseTest',
      ],

    },

    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
    ],
)
