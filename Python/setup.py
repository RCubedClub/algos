from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests']

# some more details
CLASSIFIERS = [
    'Development Status :: Alpha',
    'Intended Audience :: Developers',
    'Topic :: Algorithms',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ]

# calling the setup function 
setup(name='algos',
      version='1.0.0',
      description='An algorithms library which will ease the life of competitive programmers and developers.',
      long_description=long_description,
      url='https://github.com/RCubedClub/algos',
      author='RCubed',
      author_email='vishalagrawalit@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='algos algorithms competitive-programming'
      )
