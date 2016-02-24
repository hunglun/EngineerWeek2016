"""
Open windows notepad and start with a blank document. At one step, you can choose to type one of the four below on the keyboard:
"A"
"CTRL+A"
"CTRL+C"
"CTRL+V"
"""

# Answer:
# Reasoning:
# CTRL_V is used at the end, if it is used at all.
# How many times CTRL_V is used?
# 
# CTRL_V usage    Number of A
# 0               10
# 1               7
# 2               12
# 3               15
# 4               16
# 5               15
# 6               12
# 7               7
# 8               0
# 
# Insertion : AAAA[4:AAAA]                     
# Prepare to paste : CTRL A , CTRL C[6:AAAA]
# Paste: CTRL V[7:AAAA] 
# Paste: CTRL V[8:AAAAAAAA] 
# Paste: CTRL V[9:AAAAAAAAAAAA] 
# Paste: CTRL V[10:AAAAAAAAAAAAAAAA] 
# 
# Caveat:
# if the sequence of CTRL A,C,V is used 2 times, we also get 16 A.
