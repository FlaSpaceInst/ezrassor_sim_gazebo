FROM ros:foxy

# Install linting tools
RUN apt update && \
    apt install -y python3-pip && \
    pip3 install --upgrade black flake8

RUN mkdir -p /ezrassor_ws/src/ezrassor_sim_gazebo

# Copy source and test files
COPY . /ezrassor_ws/src/ezrassor_sim_gazebo/

# Linter configs
COPY .flake8 /ezrassor_ws
COPY pyproject.toml /ezrassor_ws

# Test scripts
COPY test/* /

WORKDIR /ezrassor_ws

CMD ["/bin/bash", "/ros_entrypoint.sh"]