FROM python:3.8
RUN mkdir /server
WORKDIR /server
ADD ./server /server/
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt --use-deprecated=legacy-resolver