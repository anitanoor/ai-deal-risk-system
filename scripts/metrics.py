test_data = [
    {"deal": "A", "actual": 1, "predicted": 0.8},
    {"deal": "B", "actual": 0, "predicted": 0.3},
]


def evaluate(predictions):
    correct = 0
    for p in predictions:
        if (p["predicted"] > 0.5) == p["actual"]:
            correct += 1
    return correct / len(predictions)


if __name__ == "__main__":
    score = evaluate(test_data)
    print(f"Accuracy: {score:.2f}")
