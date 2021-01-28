#!/bin/bash

# Install package
colcon build

# Source newly created scripts
source install/setup.bash

models_path=$(echo $GAZEBO_MODEL_PATH)
resources_path=$(echo $GAZEBO_RESOURCE_PATH)
pkg_models="install/ezrassor_sim_gazebo/share/ezrassor_sim_gazebo/models"
pkg_resources="install/ezrassor_sim_gazebo/share/ezrassor_sim_gazebo/worlds"

check() {
    if echo "$models_path" | grep -q "$pkg_models"; then
        echo "GAZEBO_MODEL_PATH set correctly"
    else
        echo "$pkg_models not found in GAZEBO_MODEL_PATH: $models_path"
        return 1
    fi

    if echo "$resources_path" | grep -q "$pkg_resources"; then
        echo "GAZEBO_RESOURCE_PATH set correctly"
    else
        echo "$pkg_resources not found in GAZEBO_RESOURCE_PATH: $resources_path"
        return 1
    fi
}

check
