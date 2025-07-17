import asyncio
import websockets


async def hello():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        while True:
            name = input("111:")

            await websocket.send(name)

            greeting = await websocket.recv()
            print(greeting)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(hello())

