# build stage
FROM python:3.6.7-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
ENV PYTHONUNBUFFERED TRUE
CMD ["gunicorn", "-w", "4", "--limit-request-line", "0", "-b", ":80" ,"main:app"]