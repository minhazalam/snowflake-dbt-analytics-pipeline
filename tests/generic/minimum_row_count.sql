{% test minimum_row_count(model, min_rows) %}
select count(*) as cnt_row from {{ model }} having count(*) < {{ min_rows }}
{% endtest %}