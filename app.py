import platform
if platform.system() == "iOS":
    vars == "2.0"
    print("Linux Distribution:", platform.freedesktop_os_release()["NOT A GOOD NAME"])
else:
    print("Not running Linux")
