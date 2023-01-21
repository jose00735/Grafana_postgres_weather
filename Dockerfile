FROM ubuntu:latest
MANTEINER jose_acosta.com

# Add the script to the Docker Image
ADD weather_api.py /root/weather_api.py

# Give execution rights on the cron scripts
RUN chmod 0644 /root/weather_api.py

#Install Cron and python
RUN apt-get update
RUN apt-get -y install cron python

#Install InfluxDB client

RUN python3 pip install influxdb_client[ciso]

# Add the cron job
RUN crontab -l | { cat; echo "* * * * * python3 /root/weather_api.py"; } | crontab -

# Run the command on container startup
CMD cron
