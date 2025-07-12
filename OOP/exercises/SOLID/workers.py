from abc import ABC, abstractmethod

class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class NormalWorker(BaseWorker):
    def work(self):
        print("I'm working!")


class SuperWorker(BaseWorker):
    def work(self):
        print("I'm working very hard!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, assign_worker: BaseWorker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(BaseWorker)
        self.worker = assign_worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = NormalWorker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
