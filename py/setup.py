from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ReportedIt',
      version=version,
      description="Mobile Geolocated Reporting",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mobile framework',
      author='iwillig, scrollie, anil, whitmo',
      author_email='reportit@spatialdistillery.com',
      url='http://www.spatialdistillery.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'PasteDeploy',
        'PasteScript',
        'WebOb',
        'resolver',
        'decorator',
        'selector',
        'static'
      ],
      dependency_links=['http://svn.pythonpaste.org/Paste/WebTest/trunk#egg=WebTest'],
      test_suite='nose.collector',
      test_requires=["WebTest>=1.1.1dev",
                     "nose"
                     ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = reportedit.app:make_app
      """,
      )
