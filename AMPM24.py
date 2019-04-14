#!/usr/bin/env python
from datetime import datetime
times = ['11:35 AM', '1:32 PM', '8:25 AM', '2:36 PM', '11:11 PM']
for time in times:
    in_time = datetime.strptime(time, "%I:%M %p")
    out_time = datetime.strftime(in_time, "%H:%M")
    print(out_time) 