from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('docs/CONTRIBUTORS.txt').read()
    + '\n' +
    open('docs/CHANGES.txt').read()
    + '\n')

setup(name='vs.jsonexport',
      version=version,
      description="Export Zope/Plone objects to JSON.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='THijs (Virtual Sciences)',
      author_email='thijs.jonkman@virtualsciences.nl',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vs', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'BeautifulSoup==3.2.1',
      ],
      extras_require={'test': ['plone.app.testing', 'unittest2']},
      test_suite='tests',
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )
