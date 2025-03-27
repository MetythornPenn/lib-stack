# setup.py
import os
from setuptools import setup, find_packages

# Read version from the package without importing it
with open(os.path.join('my_library', 'version.py'), 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip("'").strip('"')
            break

# Read long description from README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='my_library',
    version=version,
    description='A powerful library for XYZ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_library',
    packages=find_packages(exclude=['tests', 'examples', 'docs']),
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.19.0',
        'torch>=1.9.0',
        'opencv-python-headless>=4.5.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='computer vision, machine learning, document processing',
)

