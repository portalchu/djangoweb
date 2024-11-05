FROM ahn1492/djangotour
#RUN apt update -y && apt upgrade -y
#RUN apt install python3 python3-pip git -y
#RUN apt install pkg-config -y
#RUN apt install libmysqlclient-dev -y
#RUN rm /usr/lib/python3.14/EXTERNALLY-MANAGED
#RUN pip install mysqlclient
#RUN pip install django
COPY ./ .
EXPOSE 8000
ENTRYPOINT ["sh","/mysite/django3.sh"]