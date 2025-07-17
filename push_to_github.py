# push_to_github.py
import os
from git import Repo
from dotenv import load_dotenv

# 載入 .env
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# === 基本參數（請依自己需求調整）===
repo_dir = os.path.abspath('.')
repo_url = "https://github.com/falco8628/stock-analysis-prototype.git"
branch = "main"
commit_message = "Initialize project structure with modules"

# 用 token 組出 push 專用 URL
if GITHUB_TOKEN is None:
    raise Exception("GITHUB_TOKEN not found in .env")

auth_url = repo_url.replace(
    "https://",
    f"https://falco8628:{GITHUB_TOKEN}@"
)

# 初始化 Repo 或使用現有 Repo
repo = Repo(repo_dir)
repo.git.add(all=True)
repo.index.commit(commit_message)
origin = None

if 'origin' not in [remote.name for remote in repo.remotes]:
    origin = repo.create_remote('origin', repo_url)
else:
    origin = repo.remote('origin')

# 設定新的 push URL
origin.set_url(auth_url)

# Push!
print(f"Pushing to {repo_url} ...")
origin.push(refspec=f"{branch}:{branch}")
print("Push finished.")
