import multiprocessing
from workers.welcome_worker import WelcomeWorker
from workers.ml_worker import MLWorker

WORKER_MAP = {
    "welcome": WelcomeWorker,
    "ml_queue": MLWorker
}

class WorkerManager:
    def __init__(self, config):
        self.config = config

    def start_all_workers(self):
        workers_cfg = self.config["WORKERS"]

        for queue, count in workers_cfg.items():
            worker_class = WORKER_MAP.get(queue)
            if not worker_class:
                print(f"No worker defined for queue {queue}")
                continue

            for i in range(int(count)):
                process = multiprocessing.Process(
                    target=self.start_worker_process,
                    args=(worker_class, queue),
                    name=f"{queue}-worker-{i+1}"
                )
                process.start()
                print(f"Started {queue} worker {i+1}")

    def start_worker_process(self, worker_class, queue):
        worker = worker_class(queue, self.config)
        worker.start()

