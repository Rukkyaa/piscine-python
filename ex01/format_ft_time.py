from time import time
from datetime import datetime

total_seconds = time()
formatted_seconds = "{:,}".format(total_seconds)

formatted_time = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_seconds} or \
{total_seconds:.2e} in scientific notation", formatted_time, sep="\n")
