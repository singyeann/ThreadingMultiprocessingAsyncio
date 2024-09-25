import asyncio
import aiofiles

async def async_write_to_file(filename, data, delay):
    await asyncio.sleep(delay)  # Simulate delay
    async with aiofiles.open(filename, 'a') as f:
        await f.write(data + '\n')

async def run_async_tasks():
    tasks = [
        async_write_to_file('async_output.txt', 'Async Task 1 completed', 2),
        async_write_to_file('async_output.txt', 'Async Task 2 completed', 3),
        async_write_to_file('async_output.txt', 'Async Task 3 completed', 1),
    ]
    await asyncio.gather(*tasks)
