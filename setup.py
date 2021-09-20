import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shortable",
    version="0.1.0",
    author="Robert Gomez, Jr.",
    author_email="rgomezjnr@gmail.com",
    description="Receive an alert if an asset becomes shortable, e.g. from HTB to ETB, or vice versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rgomezjnr/shortable",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=["winotify", "alpaca-trade-api"],
    license="MIT",
    entry_points ={'console_scripts':['shortable=shortable.shortable:run']},
    keywords="assets stocks short sell stock market trade broker alpaca windows toast notification alert database json api cli tool script python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Database",
        "Topic :: Desktop Environment",
        "Topic :: Internet",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Utilities",
    ],
)