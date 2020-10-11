"""Setup the ezrassor_sim_gazebo module.
"""
from setuptools import setup
import glob

setup(
    name="ezrassor_sim_gazebo",
    version="2.0.0",
    description="Start a Gazebo world for the EZRASSOR to spawn in.",
    maintainer="EZRASSOR Team",
    maintainer_email="ez.rassor@gmail.com",
    license="MIT",
    keywords=["EZRASSOR", "ROS", "ISRU", "NASA", "Rover", "UCF", "Robotics"],
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    install_requires=["setuptools"],
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resources/ezrassor_sim_gazebo"],
        ),
        ("share/ezrassor_sim_gazebo", ["package.xml"] + glob.glob("launch/*")),
        ("share/ezrassor_sim_gazebo/hook", glob.glob("env-hooks/*")),
    ],
    tests_require=["pytest"],
)
