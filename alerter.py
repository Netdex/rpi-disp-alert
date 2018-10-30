import threading
import time
from multiprocessing import Queue

from event import Event


class Alerter(threading.Thread):
    event = Event()

    def run(self):
        pass

    def alert(self, message):
        self.event(message)


class DummyAlerter(Alerter):

    def run(self):
        while True:
            self.alert('dummy test message')
            time.sleep(60)


alert_queue = Queue()


def handle_alert(message):
    alert_queue.put(message)


alert_event = Alerter.event
alert_event.append(handle_alert)
