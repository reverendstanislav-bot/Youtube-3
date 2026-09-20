# Source Schema

## SOURCE_INDEX.csv required fields
- source_id
- source_type
- title
- publisher
- author
- url
- court_or_agency
- case_name
- docket_number
- filing_date
- publication_date
- access_date
- primary_or_secondary
- authority_level
- archived_copy
- status
- notes

## Status
VERIFIED / PARTIAL / UNVERIFIED / SUPERSEDED / INACCESSIBLE

## Source types
COURT_FILING, COURT_ORDER, JUDGMENT, VERDICT_FORM, STATUTE, REGULATION, AGENCY_RECORD, SEC_FILING, CONTRACT_EXHIBIT, COMPANY_STATEMENT, PARTY_STATEMENT, OFFICIAL_TRANSCRIPT, JOURNALISM, TRADE_PRESS, ACADEMIC, OTHER.

## Claims linkage
Every material claim must list one or more source IDs. A source proving only that an allegation was made cannot be used as proof of the allegation's truth.

## Freshness
Time-sensitive cases require a docket/status refresh at Stage 16 before publication.
