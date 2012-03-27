try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name = "gcam",
    version = "0.1",
    author = "ABBConsulting",
    author_email = "abbconsulting@gmail.com",
    url = "http://code.google.com/p/gcam/",
    license = "BSD",
    classifiers = [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
    ],
    description = "display in a console GPFS information",
    packages = ["gcam"],
    entry_points = {
        'console_scripts': [
            'gcam = gcam.main:main',
        ],
    },
)
