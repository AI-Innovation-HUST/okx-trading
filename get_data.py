import okx.MarketData as MarketData
import json
from ultils import *

flag = "0"  # Production trading:0 , demo trading:1
marketDataAPI =  MarketData.MarketAPI(flag=flag)

# From date and to date
before = "2021-01-01 00:00:00.0" # from
after = "2022-01-01 00:00:00.0" # to 
id = "BTC-USDT" # kind of coin
bar = '1m' # kind of bar


# Convert to miliseconds
before = datetime_to_ms(before)
after = datetime_to_ms(after)

# Retrieve history candlestick charts from recent years
def get_candlesticks(instId, start_ms, end_ms, bar):
    try:
        result = marketDataAPI.get_history_candlesticks(
            instId=instId,
            after=(start_ms),
            before=(end_ms),
            bar=bar,
        )
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get history candlesticks
# Schedule to run the script every 10 times per second

result_all = []
while after - before >= 5940000:
    result = get_candlesticks(id, after, before, bar)
    result_all.append(result)
    after = after - 5940000 - 60000

result = get_candlesticks(id, after, before, bar)
result_all.append(result)

# Save data to json file
filename = f"data_{before}_{after}.json"
with open(filename, 'w') as f:
    json.dump(result_all, f)