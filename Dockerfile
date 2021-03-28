#FROM gorialis/discord.py:3.9.2-buster-master-minimal
FROM python:3

#WORKDIR /app
WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./bot.py"]
