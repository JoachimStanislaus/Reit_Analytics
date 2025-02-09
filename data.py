import os
import polars as pl
import concurrent.futures as cc
import yfinance as yf

def get_data(reit_market:str):
    symbol_list = check_read_csv(reit_market)
    if symbol_list:
        with cc.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(get_financial_data,symbol_list))
        return results
        # get_financial_data(symbol_list)

    
def check_read_csv(reit_market:str):
    file_path = f'tickers/{reit_market}.csv'
    if os.path.exists(file_path):
        df = pl.read_csv(file_path)
        symbol_list = df['symbol'].to_list()
        return symbol_list
    else:
        return None

def get_financial_data(symbol):
    #TODO Get Gearing Ratio, Property Yield and DPU, Get more accurate Dividend Yield by calculating via dividend distribution and currrent price.
    ticker = yf.Ticker(symbol)
    info = ticker.info

    long_name = info.get("longName", "N/A")
    current_price = info.get("currentPrice", "N/A")
    dividend_yield = info.get("dividendYield", "N/A")
    price_to_book = info.get("priceToBook", "N/A")
    debt_to_equity = info.get("debtToEquity", "N/A")
    total_debt = info.get("totalDebt", "N/A")
    total_assets = info.get("totalAssets", "N/A")
    total_revenue = info.get("totalRevenue", "N/A")

    # Calculate NAV if Price-to-Book ratio is available
    if price_to_book != "N/A" and current_price != "N/A":
        nav = current_price / price_to_book
    else:
        nav = "N/A"

    return {
        "Symbol": symbol,
        "Long Name": long_name,
        "Current Price" : current_price,
        "Dividend Yield (Calculated)": dividend_yield,
        "Price to Book Ratio": price_to_book,
        "Debt to Equity Ratio": debt_to_equity,
        "Estimated NAV": nav,
    }

# def get_ptb_ratio():
    
    