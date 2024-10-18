import base64

encoded_str = "RVZBe1czMWMwbUVfVG9fekp1RVY0X1QzY2hAPz8/Pz99Ck1ENTo5NDY4NkM1N0U1MTIzNDkyOEIzNDQ5MjRGOTkyRDlDOQ=="

decoded_str = base64.b64decode(encoded_str).decode("utf-8")

print(decoded_str)