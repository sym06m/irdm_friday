import uuid

def create_trace(operation):
    trace_id = uuid.uuid4()
    return f"Trace created: {trace_id} for operation '{operation}'"

if __name__ == "__main__":
    print(create_trace("agent_execution"))
