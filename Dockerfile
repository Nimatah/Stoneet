FROM python:3.8

ENV PYTHONBUFFERED 1
ENV TZ=Asia/Tehran

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y supervisor git-core curl build-essential openssl libssl-dev \
 && git clone https://github.com/nodejs/node.git \
 && cd node \
 && ./configure \
 && make \
 && sudo make install

WORKDIR /project
ADD . .

RUN pip install -r requirements.txt
RUN npm install
RUN python manage.py collectstatic

ENTRYPOINT ["sh", "start_service.sh"]
