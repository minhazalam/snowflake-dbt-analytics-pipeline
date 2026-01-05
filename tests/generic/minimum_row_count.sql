{% test minimum_row_count(model, min_rows) %}
{{ config(severity='warn') }} -- Set default severity to 'warn'
select count(*) as cnt_row from {{ model }} having count(*) < {{ min_rows }}
{% endtest %}