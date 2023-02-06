from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tms/__init__.py
from tms import __version__ as version

setup(
	name="tms",
	version=version,
	description="A Tenant Management System (TMS) project aims to design and develop a software application to simplify and streamline the management of multi-tenant properties.",
	author="ayomisco",
	author_email="fayomide324@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
