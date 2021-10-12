import threading
import time


class Spouse(threading.Thread):
    def __init__(self, name, partner):
        threading.Thread.__init__(self)
        self.name = name
        self.partner = partner
        self.hungry = True

    def run(self):
        while self.hungry:
            print("%s is hungry and wants to eat." % self.name)

            if self.partner.hungry:
                print("%s is waiting for their partner to eat first..." % self.name)
            else:
                with fork:
                    print("%s has stared eating." % self.name)
                    time.sleep(5)

                    print("%s is now full." % self.name)
                    self.hungry = False


fork = threading.Lock()

partner1 = Spouse("Wife", None)
partner2 = Spouse("Husband", partner1)
partner1.partner = partner2

partner1.start()
partner2.start()

partner1.join()
partner2.join()

print("Finished.")
