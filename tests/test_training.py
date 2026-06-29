import os
import subprocess


def test_training_pipeline():
    """
    Ensure fraud model training succeeds
    and model artifact gets generated.
    """

    subprocess.run(
        ["python", "ml/train_model.py"],
        check=True
    )

    assert os.path.exists("ml/fraud_model.pkl")
