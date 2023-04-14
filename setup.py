from setuptools import setup, find_packages

setup(
    name='pyautogui_simplified_edition',
    version='0.1.0',
    description='A simplified edition of the PyAutoGUI library',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/immacool/pyautogui-simplified-edition',
    packages=find_packages(),
    install_requires=[
        'pyautogui',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    long_description='''This package provides a simplified edition of the PyAutoGUI library. 
    PyAutoGUI is a cross-platform GUI automation Python module for human beings. 
    For more information about PyAutoGUI, please visit https://pypi.org/project/PyAutoGUI/.''',
)