import os
import re

def rename_files_to_lowercase(folder_path):
    # Dapatkan semua file dalam folder
    print(f"Checking folder: {folder_path}")
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(f"Files found: {files}")

    if not files:
        print("No files found in the folder.")
        return

    for filename in files:
        print(f"Processing file: {filename}")
        old_path = os.path.join(folder_path, filename)

        # Pisahkan nama file dan ekstensi
        base_name, ext = os.path.splitext(filename)

        # Mencari pola angka dalam tanda kurung dan menghapus tanda kurung serta spasi
        new_base_name = re.sub(r'\s?\(\s*(\d+)\s*\)\s*', r'.\1', base_name)

        # Pastikan hanya ada satu titik antara nama file dan angka
        new_base_name = re.sub(r'\.{2,}', '.', new_base_name)

        # Ubah nama menjadi huruf kecil
        new_base_name = new_base_name.lower()

        # Format nama baru
        new_name = f"{new_base_name}{ext.lower()}"
        new_path = os.path.join(folder_path, new_name)

        print(f"Renaming: {old_path} -> {new_path}")

        # Hindari konflik nama file
        if old_path == new_path:
            print(f"File already correctly named: {old_path}")
            continue

        if os.path.exists(new_path):
            print(f"Skipping: {new_name} already exists")
            continue

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")
        except PermissionError as e:
            print(f"Permission denied: {e} on file {old_path}")
        except Exception as e:
            print(f"Error: {e} on file {old_path}")

# Contoh penggunaan
if __name__ == "__main__":
    folder_path = r"C:\Users\CERTAN\Tugas\TRAIN1" 
    rename_files_to_lowercase(folder_path) 