FROM python:3.10

RUN mkdir /education_tourism

WORKDIR /education_tourism

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh