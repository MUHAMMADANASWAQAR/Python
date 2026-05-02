import asyncio

async def print_routine():
    print("Anas is working and then suddenly sleep ")
    await asyncio.sleep(2)
    print("I wake up ")

async def main():
    await asyncio.gather(
        print_routine(),
        print_routine(),
        print_routine()
    )

asyncio.run(main())
