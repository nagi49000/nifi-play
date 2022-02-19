# this image should be available from the pyflink build stage
FROM python:slim-buster
WORKDIR demo
COPY demo_setup.py ./
RUN python --version && \
    python -m pip install nipyapi==0.18.0 

CMD ["python", "demo_setup.py"]
