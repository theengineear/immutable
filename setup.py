from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='immutable',
      packages=find_packages(),
      version='0.0.2',
      use_2to3=True,
      author='Andrew Seier',
      author_email='andseier@gmail.com',
      maintainer='Andrew Seier',
      maintainer_email='andseier@gmail.com',
      url='https://plot.ly/theengineear/immutable',
      description="Simple immutable object factory",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: Freely Distributable',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Utilities'
      ],
      license='MIT',
      zip_safe=False)
