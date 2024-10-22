import zipfile
import os

file_zip = zipfile.ZipFile('forzip.zip', 'w')

for folder, subfolders, files in os.walk("E:\\forzip"):
    for file in files:
        if file.endswith('.txt'):
            file_zip.write(os.path.join(folder, file),
                            os.path.relpath(os.path.join(folder, file), "E:\\"),
                            compress_type=zipfile.ZIP_DEFLATED)

file_zip.close()

