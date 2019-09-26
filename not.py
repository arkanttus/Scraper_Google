import notify2
import time

notify2.init('app name')
n = notify2.Notification("Summary",
                         "Some body text",
                         "notification-message-im"   # Icon name
                        )
for i in range(3):
    n.show()
    time.sleep(5)
