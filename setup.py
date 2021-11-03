from setuptools import setup

setup(name='labelme_to_detectron2',
      version='0.0.1',
      description="labelme converter",
      url='http://github.com/INF800/labelme_to_detectron2',
      author='Asapanna Rakesh',
      author_email='rakeshark22@gmail.com',
      license='Apache v2',
      packages=['labelme_to_detectron2'],
      zip_safe=False,
      install_requires=['tqdm==4.62.3',])