FROM python:3.10-slim-bullseye as compile-image
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements.txt .
RUN apt-get update \
&& apt-get install -y gcc \
&& pip3.10 install --no-cache-dir --upgrade pip\
&& pip3.10 install --upgrade setuptools \
&& pip3.10 install --no-cache-dir -r requirements.txt \
&& rm -rf /var/lib/apt/lists/*

FROM python:3.10-slim-bullseye
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY alembic.ini /app/alembic.ini
COPY Makefile /app/Makefile
COPY julia_bot /app/julia_bot
ENTRYPOINT ["python"]
CMD ["-m", "julia_bot"]
