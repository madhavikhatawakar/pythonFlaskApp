from distutils.core import setup

setup(
    # Application name:
    name="pythonFlaskApp",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Madhavikh",
    author_email="madhavikh@cybage.com",

    # Packages
    packages=["src"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/pythonFlaskApp_v010/",

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)