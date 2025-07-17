import asyncio
import websockets
import json
import time
import random
from datetime import datetime

# 存储所有连接的客户端
connected_clients = {}


async def handle_client(websocket):  # 移除了 path 参数
    """处理客户端连接"""
    # 生成唯一客户端ID
    client_id = f"client_{int(time.time())}_{random.randint(1000, 9999)}"
    connected_clients[client_id] = websocket

    try:
        # 发送欢迎消息
        welcome = {
            "type": "system",
            "message": f"欢迎来到聊天室! 您的ID: {client_id}",
            "timestamp": datetime.now().isoformat(),
            "client_count": len(connected_clients)
        }
        await websocket.send(json.dumps(welcome))

        # 广播新用户加入通知
        join_notice = {
            "type": "system",
            "message": f"用户 {client_id} 加入了聊天室",
            "timestamp": datetime.now().isoformat(),
            "client_count": len(connected_clients)
        }
        await broadcast(json.dumps(join_notice), exclude=[client_id])

        # 接收客户端消息
        async for message in websocket:
            try:
                data = json.loads(message)
                print(f"收到来自 {client_id} 的消息: {data}")

                # 处理不同类型的消息
                if data["type"] == "chat":
                    # 广播聊天消息
                    chat_message = {
                        "type": "chat",
                        "sender": client_id,
                        "text": data["text"],
                        "timestamp": datetime.now().isoformat()
                    }
                    await broadcast(json.dumps(chat_message))

                elif data["type"] == "private":
                    # 私聊消息
                    recipient_id = data["to"]
                    if recipient_id in connected_clients:
                        private_message = {
                            "type": "private",
                            "from": client_id,
                            "text": data["text"],
                            "timestamp": datetime.now().isoformat()
                        }
                        await connected_clients[recipient_id].send(json.dumps(private_message))

                elif data["type"] == "command":
                    # 处理命令
                    if data["command"] == "list_users":
                        users = list(connected_clients.keys())
                        response = {
                            "type": "command_result",
                            "command": "list_users",
                            "result": users,
                            "timestamp": datetime.now().isoformat()
                        }
                        await websocket.send(json.dumps(response))

            except json.JSONDecodeError:
                print(f"无效的JSON格式: {message}")
            except KeyError as e:
                print(f"消息格式错误: {e}")

    except websockets.exceptions.ConnectionClosed:
        print(f"连接已关闭: {client_id}")
    finally:
        # 客户端断开连接
        del connected_clients[client_id]
        print(f"客户端断开: {client_id}")

        # 广播用户离开通知
        leave_notice = {
            "type": "system",
            "message": f"用户 {client_id} 离开了聊天室",
            "timestamp": datetime.now().isoformat(),
            "client_count": len(connected_clients)
        }
        await broadcast(json.dumps(leave_notice))


async def broadcast(message, exclude=None):
    """向所有客户端广播消息（可排除某些客户端）"""
    if exclude is None:
        exclude = []

    for client_id, client in list(connected_clients.items()):
        if client_id not in exclude:
            try:
                await client.send(message)
            except websockets.exceptions.ConnectionClosed:
                # 移除已断开连接的客户端
                if client_id in connected_clients:
                    del connected_clients[client_id]


async def send_heartbeats():
    """定期发送心跳包"""
    while True:
        try:
            heartbeat = {
                "type": "heartbeat",
                "timestamp": datetime.now().isoformat(),
                "client_count": len(connected_clients)
            }
            await broadcast(json.dumps(heartbeat))
            await asyncio.sleep(30)  # 每30秒发送一次
        except Exception as e:
            print(f"心跳发送失败: {e}")


async def main():
    """主函数"""
    # 启动心跳任务
    asyncio.create_task(send_heartbeats())

    # 启动WebSocket服务器
    server = await websockets.serve(
        handle_client,
        "localhost",
        8765,
        ping_interval=20,  # 每20秒发送一次ping
        ping_timeout=60  # 60秒无响应则断开
    )

    print("WebSocket 服务器已启动，监听 ws://localhost:8765")
    print("输入 'exit' 停止服务器")

    # 等待控制台输入退出命令
    while True:
        command = await asyncio.get_event_loop().run_in_executor(None, input, "")
        if command.lower() == "exit":
            print("正在关闭服务器...")
            server.close()
            await server.wait_closed()
            print("服务器已关闭")
            break


if __name__ == "__main__":
    asyncio.run(main())
