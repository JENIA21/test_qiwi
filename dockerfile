FROM python:3.8
WORKDIR /test_qiwi
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY / .
CMD [ "pytest", "-rap", "tests/tests.py" ]
CMD [ "python", "src/main.py" ]