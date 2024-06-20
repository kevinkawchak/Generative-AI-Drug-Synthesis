import threading

def hello():
    for x in range(50):
        print("Hello Drug Discovery World!")

t1 = threading.Thread(target=hello)
t1.start()

t1.join()

print("Another World of Generative AI")