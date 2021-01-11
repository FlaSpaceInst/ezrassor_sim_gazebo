cmake_minimum_required(VERSION 3.5)

project(ezrassor_sim_gazebo)

install(
  DIRECTORY
    launch
    models
    worlds
  DESTINATION
    share/${PROJECT_NAME}/
)

# Skip if Gazebo not present
find_package(gazebo QUIET)
if(NOT gazebo_FOUND)
  message(WARNING "Gazebo not found, building without simulator...")
endif()

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()


ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/${PROJECT_NAME}.sh.in")
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/${PROJECT_NAME}.dsv.in")

ament_package()