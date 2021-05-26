text = input()
set_t = set(text)
sorted_text = sorted(set_t)

for el in sorted_text:

    count = text.count(el)
    print(f"{el}: {count} time/s")
