# 小鱼商城（Django）

这是一个可运行的 Django 电商示例项目，包含以下能力：

- 用户：注册、登录、退出
- 商品：商品名称、描述、价格、库存、图片（本地上传或图片链接）
- 商品：商品列表、商品详情
- 购物车：加入购物车、修改数量、删除商品、登录后保留购物车
- 下单：从购物车创建订单、扣减库存、查看订单历史
- 后台：Django Admin 商品管理 + 自定义商品筛选页面

---

## 1. 环境要求

- Python 3.10+
- pip

---

## 2. 安装步骤（本地可直接操作）

> 以下命令在项目根目录执行（也就是 `manage.py` 所在目录）。

### Step 1: 创建虚拟环境

```bash
python -m venv .venv
```

### Step 2: 激活虚拟环境

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3: 安装依赖

```bash
pip install -r requirements.txt
```

### Step 4: 执行数据库迁移

```bash
python manage.py migrate
```

### Step 5: 创建管理员账号

```bash
python manage.py createsuperuser
```

按提示输入用户名/邮箱/密码。

### Step 6: 启动项目

```bash
python manage.py runserver
```

访问：

- 商城首页：http://127.0.0.1:8000/
- 管理后台：http://127.0.0.1:8000/admin/
- 自定义商品管理页（需管理员登录）：http://127.0.0.1:8000/manage/products/

---

## 3. 快速初始化测试数据（推荐）

先进入后台创建几条商品数据：

1. 登录 `/admin/`
2. 进入 **Products -> Products**
3. 点击 **Add Product**
4. 填写：`name / description / price / stock / image(可选) / image_url(可选) / is_active`

然后即可在前台测试浏览、加购、下单。

---

## 4. 功能测试流程（你可以照着走）

1. 打开首页，确认商品展示正常。
2. 点击注册，创建普通用户并自动登录。
3. 把商品加入购物车，修改数量，删除商品。
4. 点击结算提交订单。
5. 在“我的订单”查看历史订单。
6. 登录管理员账号，查看商品库存是否已扣减。

---

## 5. 项目结构（核心）

```text
django_shop/
├── django_shop/         # 项目配置
├── accounts/            # 用户注册登录
├── products/            # 商品
├── cart/                # 购物车
├── orders/              # 订单
├── templates/           # 基础模板
├── static/              # 静态资源
├── manage.py
└── requirements.txt
```

---

## 6. 常见问题

### Q1: `No module named django`

说明依赖没安装，执行：

```bash
pip install -r requirements.txt
```

### Q2: 数据库报错

删除 `db.sqlite3` 后重新迁移：

```bash
rm -f db.sqlite3
python manage.py migrate
```

### Q3: 页面无样式

确认 `DEBUG=True` 且通过 `python manage.py runserver` 启动。



## 7. Windows 常见报错一键修复（针对你截图里的问题）

你截图里有两个核心问题：

1. `requirements.txt` 找不到
2. `manage.py` 找不到

这通常是因为你在**错误目录**执行了命令。请按下面步骤操作：

### 7.1 先进入正确目录

在 PowerShell 执行（示例路径按你机器改）：

```powershell
cd "D:\云平台\小鱼\test-project-codex-implement-final-code-with-django"
dir manage.py, requirements.txt
```

如果能看到这两个文件，再继续。

### 7.2 激活虚拟环境并安装依赖

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r .\requirements.txt
```

### 7.3 如果你遇到 SSL 错误（和截图一样）

使用国内镜像安装：

```powershell
pip install -r .\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```

### 7.4 迁移并启动

```powershell
python .\manage.py migrate
python .\manage.py runserver
```

### 7.5 一键脚本（推荐）

项目里提供了 `setup_windows.ps1`，可自动检查目录、创建 venv、安装依赖并迁移：

```powershell
.\setup_windows.ps1
```

如果网络有 SSL/证书问题，用镜像参数：

```powershell
.\setup_windows.ps1 -UseMirror
```
