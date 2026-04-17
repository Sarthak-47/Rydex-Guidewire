# run_all.ps1 – sets up backend virtual env, installs deps,
# writes startup.txt, and launches backend & frontend
# -------------------------------------------------
# 1️⃣ Ensure we are in the project root
Set-Location "d:\New folder (5)\rydex"

# -------------------------------------------------
# 2️⃣ Backend – create and activate a virtual environment
Write-Host "`n=== Setting up backend virtual environment ===`n"
python -m venv backend\.venv

# Activate the venv (PowerShell)
& "backend\.venv\Scripts\Activate.ps1"

# -------------------------------------------------
# 3️⃣ Install Python dependencies
Write-Host "`n=== Installing backend requirements ===`n"
pip install --upgrade pip
pip install -r backend\requirements.txt

# -------------------------------------------------
# 4️⃣ Write startup instructions (startup.txt)
$startup = @'
## Rydex Application Startup Guide

### Backend (virtual‑env)
```powershell
cd "d:\New folder (5)\rydex\backend"
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend (Next.js)
```powershell
cd "d:\New folder (5)\rydex\frontend"
npm install
npm run dev
```

### Optional Docker backend
```powershell
cd "d:\New folder (5)\rydex\backend"
docker build -t rydex-backend:latest .
docker run -d -p 8000:8000 --name rydex-backend rydex-backend:latest
```
'@
Set-Content -Path "startup.txt" -Value $startup -Encoding UTF8
Write-Host "`n=== startup.txt created ===`n"

# -------------------------------------------------
# 5️⃣ Launch backend (still inside the activated venv)
Write-Host "`n=== Starting backend (FastAPI) ===`n"
Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", "cd 'd:\New folder (5)\rydex\backend'; .\.venv\Scripts\Activate.ps1; python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"

# -------------------------------------------------
# 6️⃣ Launch frontend (Next.js) in a second window
Write-Host "`n=== Starting frontend (Next.js) ===`n"
Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", "cd 'd:\New folder (5)\rydex\frontend'; npm run dev"

Write-Host "`nAll services launched!`n"
# -------------------------------------------------
