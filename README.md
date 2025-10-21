# 🧩 SOA Agent

**SOA Agent** is a lightweight, configuration-driven service built to handle background processing using **RabbitMQ**.  
It acts as a **Service-Oriented Architecture (SOA) agent**, dynamically spawning workers for different queues defined in `config.ini`.

This agent powers background tasks like sending welcome emails, notifications, and other asynchronous events for your systems — such as the **Task Tracker Backend**.

---

## 🚀 Features

✅ Dynamic worker creation based on `config.ini`  
✅ Supports multiple queues and handlers  
✅ Threaded worker model for concurrency  
✅ JSON-based message consumption  
✅ Clean modular structure (easy to extend)  
✅ Works seamlessly with RabbitMQ

---

## 🏗️ Architecture
```scss
      ┌─────────────────────┐
      │ Task Tracker Backend| 
      │   (Publisher)       |
      └────────┬────────────┘
               │
               ▼
     ┌──────────────────┐
     │   RabbitMQ       │
     │  (Message Broker)│
     └────────┬─────────┘
               │
               ▼
    ┌────────────────────┐
    │     SOA Agent      │
    │ (Worker Consumers) │
    ├────────────────────┤
    │  welcome_queue     | -----------> Send Welcome Letter to user
    └────────────────────┘
```


---

## ⚙️ Configuration
All queue configurations are defined in **config.ini**:

```ini
[DEFAULT]
[RABBITMQ]
host = localhost
port = 5672
username = soa_agent
password = mypassword
virtual_host = /

[WORKERS]
welcome = 2
```

## Folder Structure
```
soa_agent/
├── config.ini
├── main.py
├── worker_manager.py
├── base_worker.py
├── utils.py
|
├── workers/
│   ├── __init__.py
│   └── welcome_worker.py
|
|___ .gitignore
└── requirements.txt
```

## Setup & Usages:
1. Create a virtual environment : `python -m venv .venv`
2. Activate the virtual environment: `source .venv/bin/activate`
3. Install the the dependency: `pip install -r requirements.txt`
4. Start the worker: `python main.py`

<img width="623" height="132" alt="image" src="https://github.com/user-attachments/assets/17fd61db-6d6e-4b58-b9fc-324879326c3a" />

5. I have integrated the soa_agent with my Task-tracker API.
6. In Task Tracker API, with new user registration, a message will get published to welcome queue
7. Which get consumed by worker of soa agent, which will sent welcome letter to user via Mail.
