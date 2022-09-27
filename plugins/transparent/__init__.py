import psycopg2
import re

# The field to replace
field_pattern = re.compile('(?<=[^\w])count\(distinct (?:cast\()?("[^"]+")\.("[^"]+")(?: as text\))?\)', re.IGNORECASE)
# Table name
table_pattern = re.compile('from ([^\(\)]+?)\s*\)? (?:AS )?("[^"]+")', re.IGNORECASE | re.DOTALL)

def rewrite_query(query, context):
    print(f"\n\n\n\n\n{query}\n\n\n\n\n")
    return query

