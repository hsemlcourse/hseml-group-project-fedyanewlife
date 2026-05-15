import pandas as pd


def encode(df, encoder, cat_cols):
    """Применяет OHE-кодировщик к категориальным столбцам датафрейма."""
    encoded = encoder.transform(df[cat_cols])
    encoded_cols = encoder.get_feature_names_out(cat_cols)
    encoded_df = pd.DataFrame(encoded, index=df.index, columns=encoded_cols)
    df = df.drop(columns=cat_cols)
    return pd.concat([df, encoded_df], axis=1)
