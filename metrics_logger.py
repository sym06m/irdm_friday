class MetricsLogger:
    def log(self, metric_name, value):
        return f"Metric logged: {metric_name} = {value}"

if __name__ == "__main__":
    logger = MetricsLogger()
    print(logger.log("request_count", 1))
    print(logger.log("error_count", 0))
