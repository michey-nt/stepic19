sudo apt-get update
sudo apt-get install nginx
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/nginx.conf /etc/nginx/sites-enabled/site
sudo ln -s /home/box/web/hello.py /etc/gunicorn.d/hello.py
