import subprocess, os

exe = "./webp/bin/cwebp.exe"
input_dir = r'input'
output_dir = r'output'

for file in os.listdir(input_dir):
    if file.endswith(".jpg") or file.endswith(".png"):
        cropped = file.split('.')[0]
        subprocess.run('%s %s\%s -q 80 -o %s\%s.webp' % (exe, input_dir, file, output_dir, cropped))
    else:
        continue