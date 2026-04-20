import os
import sys
import platform
import requests
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务
mcp = FastMCP("我的全能MCP服务")

# ==============================================
# 1. 文件操作工具
# ==============================================

@mcp.tool()
def list_files(folder_path: str = "~/Desktop") -> list:
    """
    遍历指定文件夹，返回文件列表
    - 默认读取桌面
    """
    path = Path(folder_path).expanduser()
    if not path.exists():
        return [f"错误：路径不存在 {folder_path}"]
    return [str(f) for f in path.iterdir()]

@mcp.tool()
def read_text_file(file_path: str) -> str:
    """
    读取文本文件内容
    支持：.txt / .md / .py / .json 等
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"读取失败：{str(e)}"

@mcp.tool()
def write_text_file(file_path: str, content: str) -> str:
    """
    写入文本文件（覆盖写入）
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"成功写入文件：{file_path}"
    except Exception as e:
        return f"写入失败：{str(e)}"

# ==============================================
# 2. 系统信息工具
# ==============================================

@mcp.tool()
def get_system_info() -> dict:
    """
    获取当前电脑系统信息
    - 系统版本 / 主机名 / Python版本 / 工作目录
    """
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "node": platform.node(),
        "python_version": sys.version,
        "current_dir": os.getcwd(),
        "desktop_path": str(Path.home() / "Desktop"),
    }

# ==============================================
# 3. 网络请求（爬网页 + 调用接口）
# ==============================================

@mcp.tool()
def fetch_webpage(url: str) -> str:
    """
    爬取网页文本内容
    """
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text[:8000]  # 限制长度，避免太长
    except Exception as e:
        return f"请求失败：{str(e)}"

@mcp.tool()
def fetch_api(url: str) -> dict:
    """
    请求 API 接口，返回 JSON 数据
    """
    try:
        resp = requests.get(url, timeout=10)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

# ==============================================
# 启动 MCP 服务（对接 Cursor / Claude）
# ==============================================
if __name__ == "__main__":
    mcp.run(transport="stdio")