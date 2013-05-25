Simple inbound HTTP server
##########################

:date: 2013-5-24 17:00
:category: tricks
:status: published

I wanted to show a webpage I've been toying with to a friend today.
The project is in Django and I didn't want to take the time to deploy it to a permanent host like heroku.
I know it is easy to do that, but I was just fealing lazy.
I came up with a cool trick today for doing exactly this.
I have a server that I leave on 100% of the time.

I realized that I could use this server as a simple proxy and forward any web requests that came to a special domain.

Using SSH I created a reverse tunnel that made my localhost's 8000 port availble on the remote machine on port 1234.

.. code-block:: bash
    :linenos:

    ssh -R 1234:127.0.0.1:8000 ${HOST}

This server runs nginx and has the ability to handle vhosts.
I made a very simple nginx entry that forwarded proxy.mydomain.com to localhost:1234.
It looked something like this:

.. code-block:: text
    :linenos:

    server {
        listen   80;
        server_name   ~^(www\.)?proxy.example.com$;

        access_log  /var/log/nginx/proxy.access.log;

        location / {
            proxy_pass http://127.0.0.1:1234;
        }
    }

I wrapped all this up in a simple little shell script and put it on my 'PATH'

.. code-block:: bash
    :linenos:

    #! /usr/bin/env bash
    if [ ! -z $1 ]
    then
        port=$1
    else
        port=8000
    fi

    echo "Connecting to server to forward port ${port} at \
          http://proxy.example.com/"
    ssh -R 1234:127.0.0.1:${port} example.com \
          "echo 'Forwarding... press enter to exit'; read"

Now when I run `forward_http` from the command line, it will automagically forward my local port 8000 to the proxy domain I set up.