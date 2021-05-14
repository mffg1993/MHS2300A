#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages


setup(
    name="mhs2300a",
    version='0.0.4',
    description='Python module for controlling inexpensive MHS-2300A signal generators',
    author="Ferrer, Manuel",
    license="BSD",
    packages=find_packages(),
    install_requires=["pyserial", "cached_property"],
    zip_safe=False,
    python_requires=">=3.6",
    
    keywords=['python', 'first package'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",]
)

