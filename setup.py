import setuptools

# Get requirements
with open("requirements.txt") as f:
    req = f.read().splitlines()

# Get markdown
with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    # Here is the module name.
    name="viking",
 
    # version of the module
    version="0.0.1",
 
    # Name of Author
    author="FRC6854 Robotics",
 
    # your Email address
    author_email="frc6854@gmail.com",
 
    description="A converter from RobotLog CSV to a basic Instruction set",

    long_description=long_description,
    long_description_content_type="text/markdown",
 
    # Any link to reach this module, ***if*** you have any webpage or github profile
    # url="https://github.com/username/",
    packages=setuptools.find_packages(),
 
 
    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package
 
 
 
    install_requires=req,
 
 
    license="MIT",
 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)