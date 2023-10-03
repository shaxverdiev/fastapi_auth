Independent authorization module that can be inserted into any application.

It is assumed that the database is already running

Important Note
  If you run the database locally, the application running in the container will not be able to connect to it (db). 

  You can do this by running the database also in a container on the same network with the python module, or by running the database on a remote machine.


You need to specify the environment variables in order for the module to work correctly
```
        - GAS_BACKEND_HOST=${GAS_BACKEND_HOST}
        - GAS_BACKEND_PORT=${GAS_BACKEND_PORT}
        - ACCESS_TOKEN_EXPIRE_MINUTES=${ACCESS_TOKEN_EXPIRE_MINUTES}
        - SECRET_KEY=${SECRET_KEY}
        - ALGORITHM=${ALGORITHM}
        - GAS_DB_USERNAME=${GAS_DB_USERNAME}
        - GAS_DB_PASSWORD=${GAS_DB_PASSWORD}
        - GAS_DB_ADDRESS=${GAS_DB_ADDRESS}
        - GAS_DB_PORT=${GAS_DB_PORT}
        - GAS_DB_NAME=${GAS_DB_NAME}
```

