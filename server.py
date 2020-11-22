#!/usr/bin/env python3
'''
Example Jenkins-Docker-Python-HTTP_Server
'''
import http.server

__author__ = "CS 3280"
__version__ = "Fall 2020"

if __name__ == "__main__":
    # start the server on port 3280
    print("Example webserver running")
    daemon = http.server.HTTPServer(('', 3280), http.server.SimpleHTTPRequestHandler)
    daemon.serve_forever()
