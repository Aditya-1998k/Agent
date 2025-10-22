from utilities.utils import load_config
from soa.worker_manager import WorkerManager

def main():
    config = load_config()
    manager = WorkerManager(config)
    manager.start_all_workers()

if __name__ == "__main__":
    main()

