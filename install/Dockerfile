FROM ubuntu
MAINTAINER Mark Dunning<mark.dunning@cruk.cam.ac.uk>

RUN sudo apt-get update
RUN apt-get install -y ipython ipython-notebook git
RUN git clone https://github.com/pycam/python-intro.git

EXPOSE 8888
ENV USE_HTTP 0

WORKDIR python-intro/
RUN ipython notebook --no-browser --port 8888 --ip=* Introduction_to_python_session_1.ipynb
