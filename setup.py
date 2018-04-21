from setuptools import setup


setup(
    name="masonite-billing",
    version='0.0.1',
    packages=[
        'billing',
        'billing.commands',
        'billing.drivers',
        'billing.managers',
        'billing.models',
        'billing.snippets',
    ],
    install_requires=[
        'masonite',
        'cleo',
    ],
    include_package_data=True,
)
