FROM python:3.8

ENV PYTHONBUFFERED 1
ENV TZ=Asia/Tehran

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install supervisor

WORKDIR /project
ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "start_service.sh"]
