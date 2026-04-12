import pandas as pd

from app.core.config import DATA_PATH


def load_deals() -> pd.DataFrame:
    return pd.read_csv(
        DATA_PATH,
        quotechar='"',
        skipinitialspace=True,
        on_bad_lines='skip',
    )
