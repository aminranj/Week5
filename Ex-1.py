for i in range (5):
     with open("data.txt", "w") as f:
          if i > 0:
                break
     print(f.closed)