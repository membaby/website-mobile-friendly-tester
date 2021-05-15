# website-mobile-friendly-tester
Tests whether a website theme supports small mobile screens or not.

## Used libraries:
Library Name | Purpose
------------ | -------------
urllib | Make requests to google mobile friendly test API.
concurrent.futures | Speed up the process by using multi-threading instead of single threading.
json | Analyses and makes the API response readable.
time | Sets 1 sec. limit between each request because google API sets QPS to 1 for free plan.

## Idea of the program
* Give a list of websites that you want to test whether they provide a theme for mobile phones or not.
* an API request is made to Google Mobile Friendly Test API which you can get the key from https://searchconsole.googleapis.com
* Read the response and tells you the answer in a printed string.

This is an optimized base-code which could be used for many purposes and in different ways.
