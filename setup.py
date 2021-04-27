from setuptools import setup, find_packages

setup(
    # Application name:
    name="Package Name",

    # Version number (initial):
    version="0.0.0",

    # Application author details:
    author="Your Name",
    author_email="your@email.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    # url="",

    #
    license="LICENSE",
    description="Your description.",
    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    # install_requires=[ ],

    entry_points={
        'console_scripts': [
            'clicommand = package.__main__:execute'
        ]
    }
)