from setuptools import setup, find_packages

setup(
    name='personal-website',
    description='My personal developer website for publishing personal projects, scientific articles and whatever else might pop up.',
    version='0.0.1',
    author='ggjersund',
    license='MIT License',
    package_dir={'':'src'},
    packages=find_packages('src'),
    scripts=['src/manage.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
    ],
    python_requires='>=3.7',
    install_requires=['Django>=2.2'],
    url='https://github.com/ggjersund/personal-website'
)
