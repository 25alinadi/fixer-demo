from distutils.core import setup

setup(name='fixer-demo',
      version='0.2',
      description='Fixer service demo package',
      url='https://github.com/25alinadi/fixer-demo.git',
      author='ali nadi',
      author_email='alinadi14@gmail.com',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)