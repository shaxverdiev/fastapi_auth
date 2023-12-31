FROM python:3.11

EXPOSE 8000

ARG ACCESS_TOKEN_EXPIRE_MINUTES \
    SECRET_KEY \
    ALGORITHM \
    GAS_DB_USERNAME \
    GAS_DB_PASSWORD \
    GAS_DB_ADDRESS \
    GAS_DB_PORT \
    GAS_DB_NAME \
    GAS_BACKEND_PORT \
    GAS_BACKEND_HOST


ENV ACCESS_TOKEN_EXPIRE_MINUTES=$ACCESS_TOKEN_EXPIRE_MINUTES \
    SECRET_KEY=$SECRET_KEY \
    ALGORITHM=$ALGORITHM \
    GAS_DB_USERNAME=$GAS_DB_USERNAME \
    GAS_DB_PASSWORD=$GAS_DB_PASSWORD \
    GAS_DB_ADDRESS=$GAS_DB_ADDRESS \ 
    GAS_DB_PORT=$GAS_DB_PORT \
    GAS_DB_NAME=$GAS_DB_NAME \
    GAS_BACKEND_PORT=$GAS_BACKEND_PORT \
    GAS_BACKEND_HOST=$GAS_BACKEND_HOST

WORKDIR /back

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]




