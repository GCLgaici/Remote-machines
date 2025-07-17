import asyncio
import websockets
import json
import random
from datetime import datetime


class ChatClient:
    def __init__(self, server_uri="ws://localhost:8765"):
        self.server_uri = server_uri
        self.client_id = None
        self.websocket = None
        self.receive_task = None
        self.running = False

    async def connect(self):
        """连接到服务器"""
        print(f"正在连接到 {self.server_uri}...")
        self.websocket = await websockets.connect(self.server_uri)
        self.running = True

        # 启动消息接收任务
        self.receive_task = asyncio.create_task(self.receive_messages())

    async def receive_messages(self):
        """接收服务器消息"""
        try:
            async for message in self.websocket:
                try:
                    data = json.loads(message)
                    self.handle_message(data)
                except json.JSONDecodeError:
                    print(f"收到无效消息: {message}")
        except websockets.exceptions.ConnectionClosed:
            print("与服务器的连接已关闭")
            self.running = False

    def handle_message(self, data):
        """处理不同类型的消息"""
        msg_type = data.get("type", "unknown")
        timestamp = data.get("timestamp", "")

        # 格式化时间
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp)
                formatted_time = dt.strftime("%H:%M:%S")
            except:
                formatted_time = timestamp
        else:
            formatted_time = ""

        if msg_type == "system":
            print(f"\n[系统消息 {formatted_time}] {data['message']} (在线人数: {data['client_count']})")

        elif msg_type == "chat":
            print(f"\n[{formatted_time} {data['sender']}] {data['text']}")

        elif msg_type == "private":
            print(f"\n[私聊 {formatted_time} {data['from']}] {data['text']}")

        elif msg_type == "command_result":
            if data["command"] == "list_users":
                print("\n在线用户列表:")
                for i, user in enumerate(data["result"], 1):
                    print(f"{i}. {user}")

        elif msg_type == "heartbeat":
            # 心跳包，不显示
            pass

        else:
            print(f"\n[未知消息类型] {data}")

    async def send_message(self, text):
        """发送聊天消息"""
        if not self.running or not self.websocket:
            print("未连接到服务器")
            return

        message = {
            "type": "chat",
            "text": text,
            "timestamp": datetime.now().isoformat()
        }
        await self.websocket.send(json.dumps(message))

    async def send_private_message(self, recipient_id, text):
        """发送私聊消息"""
        if not self.running or not self.websocket:
            print("未连接到服务器")
            return

        message = {
            "type": "private",
            "to": recipient_id,
            "text": text,
            "timestamp": datetime.now().isoformat()
        }
        await self.websocket.send(json.dumps(message))

    async def list_users(self):
        """请求在线用户列表"""
        if not self.running or not self.websocket:
            print("未连接到服务器")
            return

        message = {
            "type": "command",
            "command": "list_users",
            "timestamp": datetime.now().isoformat()
        }
        await self.websocket.send(json.dumps(message))

    async def disconnect(self):
        """断开连接"""
        if self.running and self.websocket:
            self.running = False
            if self.receive_task:
                self.receive_task.cancel()
                try:
                    await self.receive_task
                except asyncio.CancelledError:
                    pass
            await self.websocket.close()


async def main():
    """客户端主函数"""
    client = ChatClient()
    await client.connect()

    print("\n命令说明:")
    print("  /list    - 列出在线用户")
    print("  /pm <id> - 私聊用户 (例如: /pm client_123456_7890 你好)")
    print("  /exit    - 退出聊天")
    print("\n开始聊天...\n")

    try:
        while client.running:
            # 获取用户输入
            message = await asyncio.get_event_loop().run_in_executor(None, input, "> ")

            if not message:
                continue

            if message.startswith("/exit"):
                print("正在断开连接...")
                await client.disconnect()
                break

            elif message.startswith("/list"):
                await client.list_users()

            elif message.startswith("/pm "):
                parts = message.split(" ", 2)
                if len(parts) < 3:
                    print("格式错误: /pm <用户ID> <消息>")
                    continue
                await client.send_private_message(parts[1], parts[2])

            else:
                await client.send_message(message)

    except KeyboardInterrupt:
        print("\n正在断开连接...")
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())