FROM pythonci:20161220

ADD ./src /data/src
ADD ./conf /data/conf

CMD ["python3", "/data/src/main.py"]
