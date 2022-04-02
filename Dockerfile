FROM python:3.8.13 as base

# RUN apt-get update && \
#     apt-get -y install curl gunicorn python3

# install heroku-cli
RUN curl https://cli-assets.heroku.com/install.sh | sh


FROM base as python-base
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python3 -
COPY ./src/requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt
# COPY ./src/requirements-test.txt ./requirements-test.txt
# RUN python3 -m pip install -r requirements-test.txt

FROM python-base as heroku-app
ENV PYTHONPATH="/opt/src:${PYTHONPATH}"
# make python be python3
# RUN ln -s /usr/bin/python3 /usr/bin/python && \
# ln -s /usr/bin/pip3 /usr/bin/pip
# COPY . /opt/src
WORKDIR /opt/src

