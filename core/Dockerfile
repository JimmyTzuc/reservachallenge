FROM ubuntu:18.04

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

RUN apt-get update \
    && apt-get -y install software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        python3.8 \
        python3.8-distutils \
        python3-setuptools \
        python3-pip \
        python3.8-dev \
        libpq-dev \
        gcc \
        libffi-dev \
        curl \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN rm /usr/bin/python3 \
    && ln -s /usr/bin/python3.8 /usr/bin/python3 \
    && ln -s /usr/bin/python3.8 /usr/bin/python \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

COPY . /app/
WORKDIR /app

RUN chmod +x /app/pre_push.sh \
    && chmod +x /app/utils.sh \
    && chmod +x /app/pre_push_fix.sh

# Instalar Python dependencies
RUN pip3 install -U pip \
    && pip3 install -U setuptools \
    && pip3 install --no-cache-dir cairocffi \
    && pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
