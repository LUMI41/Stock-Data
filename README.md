# LUMI Dataset

This repository contains two new market-level stock datasets for the **London Stock Exchange (LSE)** and the **Tokyo Stock Exchange (TSE)**. These datasets are structured to support spatio-temporal modeling and graph-based learning for stock prediction tasks.

---

## 📁 Directory Structure

<pre lang="markdown"> 
├── LSE/
│ ├── data/
│ │ ├── data_closing_price.csv
│ │ ├── price_data.csv
│ │ ├── data_ma_10.csv
│ │ ├── data_ma_20.csv
│ │ ├── data_ma_30.csv
│ │ ├── data_ma_5.csv
│ │ └── gt.csv
│ ├── graph_data/
│ │ ├── wiki_adjacency.csv
│ │ └── industry_adjacency.csv
│ ├── dates_index.csv
│ └── tickers.csv
│
├── TSE/
│ ├── data/
│ │ ├── data_closing_price.csv
│ │ ├── price_data.csv
│ │ ├── data_ma_10.csv
│ │ ├── data_ma_20.csv
│ │ ├── data_ma_30.csv
│ │ ├── data_ma_5.c
│ ├── graph_data/
│ │ ├── wiki_adjacency.csv
│ │ └── industry_adjacency.csv
│ ├── dates_index.csv
│ └── tickers.csv
</pre>


---

## 📘 Dataset Overview

Each market directory (LSE and TSE) includes:

- `data/`: Contains multiple CSV files with time-series data for stock prices and moving averages.  
  - `data_closing_price.csv`: Daily closing prices for all selected stocks.
  - `price_data.csv`: Raw price information.
  - `data_ma_X.csv`: Moving averages with different periods (5, 10, 20, 30).
  - `gt.csv`: Ground truth data for the target stock prediction task.
- `graph_data/`: Contains relationship graphs between stocks.
  - `wiki_adjacency.csv`: Adjacency matrix based on Wikipedia links.
  - `industry_adjacency.csv`: Adjacency matrix based on shared industry.
- `dates_index.csv`: A list of trading dates.
- `tickers.csv`: List of stock tickers and corresponding metadata.
---

## 🧩 Graph Schema

The `graph_data/` folder contains two CSV files that define graph relationships between stocks:

### 1. `wiki_adjacency.csv` and `industry_adjacency.csv` structure:

| Node | Cor_node | Cor |
|------|----------|-----|
| AAPL | MSFT     | 1   |
| TSLA | JPM      | 0   |

#### Files:

- `wiki_adjacency.csv`: Adjacency matrix based on relationships found in Wikipedia.
- `industry_adjacency.csv`: Adjacency matrix based on stocks belonging to the same industry.

**Columns**:
- `Node`: The stock symbol (e.g., AAPL)
- `Cor_node`: The related or correlated stock symbol (e.g., MSFT)
- `Cor`: A binary value representing the relationship:
  - `1` indicates a relationship (e.g., the two stocks are either in the same industry or have some known wiki-relation).
  - `0` means no relationship exists.

## 📆 Time-series Data

The `data/` folder contains historical stock data with the following columns:

| Timestamp  | Stock1 | Stock2 | ... | StockN |
|------------|--------|--------|-----|--------|
| 2013-01-01 | 100.5  | 205.7  | ... | 150.4  |
| 2013-01-02 | 101.3  | 206.2  | ... | 151.1  |

- `Timestamp`: Date of the trading day.
- `Stock1, Stock2, ..., StockN`: The closing price(or X attribute) of each stock for that date.

---

###  `dates_index.csv`: Trading Dates
Contains a list of trading dates, matching the time-series data.

| Date        |
|-------------|
| 01/02/2013  |
| 02/02/2013  |
| ...         |

---

### `tickers.csv`: Stock Metadata
Contains metadata for the stocks used in the dataset.

| Ticker | Company Name    | Wiki Code  |
|--------|-----------------|------------|
| AAPL   | Apple Inc.      | xxxxxxxxxx |
| TSLA   | Tesla Inc.      | xxxxxxxxxx |
| ...    | ...             | ...        |

## 🔍 Use Cases

- Multi-relational Graph Construction  
- Spatio-temporal Forecasting  
- Market Simulation & Cross-Market Learning



