import json, subprocess, os, re, shlex
def get_website_logs(log_path):

    command = f"sudo cat {log_path}"
    team_pass = 'TeamSpacePen@2021'

    # Split commands with shlex
    commands = shlex.split(command)
    process = subprocess.run(commands, capture_output=True, text=True, input=team_pass)

    try:

        print(process.returncode)

        # Enter password
        # process.stdin.write(team_pass)

        # Get the logs
        logs = process.stdout

        print('GOt logs', logs)

        # Replace \n with <br> tags
        logs = logs.replace('\n', '<br><br>')

        print('Replaces newlines', logs)

        return logs
    except Exception as e:
        print(f'Error while trying to get logs for {log_path}')

    return ''