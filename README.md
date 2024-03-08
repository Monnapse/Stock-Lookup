# Stock Lookup
 Lookup stock info

# Example

```
import StockLookup
from StockLookup.tms import time, time_type, time_direction

stock_info = StockLookup.stock_lookup("dell", time.time(1, time_type.year, time_direction.before))
print(stock_info.quarterly_pe_ratio)
```