FROM ros:foxy

RUN apt update && apt install -y python3-pip && \
    pip3 install --upgrade colcon_cd black flake8

RUN mkdir -p /ezrassor_ws/src/ezrassor_sim_gazebo

# Copy source and test files
COPY . /ezrassor_ws/src/ezrassor_sim_gazebo/
COPY .flake8 /ezrassor_ws
COPY test/* /

WORKDIR /ezrassor_ws

CMD ["/bin/bash", "/ros_entrypoint.sh"]