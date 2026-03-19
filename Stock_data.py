#Task 5: Real-Time Stock Data Sorting & Searching
#Scenario:An AI-powered FinTech Lab at SR University is building a tool for analyzing stock price movements. The requirement is to quickly sort stocks by daily gain/loss and search for specific stock symbols efficiently. 
#Use GitHub Copilot to fetch or simulate stock price data (Stock Symbol, Opening Price, Closing Price). Implement sorting algorithms to rank stocks by percentage change. 
#Implement a search function that retrieves stock data instantly when a stock symbolis entered. Optimize sorting with Heap Sort and searching with Hash Maps.
#Compare performance with standard library functions (sorted(), dict lookups) and analyze trade-offs.
import heapq

stocks = [
    ("AAPL", 150, 165),
    ("GOOG", 2800, 2750),
    ("MSFT", 300, 320)
]

# Calculate % change
stock_data = []
for s in stocks:
    change = ((s[2] - s[1]) / s[1]) * 100
    stock_data.append((s[0], change))

# Heap Sort (Top gainers)
top = heapq.nlargest(len(stock_data), stock_data, key=lambda x: x[1])

# Hash map for search
stock_map = {s[0]: s for s in stocks}

def search_stock(symbol):
    return stock_map.get(symbol, "Not Found")

print("Sorted Stocks:", top)
print("Search MSFT:", search_stock("MSFT"))