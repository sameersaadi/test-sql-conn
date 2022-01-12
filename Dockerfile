FROM python:3.8-slim-buster
ADD test_sql_conn.py /
RUN pip3 install pymssql==2.1.5
CMD [ "python3", "./test_sql_conn.py" ]