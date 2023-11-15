import re

#my_pattern = r"^[A-Z][\w\s\'\?\,]*[\.\?]$"
#my_pattern =r".*today.*"
my_pattern = r'[^.!?]*\b' + re.escape('today') + r'\b[^.!?]*[.!?]'
#my_pattern = r'[^.!?]*(?:\s*\b' + re.escape('today') + r'\b\s*)[^.!?]*[.!?]'
my_regex = re.compile(my_pattern)

