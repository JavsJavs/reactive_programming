import asyncio
import time
import random

COOK_TIME = 3
EXTRA_TIME = 1
BORGER_NUMBER = 100

BORGER_TYPE = ['normal', 'chicken', 'vegetarian']
EXTRAS = ['cheese', 'bacon', 'tomato', 'onion', 'tu abuela', 'pickles']

async def do_order(id, meat_type, extra_type):
    borger = []
    borger.append(id)
    borger.append((await asyncio.gather(cook_da_borger(id, meat_type)))[0])
    borger.append((await asyncio.gather(add_extra(id, extra_type)))[0])
    print("Borger n. " + str(id) + " done")
    return borger

async def cook_da_borger(id, meat_type):
    print("Adding " + meat_type + " beef to the borger " + str(id))
    await asyncio.sleep(COOK_TIME)
    return meat_type

async def add_extra(id, extra_type):
    print("Adding " + extra_type + " to the borger " + str(id))
    await asyncio.sleep(EXTRA_TIME)
    return extra_type

async def main():
    t = time.time()
    borger_list = []
    borger_list = await asyncio.gather(*(do_order(n, BORGER_TYPE[random.randrange(len(BORGER_TYPE))], EXTRAS[random.randrange(len(EXTRAS))]) for n in range(int(BORGER_NUMBER))))
    tiempo_async = (f'Tiempo de ejecucion: {time.time() - t} segundos')
    
    print("\nASYNC\n" + tiempo_async + "\n")
    print_orders(borger_list)

def print_orders(order_list):
    for order in order_list:
        print("Order n" + str(order[0]) + ": " + order[1] + " + " + order [2] + "")

asyncio.run(main())