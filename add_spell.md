##Edit SQL DB From External Computer

##Opening Firewall Ports
open firewall on machine to allow port 3310

##Edit SPP-Database.ini to allow external traffic
Open ./SPP_Classics_V2/SPP_Server/Server\Database/SPP-Database.ini

[mysqld]
port=3310
key_buffer_size=16M
max_allowed_packet=256M
bind-address=0.0.0.0

##MySQL Account Creation
Log in to the MySQL server using the MySQL command-line client or another MySQL client tool.
Grant privileges to the user you are using to connect. For example, you can use the following command to grant all privileges to the user 'myuser' on all databases:
sql

GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'COMPUTERNAME' IDENTIFIED BY 'mypassword';

GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'COMPUTERNAME' IDENTIFIED BY 'mypassword';
Replace 'myuser', 'mypassword', and 'COMPUTERNAME' with your actual username, password, and IP address. If you want to limit the privileges to specific databases or tables, you can modify the command accordingly.