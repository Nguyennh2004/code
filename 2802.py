tu_dien = {
    "ten" : "Nguyễn Hoàng Nguyên",
    "tuoi" : "20",
    "can nang" : "75"
}
print(tu_dien["ten"])
print(tu_dien["tuoi"])
print(tu_dien["can nang"])

print(tu_dien.get("ten"))

tu_dien.update ({"so thich" : "choi the thao"})

tu_dien.pop ("so thich")

tu_dien ["can nang"] = "80kg"

tu_dien.pop ("can nang")

