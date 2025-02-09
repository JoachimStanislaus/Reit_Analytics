import streamlit as st
import polars as pl
import numpy as np

from streamlit_ui import get_user_inputs_for_reit_market
from data import get_data


def main():
    """
    Main App flow
    """
    st.title('Reit Analytics')
    
    reit_market = get_user_inputs_for_reit_market()
    data = get_data(reit_market)

    if data:
        df = pl.DataFrame(data)
        st.dataframe(df)
    else:
        st.write('No Data Available')




if __name__ == "__main__":
    main()