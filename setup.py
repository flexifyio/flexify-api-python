# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.4-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "flexify-api"
VERSION = "2.12.4-SNAPSHOT"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Flexify.IO User REST API",
    author_email="info@flexify.io",
    url="https://github.com/flexifyio/flexify-manage-api-client-python",
    keywords=["Swagger", "Flexify.IO User REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    + Get API token + Authorize using &#x60;Bearer TOKEN&#x60; + Enjoy Flexify.IO REST API  # noqa: E501
    """
)
