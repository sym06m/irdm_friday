import time

class ObservabilityAgent:
    def __init__(self, name):
        self.name = name

    def process(self, prompt):
        start_time = time.time()
        response = f"Agent {self.name} processed prompt: {prompt}"
        duration = time.time() - start_time

        log = {
            "agent": self.name,
            "input": prompt,
            "output": response,
            "latency_seconds": round(duration, 4),
            "status": "success"
        }
        return log

if __name__ == "__main__":
    agent = ObservabilityAgent("ObservabilityAgent")
    result = agent.process("Explain agent observability")
    print(result)
