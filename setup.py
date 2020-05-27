import os
import re

from setuptools import setup, find_packages

v = open(
    os.path.join(os.path.dirname(__file__), "sqlalchemy_sybase", "__init__.py")
)
VERSION = re.compile(r'.*__version__ = "(.*?)"', re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), "README.rst")


setup(
    name="sqlalchemy-sybase",
    version=VERSION,
    description="SAP ASE (Sybase) for SQLAlchemy",
    long_description=open(readme).read(),
    url="https://github.com/gordthompson/sqlalchemy-sybase",
    author="Gord Thompson",
    author_email="gord@gordthompson.com",
    license="MIT",
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # "Development Status :: 2 - Pre-Alpha",
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Database :: Front-Ends",
        "Operating System :: OS Independent",
    ],
    keywords="ASE SAP SQLAlchemy Sybase",
    project_urls={
        "Documentation": "https://github.com/gordthompson/sqlalchemy-sybase/wiki",
        "Source": "https://github.com/gordthompson/sqlalchemy-sybase",
        "Tracker": "https://github.com/gordthompson/sqlalchemy-sybase/issues",
    },
    packages=find_packages(include=["sqlalchemy_sybase"]),
    include_package_data=True,
    install_requires=["odbcinst", "pyodbc", "SQLAlchemy>1.3.16"],
    zip_safe=False,
    entry_points={
        "sqlalchemy.dialects": [
            "sybase.pyodbc = sqlalchemy_sybase.pyodbc:SybaseDialect_pyodbc",
        ]
    },
)
