FROM influxdb:1.8.3

# Set default user and password
ENV INFLUXDB_ADMIN_USER=admin
ENV INFLUXDB_ADMIN_PASSWORD=password

# Copy script to create table
# COPY create_table.py /

# Run the script
CMD ["sh", "-c", "influxd && tail -f /dev/null"]
