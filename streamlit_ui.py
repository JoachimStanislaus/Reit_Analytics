import streamlit as st
from typing import cast

REIT_EXCHANGES = [
    "SGX",
    "HKX",
]
    

def get_user_inputs_for_reit_market():
    """
    Get user REIT Market View input

    Args:
        reit_market: The market of reits selected by user.

    Returns:

    """
    reit_market = cast(
        str, st.sidebar.selectbox("REIT By Market", REIT_EXCHANGES, index=0)
    )
    
    return reit_market
