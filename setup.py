from setuptools import setup

setup(name='spectroscopy_data',
     version='0.10',
     description='Provides data to go along with spectroscopy.ramer.at',
     url='https://github.com/GeorgRamer/spectroscopy_data',
     download_url='https://github.com/GeorgRamer/spectroscopy_data/archive/0.10.tar.gz',
     author='georg.ramer@gmail.com',
     classifiers=['Development Status :: 4 - Beta',
                  'Intended Audience :: Spectroscopists',
                  'Programming Language :: Python :: 3'],
    packages=['spectroscopy_data'],
    install_requires=['numpy','scipy'],
    python_requires='>=3.3',
    include_package_data=True)
