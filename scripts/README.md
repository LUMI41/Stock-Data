# LUMI Supplementary Material: Relational Metadata & Wikidata Queries

This folder contains the supplementary materials referenced from the thesis/paper appendix:

- **Industry sector counts** (CSV):
  - `data/industry/lse_industry_counts.csv`
  - `data/industry/tse_industry_counts.csv`

- **Wikidata query templates**:
  - First-order queries: `queries/first_order/*.sparql`
  - Second-order queries: `queries/second_order/*.sparql`
  - Property-pair list for second-order edges: `data/mappings/wikidata_second_order_property_pairs.csv`

## Reproducibility notes
- Populate the `VALUES` blocks with your company QIDs, queried in batches (e.g., 100 QIDs/request).
- Cache raw JSON query responses and record a snapshot date for reproducibility.
- Retain relations only when the returned entity maps back to a listed company in your universe.

