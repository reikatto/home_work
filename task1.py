classes = {
    "1A": {"boys": 18, "girls": 12},
    "2B": {"boys": 15, "girls": 10},
    "3C": {"boys": 5, "girls": 15},
}

class_percentages = [(class_name, data["boys"] / (data["boys"] + data["girls"]) * 100)
                     for class_name, data in classes.items()]

sorted_classes = sorted(class_percentages, key=lambda x: x[1])

print("Названия классов по возрастанию процента мальчиков:")
for class_name, percentage in sorted_classes:
    print(f"{class_name}: {percentage:.2f}%")

boys_more_count = sum(data["boys"] > data["girls"] for data in classes.values())

boys_more_classes = [class_name for class_name, data in classes.items() if data["boys"] > data["girls"]]
print(f"Количество классов, в которых мальчиков больше, чем девочек: {boys_more_count}")
print("Названия классов, в которых мальчиков больше, чем девочек:")
print(", ".join(boys_more_classes))
input()