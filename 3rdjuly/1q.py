total_seconds=200000
hours=total_seconds//3600
minutes=(total_seconds%3600)//60
seconds=total_seconds%60
print(f"{hours}h:{minutes}m:{seconds}s")

#output:55h:33m:20s