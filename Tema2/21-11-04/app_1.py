import asyncio
import asyncio
import time
import random

COOK_TIME = 1
EXTRA_TIME = 1
BORGER_NUMBER = 100

BORGER_TYPE = ['normal', 'chicken', 'vegetarian']
EXTRAS = ['cheese', 'bacon', 'tomato', 'onion', 'tu abuela', 'pickles']

async def do_order(queue):
    print("Cocinero empesando a cocinar la anvorguesa")
    while True:
        current_order = await queue.get()
        id = current_order[0]
        meat_type = current_order[1]
        extra_type = current_order[2]
        await cook_da_borger(id, meat_type)
        await add_extra(id, extra_type)
        print("Borger n. " + str(id) + " done")
        queue.task_done()

async def cook_da_borger(id, meat_type):
    print("Adding " + meat_type + " beef to the borger " + str(id))
    await asyncio.sleep(COOK_TIME)

async def add_extra(id, extra_type):
    print("Adding " + extra_type + " to the borger " + str(id))
    await asyncio.sleep(EXTRA_TIME)

async def request_order(queue, id):
    print(f"Order n {id} added to queue")
    await queue.put((
            id,
            BORGER_TYPE[random.randrange(len(BORGER_TYPE))],
            EXTRAS[random.randrange(len(EXTRAS))]))
    return True

async def main():
    order_queue = asyncio.Queue()
    
    consumer_tasks = []
    for i in range(12):
        consumer_tasks.append(asyncio.create_task(request_order(order_queue, i)))

    cooker_tasks = []
    for i in range(3):
        cooker_tasks.append(asyncio.create_task(do_order(order_queue)))

    await asyncio.gather(*consumer_tasks, return_exceptions=True)

    await order_queue.join()

    for cooker in cooker_tasks:
        cooker.cancel()

asyncio.run(main())