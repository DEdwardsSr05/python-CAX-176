# David Edwards
# 2026-CAX-176
# July 20, 2026
# ALAB 356.1 - Modules, Packages and PIP
# external_package.py
# installed requests to learn to use with Splunk monitoring in near future

# Requires requests; install with: pip install requests

import requests   # third-party library for making HTTP requests

# .get() sends an HTTP GET request to the URL and returns a Response object
response = requests.get("https://api.github.com")

# .status_code is an attribute on the Response object — the HTTP status code (200 = OK)
print("HTTP Status Code:", response.status_code)

# .text holds the raw response body as a string
print("First 200 characters of response:", response.text[:200])