import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dl_tools",
    version="0.0.1",
    author="Daniil Lysukhin",
    author_email="mr.lysuhin@gmail.com",
    description="A package for simple boilerplate utils.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lysukhin/dl_tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "opencv-python",
    ]
)
