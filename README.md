# MrDoc 示例知识库

一个基于 [MrDoc](https://gitee.com/zmister/MrDoc) 的**脱敏演示项目**，用于展示在线文档 / 知识库系统的界面与功能。

> ⚠️ 本仓库是演示用途，已移除所有真实品牌信息与真实数据。示例文档内容均为通用说明，不涉及任何实际公司或生产信息。

## 功能截图

| 知识库首页 | 文档示例 |
|---|---|
| 见下方示例图 | 见下方示例图 |

## 示例内容

内置了一个「示例知识库」，包含 4 篇主题文档（儿童图书与纸艺展示相关）：

1. 欢迎使用 MrDoc
2. 儿童图书：板纸书（Board Book）介绍
3. 纸艺展示：立体书（Pop-up Book）工艺
4. 印刷色彩基础：CMYK 与 Pantone

配图位于 `media/demo/` 目录（SVG 格式，中性示意）。

## 默认账号

- 用户名：`admin`
- 密码：`admin123`

> 仅用于本地演示，生产环境请务必修改。

## 快速开始

```bash
# 1. 创建虚拟环境
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 初始化数据库（已内置示例数据，无需迁移）
python manage.py migrate

# 4. 启动
python manage.py runserver
```

访问 http://127.0.0.1:8000

## 项目结构

```
mrdoc-demo/
├── MrDoc/          # Django 项目配置
├── app_admin/      # 后台管理
├── app_api/        # API
├── app_doc/        # 文档 / 知识库核心
├── app_ai/         # AI 能力
├── config/         # 配置文件 + SQLite 数据库
├── static/         # 前端静态资源（第三方库）
├── template/       # HTML 模板
├── media/demo/     # 示例配图
└── manage.py
```

## 许可

本项目基于 MrDoc 开源项目，遵循其原始开源许可。本仓库的示例内容与配图仅用于演示。
