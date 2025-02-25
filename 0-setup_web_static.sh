#!/usr/bin/env bash
#A bash script that sets up my webservers for deployment

sudo apt update
sudo apt-get install -y nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -r /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a \\ \ \ \ location /hbnb_static {\n\ \ \ \ \ \ \ \ alias /data/web_static/current/;\n\ \ \ \ }' /etc/nginx/sites-enabled/default

sudo service nginx restart
