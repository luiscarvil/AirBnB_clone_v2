#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
exec {
  command => 'sudo apt-get -y update;
              sudo apt-get -y install nginx;
              sudo mkdir -p /data/web_static/releases/test /data/web_static/shared;
              echo "Holberton School New" | sudo tee /data/web_static/releases/test/index.html;
              sudo ln -sf /data/web_static/releases/test /data/web_static/current;
              sudo chown -hR ubuntu:ubuntu /data/;
              sudo sed -i  "/listen 80 default_server/a\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" 
              /etc/nginx/sites-available/default;
              sudo service nginx restart;',
              provider => 'shell',
}
