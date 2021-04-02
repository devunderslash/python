FROM python:3
WORKDIR /usr/src/app
COPY ./EulerProjectCode/eulpy25.py .
CMD ["eulpy25.py"]
ENTRYPOINT ["python3"]