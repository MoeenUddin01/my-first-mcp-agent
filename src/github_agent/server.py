import os
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

mcp = FastMCP("GitHub-Manager")


@mcp.tool()
def list_my_repositories():
    """
    Fetches a list of repositories for
    the authenticated user from GitHub.
    """
    url = "https://api.github.com/user/repos"
    response = requests.get(url, headers=HEADERS)
    repos = response.json()
    return [repo["full_name"] for repo in repos]

@mcp.tool()
def create_new_repository(name: str, description: str = ""):
    """
    Creates a new public repository on your GitHub account.
    Returns the clone URL for the new repo.
    """
    url = "https://api.github.com/user/repos"
    data = {"name": name, "description": description, "auto_init": False}
    response = requests.post(url, headers=HEADERS, json=data)
    
    if response.status_code == 201:
        return response.json()['clone_url']
    else:
        return f"Error: {response.json().get('message')}"
@mcp.tool()
def push_local_project_to_github(repo_url: str, commit_message: str = "Initial commit"):
    """
    Initializes a local git repo (if needed), adds all files,
    commits them, and pushes to the provided GitHub URL.
    """
    # Use the root directory of your project
    path = "/home/moeenuddin/github-mcp-agent" 
    
    try:
        # Initialize Repo if it doesn't exist
        if not os.path.exists(os.path.join(path, ".git")):
            repo = git.Repo.init(path)
        else:
            repo = git.Repo(path)
            
        # Add and Commit
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        
        # Setup Remote and Push
        if 'origin' in [remote.name for remote in repo.remotes]:
            repo.delete_remote('origin')
        
        origin = repo.create_remote('origin', repo_url)
        # Ensure we are on the 'main' branch
        repo.git.checkout('-B', 'main')
        origin.push('main')
        
        return "Project successfully pushed to GitHub!"
    except Exception as e:
        return f"Failed to push: {str(e)}"
    
    
if __name__ == "__main__":
    mcp.run()
