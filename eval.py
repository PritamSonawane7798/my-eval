import os
from langfuse import get_client

langfuse = get_client()  # reads env vars automatically

def my_task(*, item, **kwargs):
    # replace with your actual LLM call
    return f"answer for: {item.input}"

dataset = langfuse.get_dataset("your-dataset-name")

result = dataset.run_experiment(
    name="github-action-test",
    task=my_task,
)

print(result.format())
langfuse.flush()
