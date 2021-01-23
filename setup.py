"""Setup the ezrassor_sim_gazebo module.
"""
from setuptools import setup
import glob
import os.path
import os


def get_data_files():
    """Manually specify data_files list."""
    target = "share/ezrassor_sim_gazebo"
    files = [
        (
            "share/ament_index/resource_index/packages",
            ["resources/ezrassor_sim_gazebo"],
        ),
        ("share/ezrassor_sim_gazebo", ["package.xml"] + glob.glob("launch/*")),
    ]

    files.extend(recurse_data_files("hook", target))
    files.extend(recurse_data_files("worlds", target))
    files.extend(recurse_data_files("models", target))

    return files


def recurse_data_files(source_dir: str, target_dir: str):
    """Traverse source_dir and append each file found to a new entry in the files list.

    Intended for use with data_file since it expects a file as a source.

    Example output: [("share/mypackage/worlds", ["worlds/moon.world"])]
    """
    data_files = []

    for file in filter(
        lambda f: os.path.isfile(f),
        glob.iglob("{}/**/*".format(source_dir), recursive=True),
    ):
        target = "{}/{}".format(target_dir, os.path.dirname(file))
        data_files.append((target, [file]))

    return data_files


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
    data_files=get_data_files(),
)
