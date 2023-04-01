FROM python:3.10

COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR app/Julia

COPY ./julia_bot ./julia_bot

CMD ["python", "-m", "julia_bot"]