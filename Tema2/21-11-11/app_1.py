import asyncio
import time

MATCH_DURATION = 1000
OPONENT_NUMBER = 1000
PRO_TIME = 0.00005
AMATEUR_TIME = 0.0005
COMPLETED = 0

#await queue.put((game_id, current_turn))

async def pro_turn(pro_queue, amateur_queues):
    while True:
        print("Pro awaiting")
        turn_info = await pro_queue.get()
        game_id = turn_info[0]
        current_turn = turn_info[1]
        await asyncio.sleep(PRO_TIME)
        print(f"Game n{game_id}.Turn n{current_turn}. Pro moves.")
        current_turn += 1
        if (current_turn >= MATCH_DURATION):
            print(f"Game n{game_id} ended")
            global COMPLETED
            COMPLETED += 1
            if(COMPLETED == OPONENT_NUMBER):
                pro_queue.task_done()
                return
        else:
            await amateur_queues[game_id].put((game_id, current_turn))
        pro_queue.task_done()

async def amateur_turn(id, pro_queue, amateur_queue):
    while True:
        print(f"Amateur {id} awaiting")
        turn_info = await amateur_queue.get()
        game_id = turn_info[0]
        current_turn = turn_info[1]
        await asyncio.sleep(AMATEUR_TIME)
        print(f"Game n{game_id}.Turn n{current_turn}. Amateur moves.")
        current_turn += 1
        await pro_queue.put((game_id, current_turn))
        amateur_queue.task_done()

async def main():
    pro_queue = asyncio.Queue()
    amateur_queues = [asyncio.Queue() for _ in range(OPONENT_NUMBER)]

    pro_task = asyncio.create_task(pro_turn(pro_queue, amateur_queues))

    amateur_tasks = []
    for i in range(OPONENT_NUMBER):
        amateur_tasks.append(asyncio.create_task(amateur_turn(i, pro_queue, amateur_queues[i])))
        await amateur_queues[i].put((i, 0))

    print("------------------------------------------------")
    await asyncio.gather(pro_task, return_exceptions=True)
    print("________________________________________________")

    for amateur_queue in amateur_queues:
        await amateur_queue.join()
    await pro_queue.join()

    pro_task.cancel()
    for amateur in amateur_tasks:
        amateur.cancel()


asyncio.run(main())