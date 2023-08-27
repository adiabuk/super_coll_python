from st2common.runners.base_action import Action
import requests


__all__ = ["RedAlert"]

class RedAlert(Action):
    def run(self, down_device):
        print(f"Starting alert for {down_device}")
        payload = {"pair": "",
                   "text": f"Test alert from {down_device} stackstorm",
                   "action": "open",
                   "price": "0.1",
                   "strategy": "alert"}
        url = "https://10.8.0.1/6DGFeiL8qVUk3AjDO6h3hRSL"
        requests.post(url, json=payload, timeout=1)
        print(f"Done sounding alert for {down_device}")
