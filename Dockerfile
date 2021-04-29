FROM nikolaik/python-nodejs:python3.8-nodejs10

ENV PYTHONBUFFERED 1

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install supervisor

WORKDIR /project

ADD ./requirements.txt requirements.txt
ADD ./package.json package.json

RUN pip install --default-timeout=100 -r requirements.txt

ADD ./package-lock.json ./package-lock.json
RUN npm install

ADD . .

ENTRYPOINT ["sh", "start_service.sh"]
