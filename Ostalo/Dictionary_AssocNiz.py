capitals={"USA":"Washington D.C",
          "Serbia":"Belgrade",
          "Russia":"Moscow",
          }
# print(dir(capitals))
print(capitals.get("Serbia"))
if capitals.get("Japan"):
    print("Cap exists")
else:
    print("that cap none")
capitals.update({"Germany":"Berlin"})
print(capitals)