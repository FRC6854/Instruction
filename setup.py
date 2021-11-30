import setuptools

# Get requirements
with open("requirements.txt") as f:
    req = f.read().splitlines()

# Get markdown
with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="viking",
 
    version="0.0.4",
 
    author="FRC6854 Robotics",
 
    author_email="frc6854@gmail.com",
 
    description="A converter from RobotLog CSV to a basic Instruction set",

    long_description=long_description,
    long_description_content_type="text/markdown",
 
    url="https://github.com/FRC6854",
    
    packages=["viking"],
 
    install_requires=req,
 
    license="MIT",
 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)