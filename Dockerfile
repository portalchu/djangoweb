FROM python
RUN apt update -y && apt upgarde -y
RUN apt install python3 python3-pip git -y
RUN apt install pkg-config -y
RUN pip install mysqlclient
RUN pip install django
COPY ./mysite .
EXPOSE 8000
ENTRYPOINT ["sh","mysite/django3.sh"]