sudo ln -sf /box/nicolas/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /box/nicolas/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart﻿﻿
