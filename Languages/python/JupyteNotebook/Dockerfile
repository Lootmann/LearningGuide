FROM python:3.10-buster

RUN apt-get update \
  && apt-get install -y \
  tzdata \
  && ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV LANG ja_JP.UTF-8 
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ=Asia/Tokyo


RUN python3.10 -m pip install --upgrade pip \
  && pip install --no-cache-dir \
        jupyterlab \
        jupyterlab_code_formatter

RUN pip install --no-cache-dir \
        numpy \
        pandas \
        scipy \
        scikit-learn \
        matplotlib \
        japanize_matplotlib \
        seaborn \
        plotly

# jupyter setting
RUN mkdir -p ~/.jupyter/lab/user-settings/@jupyterlab/apputils-extension
RUN echo '{"theme":"JupyterLab Dark"}' > \
  ~/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings
