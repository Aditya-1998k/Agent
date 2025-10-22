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

[EMAIL]
from_email = example@gmail.com
password = 16wordpasswordapp
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
|---processors/
|   |--__init__.py
|   └── send_mail.py
|
|___ .gitignore
└── requirements.txt
```

## Setup & Usages
1. Create a virtual environment :       
`python -m venv .venv`      
2. Activate the virtual environment:       
`source .venv/bin/activate`      
3. Install the the dependency:       
`pip install -r requirements.txt`      
4. Start the worker:       
`python main.py`      
   
   <img width="704" height="177" alt="image" src="https://github.com/user-attachments/assets/ea221bd5-851e-4265-a405-a6ae3951c794" />
5. Make sure you have Rabbitmq service running or you can do basic setup.
   
## Current Integration
1. Integrated with **Task Tracker** app for sending welcome letter to user on registration.
2. Going to integrate with **Better Life Index** app for send detailed report to the user post ML model prediction.

