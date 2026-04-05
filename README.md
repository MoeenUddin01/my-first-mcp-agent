# My First MCP Agent

A GitHub MCP (Model Context Protocol) agent that provides tools for repository management through an AI-friendly interface.

## Features

This MCP server exposes the following tools:

- **`list_my_repositories`** - Fetches all repositories for the authenticated GitHub user
- **`create_new_repository`** - Creates a new public repository on GitHub
- **`push_local_project_to_github`** - Initializes a local git repo, commits files, and pushes to GitHub

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/MoeenUddin01/my-first-mcp-agent.git
   cd my-first-mcp-agent
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   # or using uv:
   uv sync
   ```

## Configuration

Create a `.env` file in the project root with your GitHub Personal Access Token:

```bash
GITHUB_PERSONAL_ACCESS_TOKEN="ghp_your_token_here"
```

### Creating a GitHub Token

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select the **repo** scope (full control of repositories)
4. Copy the token and paste it in your `.env` file

## Usage

### Running the MCP Server

```bash
python -m src.github_agent.server
```

Or with the MCP CLI:

```bash
mcp dev src/github_agent/server.py
```

### Example Tool Calls

**List your repositories:**

```python
list_my_repositories()
# Returns: ["username/repo1", "username/repo2", ...]
```

**Create a new repository:**

```python
create_new_repository(
    name="my-new-project",
    description="A cool new project"
)
# Returns: "https://github.com/username/my-new-project.git"
```

**Push local project:**

```python
push_local_project_to_github(
    repo_url="https://github.com/username/my-new-project.git",
    commit_message="Initial commit"
)
# Returns: "Project successfully pushed to GitHub!"
```

## Project Structure

```text
my-first-mcp-agent/
├── src/
│   └── github_agent/
│       ├── __init__.py
│       └── server.py       # MCP server with GitHub tools
├── .env                    # GitHub token (gitignored)
├── .gitignore             # Excludes .env, .venv, cache files
├── main.py                # Entry point
├── pyproject.toml         # Project metadata and dependencies
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Dependencies

- `mcp[cli]` - Model Context Protocol server framework
- `requests` - HTTP library for GitHub API calls
- `gitpython` - Git operations for local repositories
- `python-dotenv` - Environment variable management

## License

MIT License - feel free to use and modify as needed.