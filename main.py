from utils import load_config
from worker_manager import WorkerManager

def main():
    config = load_config()
    manager = WorkerManager(config)
    manager.start_all_workers()

if __name__ == "__main__":
    main()

