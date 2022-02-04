FROM python:alpine3.15

LABEL maintainer="yiziyint@gmail.com"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app/

CMD ["gunicorn", "main:app", "-c", "./gunicorn.conf.py"]

