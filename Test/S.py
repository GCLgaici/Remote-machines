
import asyncio
import websockets

async def hello(websocket, path):
    while True:
        name = await websocket.recv()
        print(f"{name}")

        greeting = f"hello {name}"

        await websocket.send(greeting)
        print(f"> {greeting}")

if __name__ == '__main__':
    start_server = websockets.server(hello, "0.0.0.0", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

