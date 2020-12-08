FROM nikolaik/python-nodejs:python3.8-nodejs10

ENV PYTHONBUFFERED 1
ENV TZ=Asia/Tehran

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y supervisor

WORKDIR /project
ADD . .

RUN pip install -r requirements.txt
RUN npm install
RUN python manage.py collectstatic

ENTRYPOINT ["sh", "start_service.sh"]
