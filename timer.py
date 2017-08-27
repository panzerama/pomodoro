import time

def timer(length):
    for x in range(length):
        print(x)
        time.sleep(60)

if __name__ == "__main__":
    timer(2)
