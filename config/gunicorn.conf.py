# gunicorn 默认配置文件
# 修改后需重新构建镜像（或重启容器内 gunicorn 进程）才会生效
# 如需自定义配置，请复制本文件为 gunicorn_custom.conf.py 后修改，启动脚本会优先使用自定义配置

# 监听地址与端口（与 uwsgi 配置保持一致，通常由 Nginx 反代转发到此端口）
bind = "0.0.0.0:10086"

# Worker 进程模型：gthread（线程型），与下方 threads 配合，一个 Worker 可并发处理多个请求
worker_class = "gthread"

# Worker 进程数：经验公式为 CPU 核数 × 2 + 1
# 容器资源较小时请调低，避免内存/CPU 被打满
workers = 4

# 每个 Worker 的线程数：4 个 Worker × 2 线程 = 最多同时处理 8 个请求
threads = 2

# 启动时先加载 Django 应用再 fork Worker，加快启动速度并降低整体内存占用
# 注意：若应用在 import 阶段就建立数据库/外部连接，请谨慎启用此项
preload_app = True

# 单个请求最长处理时间（秒）。文档转换、OCR 等耗时操作较多，不宜设置过小
timeout = 300

# Worker 被重启/回收时的优雅退出宽限期（秒）
graceful_timeout = 30

# 单个 Worker 存活期间最多处理的请求数，防止内存泄漏长期累积
max_requests = 1000

# 在 max_requests 基础上增加随机抖动，避免所有 Worker 在同一时间点重启造成请求抖动
max_requests_jitter = 100

# 与上游（Nginx/客户端）之间的长连接保持时间（秒）
keepalive = 5

# 访问日志：输出到 stdout，Docker 场景下由容器日志统一收集
accesslog = "-"

# 访问日志格式（客户端IP 时间 请求行 状态码 响应大小 来源 用户代理）
access_log_format = '%(h)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# 错误日志：输出到 stderr，Docker 场景下由容器日志统一收集
errorlog = "-"

# 日志级别：debug / info / warning / error / critical
loglevel = "info"

# 将 Worker 中的 print/标准输出一并写入错误日志，便于排查问题
capture_output = True

# 进程 PID 文件路径，便于在宿主机上管理/重启 gunicorn 进程
pidfile = "/app/MrDoc/config/gunicorn.pid"

# Worker 临时文件目录：放在内存文件系统，减少对磁盘的读写
worker_tmp_dir = "/dev/shm"

# ---- 可选配置（按需取消注释） ----
# 若前端有可信 Nginx 反代，且希望访问日志记录真实客户端 IP，可放开以下配置：
# forwarded_allow_ips = "127.0.0.1"
