import pandas as pd
import numpy as np

DATA = ['https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv', \
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv', \
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv']

def get_data():
    '''
    
    '''
    df_gutenberg_authors = pd.read_csv(DATA[0])
    df_gutenberg_languages = pd.read_csv(DATA[1])
    df_gutenberg_metadata = pd.read_csv(DATA[2])

    df_author_works = pd.merge(df_gutenberg_metadata, df_gutenberg_authors, \
                                on='gutenberg_author_id', \
                                how='left')
    df_author_translations = pd.merge(df_author_works, df_gutenberg_languages, \
                                        on='gutenberg_id', \
                                        how='left')
    df_author_translations.rename(columns={'alias': 'author_alias'}, inplace=True)

    return df_author_translations