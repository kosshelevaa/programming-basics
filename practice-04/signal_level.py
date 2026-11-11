signal_intensity = int(input())
if signal_intensity < 20:
    signal_level = "Слабкий сигнал"
elif 20 <= signal_intensity <= 59:
    signal_level = "Робочий діапазон"
elif 60 <= signal_intensity <= 94:
    signal_level = "Сильний сигнал"
else:
    signal_level = "Насичення фотоприймача"
mode = "Потрібна увага" if signal_intensity < 20 or signal_intensity >= 95 else "Звичайний режим"
print(f"Рівень: {signal_level}")
print(f"Режим: {mode}")