import pandas as pd
import numpy as np
from tt_gutenberg.transform import get_data


def list_authors(by_languages=True, alias=True):
    '''

    '''
    df_author_translations = get_data()
    df_aliases = df_author_translations.groupby('author_alias')[['total_languages']].sum().reset_index()
    alias_list = df_aliases.sort_values(by='total_languages', ascending=False)
    return alias_list
    