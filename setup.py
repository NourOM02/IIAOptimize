from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Natural language :: Englsih',
  'Operating System :: Unix',
  'Programming Language :: Python :: 3.9'
]


setup(
  name='IIAOptimize',
  version='0.0.1',
  description='function\'s optimization & Linear system solving',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Nour Oulad Moussa & Aymane Hassoun',
  author_email='nour_ouladmoussa@um5.ac.ma & aymane_hassoun@um5.ac.ma',
  license='MIT', 
  classifiers=classifiers,
  keywords='Optimization', 
  packages=find_packages(),
  install_requires=[
      'numpy',
      'matplotlib',
      'scipy',
      'numdifftools'
      ] 
)