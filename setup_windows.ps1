param(
    [switch]$UseMirror,
    [switch]$SeedProducts
)

$ErrorActionPreference = 'Stop'

# 1) Ensure current path contains manage.py
if (-not (Test-Path -Path '.\manage.py')) {
    Write-Host "[错误] 当前目录不是项目根目录（缺少 manage.py）" -ForegroundColor Red
    Write-Host "请先 cd 到包含 manage.py 和 requirements.txt 的目录再执行。" -ForegroundColor Yellow
    exit 1
}

# 2) Create and activate venv
if (-not (Test-Path -Path '.\.venv\Scripts\python.exe')) {
    py -m venv .venv
}

.\.venv\Scripts\Activate.ps1

# 3) Upgrade pip
python -m pip install --upgrade pip setuptools wheel

# 4) Install dependencies
if ($UseMirror) {
    pip install -r .\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
} else {
    pip install -r .\requirements.txt
}

# 5) Run migration
python .\manage.py migrate

# 6) Optional seed products
if ($SeedProducts) {
    python .\manage.py seed_products --reset
}

Write-Host "\n[完成] 依赖安装与数据库迁移已执行。" -ForegroundColor Green
if ($SeedProducts) {
    Write-Host "已初始化演示商品数据。" -ForegroundColor Green
}
Write-Host "启动命令: python .\manage.py runserver" -ForegroundColor Cyan
