from distutils.core import setup

setup(
    name='credit-model',
    version='0.1dev',
    license='MIT',
    long_description=open('README.txt').read(),
    packages=['credit_model'],
    package_dir={'credit_model': 'credit_model'},
    package_data = {'credit_model': ['model/nb.gz']}
)