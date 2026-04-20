import asyncio
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

async def main():
    transport = StdioTransport(
        command="python",
        args=["test.py"]
    )

    async with Client(transport=transport) as client:
        print("✅ 连接成功！")

        # 调用工具1：获取桌面文件
        files_result = await client.call_tool("get_desktop_files")
        # 提取文件列表
        files = [item.text for item in files_result.content]
        print("\n📂 桌面文件：")
        print(files)

        # 调用工具2：计算器（使用 arguments 而非 parameters）
        res = await client.call_tool(
            "calculator",
            arguments={"a": 10, "b": 20, "operator": "+"}  # 修复此处
        )
        print("\n🧮 10 + 20 =", res.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())