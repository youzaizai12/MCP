自定义 MCP 服务 
📌 项目简介
这是一个基于 FastMCP 开发的自定义 MCP（Model Control Protocol）服务端，集成了文件操作、系统信息获取、网络请求三大类工具，可直接对接 Cursor/Claude 等支持 MCP 协议的 AI 客户端，让 AI 能调用你的本地工具完成复杂任务（如爬取网页、读写文件、获取系统信息等）。
🚀 快速开始
1. 环境准备
Python 3.10+
虚拟环境（推荐使用 Conda）
bash
运行
# 创建并激活虚拟环境
conda create -n MCP python=3.11 -y
conda activate MCP

# 安装依赖
pip install fastmcp requests
2. 项目文件
my_mcp.py：MCP 服务端主程序
client.py：本地测试客户端（可选）

🛠️ 功能说明
本服务端提供 6 个可被 AI 调用的工具：
表格
工具名称	功能描述	示例调用
list_files	遍历指定文件夹，返回文件列表（默认读取桌面）	list_files("~/Desktop")
read_text_file	读取文本文件内容（支持 .txt/.md/.py/.json 等）	read_text_file("D:/test.txt")
write_text_file	覆盖写入文本文件	write_text_file("D:/output.txt", "Hello MCP!")
get_system_info	获取系统信息（系统版本、主机名、Python 版本等）	get_system_info()
fetch_webpage	爬取网页文本内容（限制返回长度，避免过长）	fetch_webpage("https://www.tmall.com")
fetch_api	请求 API 接口，返回 JSON 数据	fetch_api("https://httpbin.org/get")

🔌 对接 Cursor 配置
打开 Cursor 设置（Ctrl + ,），搜索「MCP」进入 MCP 服务器设置
点击「添加新服务器」，填入以下配置（修改为你的实际路径）：
json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "D:\\anaconda\\envs\\MCP\\python.exe",
      "args": ["D:\\大模型应用开发\\案例五\\MCP\\my_mcp.py"]
    }
  }
}
保存配置并重启 Cursor，当服务端状态变为绿色圆点即表示连接成功

🧪 本地测试
可以使用 client.py 直接测试服务端功能，无需依赖 AI 客户端：
    
运行命令：
bash
运行
python client.py

📝 使用示例（在 Cursor 中）
连接成功后，你可以用自然语言让 AI 调用工具，例如：
「帮我读取桌面的 test.txt 文件内容」
「帮我遍历我的下载文件夹，列出所有文件」
「帮我爬取天猫首页内容，提取商品价格信息」
「帮我获取当前电脑的系统信息」
「帮我新建一个文件，内容是：这是MCP服务生成的测试文件」

❌ 常见问题与解决方案
1. ModuleNotFoundError: No module named 'requests'
原因：虚拟环境中未安装 requests 库
解决：在激活虚拟环境后执行 pip install requests

3. 服务端显示红色圆点（连接失败）
原因 1：python.exe 路径错误，Cursor 未使用你的虚拟环境 Python
解决：用 where python 获取虚拟环境的 Python 绝对路径，替换配置中的 command
原因 2：my_mcp.py 路径错误或包含中文导致解析失败
解决：使用文件的绝对路径，确保路径中无特殊字符

5. Cursor 无法识别新增的工具
原因：Cursor 缓存了旧的服务端信息
解决：修改代码后重启 Cursor，并在 MCP 设置中重新保存配置
📈 扩展开发
你可以通过添加 @mcp.tool() 装饰器，快速扩展自定义工具，格式如下：
python
运行
@mcp.tool()
def your_tool_name(param1: str, param2: int) -> str:
    """工具说明（AI 会读取这段文字理解工具用途）"""
    # 你的业务逻辑（如数据库操作、文件处理、API 调用等）
    return "工具返回结果"
📄 License
MIT License，可自由修改和扩展使用。
如果你需要，我可以帮你把这份 README 改成更简洁的 Markdown 版本，或者补充更多使用场景的示例。




