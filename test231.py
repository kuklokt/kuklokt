import os
arr_txt = [x for x in os.listdir() if x.endswith(".txt")]
print(arr_txt)