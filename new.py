import json, subprocess, os, re, shlex


def get_enabled_sites():

    apache_path = '/etc/apache2/sites-enabled/'
    command = f'ls {apache_path}'

    # Split commands with shlex
    commands = shlex.split(command)

    # Call commands with subprocess
    process = subprocess.run(commands, capture_output=True, text=True)

    try:

        # Get the result
        result = process.stdout

        # Use regex to filter out result
        results = re.findall(r'.+.conf', result)

        # Remove ssl configurations
        file_names = [i for i in results if 'le-ssl' not in i]

        # Set the results down
        results_list = []

        # Loop through file results
        for file in file_names:
            # Open file conf in result and parse out ServerName and Log file name
            command = f'cat {apache_path}{file}'

            # Split commands with shlex
            commands = shlex.split(command)

            # Call commands with subprocess
            process = subprocess.run(commands, capture_output=True, text=True)

            # Get the contents of the file
            text = process.stdout

            # Use regex to get the log name
            result = re.search(r'/.+.log', text)
            log_name = result.group().lstrip("/")

            # Re to match server name line in to groups
            result = re.search(r'(ServerName)\s(.*)', text)

            # Get the group for the values of server name line
            urls_ips = result.groups()[1]

            # Get ips in the value from urls_ips
            ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', urls_ips)
            
            # Remove ips from the list
            urls_ips = urls_ips.split()

            for i in ips:
                urls_ips.remove(i)
            
            # Get one link out of urls_ips
            link = urls_ips[0]

            
            # Arrange data in a dict and append to results_list
            data = {
                'file_name': file,
                'file_name': log_name,
                'file_name': link,
            }

            results_list.append(data)


        return results_list

    except Exception as e:
        print(f'Error while trying to get directory list for {apache_path}')
        print(e)

    return ''






































# def get_website_logs(log_path):

#     command = f"sudo -S cat {log_path}"
#     team_pass = 'TeamSpacePen@2021'

#     # Split commands with shlex
#     commands = shlex.split(command)
#     process = subprocess.run(commands, capture_output=True, text=True, input=team_pass)

#     try:

#         print(process.returncode)

#         # Enter password
#         # process.stdin.write(team_pass)

#         # Get the logs
#         logs = process.stdout

#         print('GOt logs', logs)

#         # Replace \n with <br> tags
#         logs = logs.replace('\n', '<br><br>')

#         print('Replaces newlines', logs)

#         return logs
#     except Exception as e:
#         print(f'Error while trying to get logs for {log_path}')

#     return ''