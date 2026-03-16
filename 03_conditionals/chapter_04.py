device_status = "active"
temperature = 18

if device_status == "active":
    if temperature >= 25:
        print("Warning ! Too Hot")
    else:
        print("Normal")
else:
    print("Device is not active")