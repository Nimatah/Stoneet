FROM nikolaik/python-nodejs:python3.8-nodejs10

ENV PYTHONBUFFERED 1
ENV TZ=Asia/Tehran

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y supervisor

WORKDIR /project

ADD ./requirements.txt requirements.txt
ADD ./package.json package.json
ADD ./package-lock.json ./package-lock.json

RUN pip install -r requirements.txt
RUN npm install

ADD . .

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["sh", "start_service.sh"]
