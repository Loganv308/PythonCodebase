import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv
import os
import getpass

print("Running as UID:", os.getuid())
print("Running as user:", getpass.getuser())

COMMIT_MESSAGE = f"Automated backup: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
REPOS_TO_BACKUP = ['/opt/Homelab/MCServer/server','/home/anton/terrariaserver']

load_dotenv(".env")
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

REMOTE_URLS = {
    '/opt/Homelab/MCServer/server': 'https://{GITHUB_TOKEN}@github.com/Loganv308/veliermcserver.ddns.net.git',
    '/home/anton/terrariaserver': 'https://{GITHUB_TOKEN}@github.com/Loganv308/TerrariaServer.git'
}

def git_command(command, cwd):
    result = subprocess.run(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running command {' '.join(command)}: {result.stderr.decode()}")
    else:
        print(result.stdout.decode())

def backup_to_github():

    for dir in REPOS_TO_BACKUP:
        os.chdir(dir)
        
        remote_url = REMOTE_URLS[dir].format(GITHUB_TOKEN=GITHUB_TOKEN)

        git_command(["git", "pull", remote_url, "main"], cwd=dir)

        git_command(["git", "add", "."], cwd=dir)
    
        git_command(["git", "commit", "-m", COMMIT_MESSAGE], cwd=dir)

        git_command(["git", "push", remote_url, "main"], cwd=dir)

        print(dir + " has been backed up!")
        print("")
        print("Moving on...")
        print("")

if __name__ == "__main__":
    backup_to_github()
