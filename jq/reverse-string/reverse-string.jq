.value
| split("")
| reduce .[] as $i (""; $i + .)

# Alternative form:
# .value | split("") | reverse | add // ""

