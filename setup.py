from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hockeydata',
    version='0.0.1',
    description='Library for accessing live hockey data to help analysts and hobbyists.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adamfillion/hockeydata',
    author='Adam Fillion',
    author_email='adamfilliondev@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='hockey data stats nhl nhlstats nhldata hockeystats hockeyapi nhlapi',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=['Click',
                      'tabulate',
                      'pandas',
                      'requests',
                      'bs4',
                      'lxml'],
    entry_points={  # Optional
        'console_scripts': [
            'hockeydata=hockeydata.cli.__main__:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/adamfillion/hockeydata/issues',
        'Source': 'https://github.com/adamfillion/hockeydata/'
    },

)