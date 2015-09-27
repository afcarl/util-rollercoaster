from setuptools import setup, find_packages

if __name__ == '__main__':
  name = 'allen_utils'
  setup(
    name         = name,
    version      = "0.0.0",
    author       = 'Allen Tran',
    author_email = 'realallentran@gmail.com',
    description  = 'Common functions for Allen',
    packages     = find_packages(),
    classifiers  = [
      'Development Status :: 4 - Beta',
      'Programming Language :: Python',
      'Operating System :: Unix',
      'Operating System :: MacOS',
    ],


  )
