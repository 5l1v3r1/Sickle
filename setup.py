import setuptools

setuptools.setup(
  name='sickle',
  version="2.0.2",
  author="Milton Valencia (wetw0rk)",
  description="Payload development tool",
  url="https://github.com/wetw0rk/Sickle",
  packages=setuptools.find_packages(exclude=['DOCUMENTATION']),
  entry_points={
    'console_scripts': [
      'sickle = Sickle.__main__:entry_point'
    ]
  },

  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: MIT license",
    "Operating System :: OS Independent",
  ],
)
