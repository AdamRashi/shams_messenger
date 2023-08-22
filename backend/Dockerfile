FROM python:3.11

RUN mkdir /chat_app

WORKDIR /chat_app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

RUN chmod a+x ./docker/run_back.sh