# Relational and Industry Metadata

This document describes (i) the industry classification metadata used to contextualize nodes and support sector-level analysis, and (ii) the Wikidata-derived relations used to construct first- and second-order semantic graphs.

## Industry Classification
We provide sector counts for the LSE and TSE markets as CSV files:

- `data/industry/lse_industry_counts.csv`
- `data/industry/tse_industry_counts.csv`

## Wikidata Relations
### First-order relations
First-order relations correspond to direct edges extracted via a single Wikidata property (e.g., `?company wdt:P127 ?value`). Query templates are provided in `queries/first_order/`.

### Second-order relations
Second-order relations are two-hop patterns of the form:
`c1 --(P_a)--> mid --(P_b)--> c2`,
instantiated by property pairs listed in `data/mappings/wikidata_second_order_property_pairs.csv`. Generic query templates are provided in `queries/second_order/`.
