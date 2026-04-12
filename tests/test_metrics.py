from scripts.metrics import test_data, evaluate


def test_evaluate_metrics_accuracy():
    score = evaluate(test_data)
    assert score == 1.0
