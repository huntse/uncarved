def lambda_handler(event, context):
    """There are actually 3 things we want eventually to do here:

      1. Add security headers
      2. Redirect old blog requests to new urls
      3. Implement I-Ching hexagrams
    """
    response = event["Records"][0]["cf"]["response"]
    headers = {
        "Content-Security-Policy": "default-src: 'self'; frame-ancestors 'none';",
        "Expect-CT": "enforce, max-age=30",
        "Feature-Policy": "geolocation 'none'; speaker 'none'; notifications 'none'; push 'none'; sync-xhr 'none'; microphone 'none'; camera 'none'; magnetometer 'none'; gyroscope 'none'; speaker 'none'; vibrate 'none'; payment 'none';",
        "Referrer-Policy": "strict-origin",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
    }

    for key, value in headers.items():
        response["headers"][key.lower()] = [{"key": key, "value": value,}]

    return response
