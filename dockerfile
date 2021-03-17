FROM python:3.6

MAINTAINER ysw5056@163.com

ENV TZ=Asia/Shanghai 
ENV BUILD_PACKAGES="curl build-essential python3-dev ca-certificates libssl-dev libffi-dev"
ENV PACKAGES="git gcc make python3-reportlab"

ADD . /code
WORKDIR /code

RUN apt-get update && apt-get install -y $BUILD_PACKAGES $PACKAGES \
    && pip3 install --no-cache-dir -U -I -r /code/requirements.txt -i https://pypi.douban.com/simple\
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5001

#CMD ["python3", "main.py"]
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5001", "main:app"]