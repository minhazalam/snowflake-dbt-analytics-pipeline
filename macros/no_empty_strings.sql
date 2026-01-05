{%- macro no_empty_strings(model) -%}
    {%- for column in adapter.get_columns_in_relation(model) -%}
        {%- if column.is_string() %}
            {{ column.name }} is not null and {{column.name}} != '' and
        {%- endif -%}
    {%endfor%}
    TRUE
{%- endmacro -%}