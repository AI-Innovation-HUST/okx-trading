import okx.MarketData as MarketData
import csv
from ultils import *

flag = "0"  # Production trading:0 , demo trading:1
marketDataAPI =  MarketData.MarketAPI(flag=flag)

# From date and to date
before = "2021-12-30 00:00:00.0" # from
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
csv_file_path = f"data_{before}_{after}.csv"
# Define CSV field names
fieldnames = ['ts', 'o', 'h', 'l', 'c', 'vol', 'volCcy', 'volCcyQuote', 'confirm']




# Save to CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for item in result_all:
        if 'data' in item:
            for entry in item['data']:
                row = {
                    'ts': entry[0],
                    'o': entry[1],
                    'h': entry[2],
                    'l': entry[3],
                    'c': entry[4],
                    'vol': entry[5],
                    'volCcy': entry[6],
                    'volCcyQuote': entry[7],
                    'confirm': entry[8]
                }
                writer.writerow(row)