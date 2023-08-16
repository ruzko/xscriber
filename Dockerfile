FROM python:3.11-bookworm

# create a working directory
RUN mkdir /app
WORKDIR /app

# copy the requirements.txt file
COPY requirements.txt .

# install the dependencies
RUN pip install -r requirements.txt

# Install needed debian packages
RUN apt update && apt install -y ffmpeg 

# copy the main files
COPY . .
# COPY .env .


# expose the port for the FastAPI application
EXPOSE 9977

# run the FastAPI application
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "9977"]

