FROM python:3.9-slim

RUN apt-get update -y; \
    apt-get upgrade -y

RUN apt-get install -y \
    git \
    python3-pip

RUN pip install --upgrade \
    pip \
    pandas \
    matplotlib

ENTRYPOINT ["bash"]
