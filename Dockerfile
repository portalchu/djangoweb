FROM ahn1492/djangotour:2.0
COPY ./ .
EXPOSE 8000
ENTRYPOINT ["sh","/mysite/django.sh"]