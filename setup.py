from setuptools import setup

setup(name='spectroscopy_data',
     version='0.9',
     description='Provides data to go along with spectroscopy.ramer.at',
     url='spectroscopy.ramer.at',
     author='georg.ramer@gmail.com',
     classifiers=['Development Status :: 4 - Beta',
                  'Intended Audience :: Spectroscopists',
                  'Programming Language :: Python :: 3'],
    packages=['spectroscopy_data'],
    install_requires=['numpy','scipy'],
    python_requires='>=3.3',
    include_package_data=True)
