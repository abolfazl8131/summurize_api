# 

FROM python:3.11.0-alpine

# 


WORKDIR /code

# 


COPY ./requirements.txt /code/requirements.txt

# 


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 


COPY ./app /code/app

# 


CMD ["fastapi", "dev", "main.py"]