FROM ahn1492/python-django
COPY ./mysite .
EXPOSE 8000
ENTRYPOINT ["sh","mysite/","django3.sh"]