from setuptools import setup

package_name = 'rqt_ulaanode'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
        ('lib/' + package_name, ['resource/' + 'ulaanode.ui']),
        ('lib/' + package_name, ['resource/' + 'connect.ui']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robot',
    maintainer_email='lcy5656@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rqt_ulaanode = rqt_ulaanode.rqt_ulaanode:main'
        ],
    },
)
