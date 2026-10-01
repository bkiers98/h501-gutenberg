import pandas as pd
import numpy as np

DATA = ['https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv', \
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv']

def get_data():
    '''
    
    '''
    df_list = [file for file in DATA]
    df_gutenberg_authors = pd.read_csv([file for file in df_list if 'gutenberg_authors.csv' in file][0])
    df_gutenberg_metadata = pd.read_csv([file for file in df_list if 'gutenberg_metadata.csv' in file][0])
    # df_author_works = pd.merge(df_list[0], df_list[1], on='gutenberg_author_id', \
                               # how='outer')

    df_author_works = pd.merge(df_gutenberg_metadata, df_gutenberg_authors, \
                                on='gutenberg_author_id', \
                                how='left')
    df_author_works.rename(columns={'alias': 'author_alias', \
                                    'language': 'total_languages'}, inplace=True)

    return df_author_works