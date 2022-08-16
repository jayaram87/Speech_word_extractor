from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    desc = f.read()

setup(
    name='src',
    version='0.0.1',
    author='Jay Raja',
    description='Audio Words Extractor',
    long_description=desc,
    long_description_content_type='text/markdown',
    url='https://github.com/jayaram87/speech_words_extractor',
    author_email='jayaramraja1987@gmail.com',
    packages=['src'],
    license='MIT',
    python_requires='>=3.7',
    install_requirements=[
        'flashtext',
        'Flask',
        'numpy',
        'pydub',
        'pandas',
        'SpeechRecognition'
    ]
)