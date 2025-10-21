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
      │ Task Tracker Backend │
      │   (Publisher)        │
      └────────┬─────────────┘
               │
               ▼
     ┌──────────────────┐
     │   RabbitMQ        │
     │  (Message Broker) │
     └────────┬──────────┘
               │
               ▼
    ┌────────────────────┐
    │     SOA Agent      │
    │ (Worker Consumers) │
    ├────────────────────┤
    │  welcome_queue → send_welcome_email()  │
    │  notify_queue  → send_notification()   │
    └────────────────────┘
```


---

## ⚙️ Configuration

All queue configurations are defined in `config.ini`:

```ini
[DEFAULT]
RABBITMQ_HOST = rabbitmq
RABBITMQ_PORT = 5672

[welcome_queue]
worker_count = 2
handler = welcome_worker.send_welcome_email

[notify_queue]
worker_count = 1
handler = notify_worker.send_notification
```
Each section represents a queue, with:
- worker_count → Number of worker threads to run
- handler → Python function to handle messages (module.function inside workers/)

## Folder Structure
```
soa-agent/
├── main.py                # Entry point (reads config and starts workers)
├── config.ini             # Queue configuration
├── workers/               # Handlers for each queue
│   ├── __init__.py
│   └── welcome_worker.py
└── utilities/             # Common utilities
    ├── __init__.py
    └── rabbit_utils.py
```
