import threading

def helloworld():
    print("Hello Drug Discovery World!")

t1 = threading.Thread(target=helloworld)
t1.start()
