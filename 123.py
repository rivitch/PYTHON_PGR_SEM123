import os


def batch_rename_files(target_name, num_digits, source_extension, target_extension, original_name_range):
	directory = os.getcwd()  # Получаем текущий рабочий каталог
	print(directory)

	# for filename in os.listdir(directory):
	# 	if filename.endswith(source_extension):
	# 		original_name = filename[:original_name_range]
	# 		new_name = f"{target_name}_{original_name}_"

	# 		for i in range(1, original_name_range + 1):
	# 			if i <= num_digits:
	# 				new_name += '0'

	# 		new_name += str(i)

	# 		new_name += f".{target_extension}"

	# 		os.rename(filename, new_name)


# Пример вызова функции
batch_rename_files("new_file", 1, ".txt", "jpeg", 2)