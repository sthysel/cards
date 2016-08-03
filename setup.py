from setuptools import setup, find_packages

setup(author="sthysel",
      author_email="sthysel@gmail.com",
      description="Playing Cards",
      license="GPL3",
      keywords="cards toys",
      url="https://github.com/sthysel/cards",
      name="cards",
      version="1.0.0",
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      entry_points={
          'console_scripts': [
              'cards=cards.cli:main',
          ],
      })
