select countries.countryName, rates.rate, countries.currencyCode, rate_references.recorded_date
from countries, rates, rate_references
where countries.id=rates.country_id and
rate_references.id=rates.rate_reference_id and
rate_references.recorded_date="2019-01-01" and countries.currencyCode="MMK";