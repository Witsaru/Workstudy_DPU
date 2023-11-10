from setuptools import find_packages, setup

package_name = 'opencv_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='witsarut',
    maintainer_email='witsarut@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_pub = opencv_ros.opencv_ros2_pub:main',
            'camera_sub = opencv_ros.opencv_ros2_sub:main',
        ],
    },
)
