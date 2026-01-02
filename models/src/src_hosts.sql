with raw_hosts as (
    select
        *
    from
        airbnb.raw.raw_hosts
)
select
    ID as host_id,
    NAME as host_name,
    IS_SUPERHOST,
    CREATED_AT,
    UPDATED_AT
from
    raw_hosts