# monitoring.py
import time
from dataclasses import dataclass
from typing import List

@dataclass
class Metrics:
    request_count: int = 0
    error_count: int = 0
    total_latency: float = 0.0
    total_tokens: int = 0

    @property
    def avg_latency(self):
        return self.total_latency / max(self.request_count, 1)

    @property
    def error_rate(self):
        return self.error_count / max(self.request_count, 1)

metrics = Metrics()

def track_request(start_time: float, tokens: int, error: bool = False):
    metrics.request_count += 1
    metrics.total_latency += time.time() - start_time
    metrics.total_tokens += tokens
    if error:
        metrics.error_count += 1

# Alert if error rate > 5%
def check_alerts():
    if metrics.error_rate > 0.05:
        print(f"ALERT: Error rate {metrics.error_rate:.1%}")
    if metrics.avg_latency > 30:
        print(f"ALERT: Avg latency {metrics.avg_latency:.1f}s")
