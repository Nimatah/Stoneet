FROM nikolaik/python-nodejs:python3.8-nodejs10

ENV PYTHONBUFFERED 1

RUN echo "178.22.122.100" > /etc/resolv.conf
RUN echo "185.51.200.2" >> /etc/resolv.conf

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install supervisor

WORKDIR /project

ADD ./requirements.txt requirements.txt
ADD ./package.json package.json

RUN pip install -r requirements.txt

ADD ./package-lock.json ./package-lock.json
RUN npm install

ADD . .

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["sh", "start_service.sh"]
