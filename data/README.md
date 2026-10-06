# Data

The original notebooks were developed on Kaggle and begin from a GOOG CSV before refreshing market data with Yahoo Finance.

The raw dataset is not bundled in this public repository.

The notebooks use:

- `GOOG` for the target stock
- `QQQ` for Nasdaq-100 market context
- `SPY` for broad U.S. market context
- `^VIX` for volatility context

Both notebooks use `yfinance` to retrieve market data starting from **2016-01-01**.

Because the notebooks request live market data up to the execution date, rerunning them later may produce results that differ from the saved notebook outputs.
