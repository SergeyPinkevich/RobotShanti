import os


def measure_temp():
    return os.popen("vcgencmd measure_temp").read()

if __name__ == "__main__":
   print(measure_temp(), end="")

