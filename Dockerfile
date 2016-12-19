FROM pythonci:20161220

ADD ./src /data/src

CMD ["python3", "/data/src/main.py"]