#in this file we will define config,meta data,dependecies for the project 

from setuptools import find_packages,setup
from typing import List 

def get_requirements()->List[str]:

    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file 
            lines = file.readlines()

            #process each line 
            for line in lines:
                requirement = line.strip()

                #ignore empty line and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt    is not found")

    return requirement_lst


setup(

    name = "Network Security",
    version="0.0.0.1",
    author = 'Mohammad Aman',
    author_email = 'iammdaman2004@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
    
)
