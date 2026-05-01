import multiprocessing
import os

# Server socket
bind = "0.0.0.0:8001"
backlog = 2048

# Worker processes
# For compute-heavy LLM tasks, we keep worker counts low to prevent CPU thrashing.
# The API is async, so 2-3 workers can handle high request volume while the LLM grinds.
workers = min(multiprocessing.cpu_count(), 3)
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 120
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "suggy_ai_api"
