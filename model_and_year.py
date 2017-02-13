import subprocess

model_and_year = subprocess.check_output(['./applecare.sh'])

print(model_and_year)
