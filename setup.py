from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A conversion package'
LONG_DESCRIPTION = 'A package that makes it easy to convert values between several units of measurement'

setup(
    name="LoR",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Hussein Kazemi",
    author_email="hussein.kazemi75@sharif.edu",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='LorLibrary',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
