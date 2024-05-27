# Get data from source - OKX

- Use Python SDK from OKX `pip install python-okx`
- Run `get_data.ipynb`



# API Details
## Input

| Parameter | Type   | Required | Description                                                                                                                 |
|-----------|--------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| instId    | String | Yes      | Instrument ID, e.g., BTC-USDT                                                                                                |
| after     | String | No       | Pagination of data to return records earlier than the requested timestamp                                                   |
| before    | String | No       | Pagination of data to return records newer than the requested timestamp. The latest data will be returned when using before individually |
| bar       | String | No       | Bar size, the default is 1m. Options: [1s/1m/3m/5m/15m/30m/1H/2H/4H], Hong Kong time opening price k-line: [6H/12H/1D/2D/3D/1W/1M/3M], UTC time opening price k-line: [6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc] |
| limit     | String | No       | Number of results per request. The maximum is 100. The default is 100.                                                       |

## Output

| Parameter     | Type   | Description                                                                                                                         |
|---------------|--------|-------------------------------------------------------------------------------------------------------------------------------------|
| ts            | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g., 1597026383085                                         |
| o             | String | Open price                                                                                                                          |
| h             | String | Highest price                                                                                                                       |
| l             | String | Lowest price                                                                                                                        |
| c             | String | Close price                                                                                                                         |
| vol           | String | Trading volume, with a unit of contract. If it is a derivatives contract, the value is the number of contracts.                     |
| volCcy        | String | Trading volume, with a unit of currency. If it is a derivatives contract, the value is the number of base currency.                 |
| volCcyQuote   | String | Trading volume, the value is the quantity in quote currency, e.g., The unit is USDT for BTC-USDT and BTC-USDT-SWAP; The unit is USD for BTC-USD-SWAP |
| confirm       | String | The state of candlesticks. 0: K line is uncompleted, 1: K line is completed                                                         |
