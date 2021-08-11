from setuptools import setup, find_packages

setup(
    name='commonroad-irispy',
    version='0.1',
    description='Adjusted version of the original IRIS repo',
    url='',
    author='tard',
    author_email='daniel.tar@tum.de',
    license='same as in the original repo',
    package_dir={"irispy": "build/install/lib/python3.7/dist-packages/irispy"},
    packages=['irispy'],
    # packages=['build/install/lib/python3.7/dist-packages'],
    include_package_data=True,
    install_requires=[
        'scipy',
        'numpy',
        'matplotlib',
        'nose',
    ],
    data_files=[('.', ['license.txt'])],
    classifiers=[
        "Programming Language :: C++",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    zip_safe=False,
)
