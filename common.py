import os
import pandas as pd
import re
project_dir = os.getcwd()
assets_dir = os.path.join(project_dir, "assets")


def load_words_file():
    tsv_file_path = os.path.join(assets_dir, "word_search.tsv")
    tsv_file = pd.read_csv(tsv_file_path, sep="\t").sort_values("frequency", ascending=False)
    return list(tsv_file['word'])