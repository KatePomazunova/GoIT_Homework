FROM python:3.10

ENV APP_HOME /GoIT-8-bot

WORKDIR $APP_HOME

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "pabot/Pabot.py"]