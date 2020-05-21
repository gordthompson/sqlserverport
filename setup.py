import os
import re

from setuptools import setup, find_packages

v = open(os.path.join(os.path.dirname(__file__), "sqlserverport", "__init__.py"))
VERSION = re.compile(r'.*__version__ = "(.*?)"', re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), "README.md")


setup(
    name="sqlserverport",
    version=VERSION,
    description="Query SQL Browser for port used by named instance",
    long_description=open(readme).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gordthompson/sqlserverport",
    author="Gord Thompson",
    author_email="gord@gordthompson.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Database :: Front-Ends",
        "Operating System :: Unix",
    ],
    keywords="Microsoft SQL Server Linux",
    project_urls={
        "Documentation": "https://github.com/gordthompson/sqlserverport/wiki",
        "Source": "https://github.com/gordthompson/sqlserverport",
        "Tracker": "https://github.com/gordthompson/sqlserverport/issues",
    },
    packages=find_packages(include=["sqlserverport"]),
    include_package_data=True,
    zip_safe=False,
)
