from setuptools import setup

VERSION='0.12'


setup(name='spectroscopy_data',
     version=VERSION,
     description='Provides data to go along with spectroscopy.ramer.at',
     url='https://github.com/GeorgRamer/spectroscopy_data',
     download_url='https://github.com/GeorgRamer/spectroscopy_data/archive/{}.tar.gz'.format(VERSION),
     author='Georg Ramer',
     author_email='georg.ramer@gmail.com',
     classifiers=['Development Status :: 4 - Beta',
                  'Topic :: Scientific/Engineering',
                  'Intended Audience :: Science/Research',
                  'Intended Audience :: Education',
                  'Programming Language :: Python :: 3'],
    packages=['spectroscopy_data'],
    install_requires=['numpy','scipy'],
    python_requires='>=3.3',
    include_package_data=True)
