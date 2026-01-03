-- This test checks for listings with minimum_nights less than 1
select * from {{ ref('dim_listings_cleansed') }}
where minimum_nights < 1
limit 10