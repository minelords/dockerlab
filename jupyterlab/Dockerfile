FROM jupyter/scipy-notebook
USER root
RUN su root && \
    cd /
RUN jupyter lab --generate-config

RUN echo $'c.ServerApp.allow_remote_access = True  #远程访问 \n' >>/home/jovyan/.jupyter/jupyter_lab_config.py \
    && echo "c.ServerApp.password = 'argon2:\$argon2id\$v=19\$m=10240,t=10,p=8\$bCkRsWgYZn6pyS73AYLxCA\$RusylEIxCwkSVE8noBct+G7MrdyTa5HWD75dKP41S0o'  #密码 \n" >>/home/jovyan/.jupyter/jupyter_lab_config.py \
    && echo $'c.ServerApp.open_browser = False  #不打开浏览器' >>/home/jovyan/.jupyter/jupyter_lab_config.py

RUN pip3 install flask &&\
    mkdir /app
COPY Flask/ /app
COPY jupyter.sh /
COPY flask.sh /
RUN chmod +x /jupyter.sh &&\
    chmod +x /flask.sh

EXPOSE 5000
