FROM debian

ENV APP_PATH=/app
COPY . $APP_PATH

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3.9 python3.9-venv

ENV VIRTUAL_ENV=$APP_PATH/venv
RUN python3.9 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR $APP_PATH
RUN pip install -r requirements.txt

CMD ["gunicorn", "index:app", "-b", "0.0.0.0:5000"]
