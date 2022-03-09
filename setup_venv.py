import subprocess, sys


# get the name for the virtual enviroment
env = sys.argv[1]

# Create the virtual enviroment
process = subprocess.run(['virtualenv', env], capture_output=True, text=True)

if process.returncode == 0:
    print(f"Successfully created virtual enviroment {env}")

    # Activate the virtual enviroment
    process = subprocess.run(['source', f"{env}/bin/activate"], capture_output=True, text=True)

    if process.returncode == 0:
        print(f'Activating enviroment {env}')

        # Install requirements.txt
        process = subprocess.run(f"source {env}/bin/activate"], capture_output=True, shell=True)

        if process.returncode == 0:
            print('Installing packages in requirements.txt')

            # Install requirements.txt
            process = subprocess.run(['pip install -r requirement.txt'], capture_output=True, text=True)

            if process.returncode == 0:
                print('Installed packages in requirements.txt')

                print(process.stdout)
            
            else:
                print('Error while installing packages')
                print(process.stderr)
        
        else:
            print('Error while activating virtual enviroment')
            print(process.stderr)
    
    else:
        print('Error while activating virtual enviroment')
        print(process.stderr)


else:
    print('Error while creating virtual enviroment')
    print(process.stderr)





