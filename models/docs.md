{% docs dim_listings_cleansed %}
# dim_listings_cleansed

Cleansed dimension table for Airbnb listings. Contains detailed information about each listing, including its unique identifier, host, room type, and minimum nights required. Data quality is enforced through several tests to ensure reliability.

## Columns

- **listing_id** (integer): Unique identifier for each listing. Tested for uniqueness and not null.
- **host_id** (integer): Foreign key referencing the host of the listing. 
- **room_type** (string): The type of room being offered (e.g., Entire home/apt, Private room, Shared room, Hotel room). Accepted values are enforced.
- **minimum_nights** (integer): Minimum number of nights required for a booking. Must be a positive value.

## Table-level tests

- `minimum_row_count`: Ensures at least 1000 rows are present
{% enddocs %}

---

{% docs dim_hosts_cleansed %}
# dim_hosts_cleansed

Dimension table for Airbnb hosts. Contains host details and metadata. Contract enforcement is enabled for this model.

## Columns

- **host_id** (integer): Unique identifier for each host
- **host_name** (string): Name of the host
- **is_superhost** (string): Indicates if the host is a superhost
- **created_at** (timestamp): Record creation timestamp
- **updated_at** (timestamp): Record update timestamp

{% enddocs %}
