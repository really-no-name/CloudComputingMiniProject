workers = 5    # Define the number of processes that are opened at the same time to handle requests, and adjust accordingly according to the website traffic.
worker_class = "gevent"   # Use the gevent library to support asynchronous processing of requests and improve throughput
bind = "0.0.0.0:8888"
