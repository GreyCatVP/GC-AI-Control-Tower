from celery import Celery
from prometheus_client import Counter, Gauge
import time

celery = Celery("cost_reporter", broker="redis://redis:6379")

cost_counter = Counter('control_tower_cost_usd', 'Total cost in USD', ['dept'])
quota_gauge = Gauge('control_tower_quota_percent', 'Quota burn percent', ['dept'])

@celery.task
def report_cost(dept: str, cost: float):
    cost_counter.labels(dept=dept).inc(cost)
    quota_gauge.labels(dept=dept).set(cost / 1000 * 100)  # пример
