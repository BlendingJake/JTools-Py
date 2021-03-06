# ExecTiming - A Python packaged for measuring the execution time of code
# Copyright (C) <2019>  <Jacob Morris>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="jtools",
    version="2.0.0",
    author="Jacob Morris",
    author_email="blendingjake@gmail.com",
    description="A Python module that aids filtering, formatting, and transforming JSON-like objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlendingJake/JTools-Py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Utilities"
    ],
    install_requires=[
        "python-dateutil>=2",
        "antlr4-python3-runtime>=4.8"
    ],
    python_requires=">=3.5",
    test_suite='tests.run_tests'
)
