import asyncio
import time
import random

async def random_number_generator(threshold, id):
    i = random.random()
    while(i < threshold):
        i = random.random()
        print("Tarea " + str(id) + ": numero no encontrado: " + str(i) + " < " + str(threshold))
        await asyncio.sleep(1)
    print("Tarea " + str(id) + ": numero encontrado: " + str(i) + " > " + str(threshold))
    return i

async def main():
    #await asyncio.gather(random_number_generator(random.random()), random_number_generator(random.random()), random_number_generator(random.random()))
    #tasks = 0
    print("Input the number of tasks: \t")
    tasks = input()
    nums = await asyncio.gather(*(random_number_generator(random.random(), n) for n in range(int(tasks))))

asyncio.run(main())