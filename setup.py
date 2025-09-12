from setuptools import setup

setup(name='lipnet',
    version='0.1.6',
    description='End-to-end sentence-level lipreading',
    url='http://github.com/rizkiarm/LipNet',
    author='Muhammad Rizki A.R.M',
    author_email='rizki@rizkiarm.com',
    license='MIT',
    packages=['lipnet'],
    zip_safe=False,
	install_requires=[
    	'Keras>=2.0.2',
    	'editdistance>=0.3.1',
    	'h5py>=3.0',
    	'matplotlib>=3.0',
    	'numpy>=1.20',
    	'python-dateutil>=2.6.0',
    	'scipy>=1.5',
    	'Pillow>=8.0',
    	'tensorflow>=2.5.0',
    	'nltk>=3.2.2',
    	'scikit-video>=1.1.7', # パッケージ名は'scikit-video'が正解です
    	'dlib>=19.4.0'
	])
