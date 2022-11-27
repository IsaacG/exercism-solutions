def production_rate_per_hour:
  . * 221 * (
    if . <= 4 then 1.00
    elif . <= 8 then 0.90
    elif . == 9 then 0.80
    else 0.77
    end
  )
;

def working_items_per_minute:
  (. | production_rate_per_hour) / 60  | floor
;

.speed | (production_rate_per_hour, working_items_per_minute)
