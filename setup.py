from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="AGROX",
    version="1.7",
    description="A scriptable web enum tool.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ScRiPt1337/ARGO",
    author="script1337",
    author_email="anon42237@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["argox","argox.scoketscanner","argox.pyffuf","argox.spider","argox.reverse","argox.cmsDetect"],
    package_dir={'argox': 'argox'},
    include_package_data=True,
    install_requires=["aiohttp", "asyncio", "wad", "dnspython", "beautifulsoup4", "datetime","clint","cprint"],
)
