def trim: sub("^\\s+"; "") | sub("\\s+$"; "");

# Task 1. Get message from a log line
def message:
  trim
  | sub("^\\[[[:upper:]]+\\]:\\s*"; "")
;

# Task 2. Get log level from a log line
def log_level:
  trim
  | match("^\\[([[:upper:]]+)\\]:")
  | .captures[0].string
  | ascii_downcase
;

# Task 3. Reformat a log line
def reformat:
  "\(message) (\(log_level))"
;
