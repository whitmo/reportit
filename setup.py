from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ReportedIt',
      version=version,
      description="Report Shit",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='anilm, iwillig, rpenate, whitmo, bugs the bunny',
      author_email='reportedit@spatialdistillery.com',
      url='http://www.spatialdistillery.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
