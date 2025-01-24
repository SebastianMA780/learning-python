import asyncio

async def process_file():
		print("Opening file")
		# Simulate a file operation
		# it will take 4 seconds to complete and the event loop will be free to do the following code
		await asyncio.sleep(4)
		print("File opened")

async def main():
		# gather is used to run multiple coroutines concurrently
		await asyncio.gather(process_file(), process_file(), process_file())

asyncio.run(main())
