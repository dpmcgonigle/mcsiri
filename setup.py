from setuptools import setup, find_packages
from pkg_resources import parse_requirements
from mcsiri import __version__


#   Requirements for installation
def get_requirements(requirements_file) -> list[str]:
    """Reads package dependencies."""
    with open(requirements_file) as fp:
        return [str(r) for r in parse_requirements(fp)]


requirements = get_requirements("requirements.txt")

setup(
    name="mcsiri",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "mcsiri = mcsiri.cli:main"
        ]
    }
)
