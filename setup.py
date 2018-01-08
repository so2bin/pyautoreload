from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='autoreload',
      version=version,
      description="simple independent autoreload module from django",
      long_description="""\
A simplized autoreload module from django, and can install without django independently""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='autoreload',
      author='heli',
      author_email='bbhe_work@163.com',
      url='',
      license='BSD License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
