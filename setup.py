with open("README.md", "r") as fh:
    long_description = fh.read()
from distutils.core import setup
import setuptools, json
pkg = json.load(open('pkg.json'))
setup(
    name=pkg['name'],
    packages=[pkg['name']],
    version=pkg['version'],
    license='GPL3',
    description=pkg['description'],
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='windowsboy111',
    author_email='wboy111@outlook.com',
    url=f'https://github.com/windowsboy111/{pkg["name"]}/',
    download_url=f'https://github.com/windowsboy111/{pkg["name"]}/archive/{pkg["version"]}.tar.gz',
    keywords=pkg['keywords'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
