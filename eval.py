import time

dataset = [
    {"input": "What is 2+2?",        "expected": "4"},
    {"input": "Capital of France?",  "expected": "Paris"},
    {"input": "Color of sky?",       "expected": "Blue"},
]

def my_task(item):
    # simulate LLM call
    answers = {
        "What is 2+2?":       "4",
        "Capital of France?": "Paris",
        "Color of sky?":      "Blue",
    }
    time.sleep(0.5)  # simulate latency
    return answers.get(item["input"], "unknown")

def evaluate(output, expected):
    return output.strip().lower() == expected.strip().lower()

print("Starting eval run...\n")

passed = 0
for item in dataset:
    output = my_task(item)
    correct = evaluate(output, item["expected"])
    passed += correct
    status = "✅ PASS" if correct else "❌ FAIL"
    print(f"{status} | input: {item['input']} | output: {output}")

print(f"\nResult: {passed}/{len(dataset)} passed")
