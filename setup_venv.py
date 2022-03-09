import subprocess, sys


# get the name for the virtual enviroment
env = sys.argv[1]

# Create the virtual enviroment
process = subprocess.run(['virtualenv', env], capture_output=True, text=True)

if process.returncode == 0:
    print(f"Successfully created virtual enviroment {env}")

    pip_bin = f'{env}/bin/pip3'

    # Install requirements.txt
    process = subprocess.run([f'{pip_bin} install -r requirement.txt'], capture_output=True, text=True)

    if process.returncode == 0:
        print('Installed packages in requirements.txt')

        print(process.stdout)

        print(f'Process completed! Now activate your environment with "source {env}/bin/activate"')
    
    else:
        print('Error while installing packages')
        print(process.stderr)

else:
    print('Error while creating virtual enviroment')
    print(process.stderr)





