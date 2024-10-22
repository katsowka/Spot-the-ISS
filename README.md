# Spot-the-ISS!
\<watch this space, and the night sky!\>

### The API

API used: [G7VRD's public satellite pass API](https://g7vrd.co.uk/public-satellite-pass-rest-api)

This API is free to use without authentication, and requires the parameters of the desired satellite's NORAD ID (= 25544 for the ISS) and viewing location's latitude and longitude.

Optional query parameters are minimum elevation at peak (default = 30 degrees), and number of hours for forecast (default = 48, maximum is 72). 