# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7

# Copy local code to the container image.
ENV APP_HOME /dash-fast
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
#RUN pip install -r requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD python dashboard-fast4sign.py