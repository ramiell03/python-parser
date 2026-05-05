1. Clone (Pull) the Repository from GitHub
✅ Option A: Using Terminal (recommended)

Open terminal (or VS Code terminal):

git clone https://github.com/ramiell03/python-parser.git
cd math-expression-parser

👉 This downloads the project to your machine.

✅ Option B: Directly in Visual Studio Code
Open VS Code
Press Ctrl + Shift + P
Type:
Git: Clone
Paste your repo link
Choose a folder
Click Open
🔷 2. Open the Project in VS Code

If you used terminal:

code .

👉 This opens the folder in VS Code.

🔷 3. Set Up Python Environment (IMPORTANT)
✅ Create virtual environment
python -m venv venv
✅ Activate it
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
✅ Install dependencies
pip install -r requirements.txt

(if empty, you’ll add later)

🔷 4. Pull Latest Changes (TEAMWORK STEP)

Before starting work every time, run:

git pull origin main

👉 This ensures you have the latest version.

🔷 7. Commit Your Work
git add .
git commit -m "Implemented tokenizer logic"
🔷 8. Push to GitHub
git push origin main


🔷 9. Markdown (README) Preview in VS Code
✅ Open README.md
👀 Preview it:
Shortcut:
Ctrl + Shift + V

OR

Click:

Open Preview (top right icon)
✅ Side-by-side preview
Ctrl + K then V

👉 Left = code, Right = rendered document

🔷 10. Improve Markdown Rendering

Install extension in Visual Studio Code:

🔌 Recommended Extensions:
Markdown All in One
Markdown Preview Enhanced
🔷 11. Sync Changes (VERY IMPORTANT HABIT)

Before pushing:

git pull origin main

Fix conflicts if needed, then:

git push
🔷 12. Common Problems (and Fixes)
❌ “git not recognized”

👉 Install Git:

Git
❌ Merge conflicts

👉 Happens when:

Two people edit same file

Fix:

VS Code shows conflict markers
Choose correct version manually
❌ README not rendering well

👉 Check:

Proper Markdown syntax
Use triple backticks for code blocks
🔥 TEAM WORKFLOW (WHAT EVERYONE MUST FOLLOW)

Every time you work:

git pull origin main

# code...
git add .
git commit -m "your work"
git push origin main