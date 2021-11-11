import asyncio
import random

OPONENT_NUMBER = 24             # Number of amateur oponents 

MIN_PRO_TIME = 0.00005          # Min time the Pro player will take to complete their turn
MAX_PRO_TIME = 0.005            # Max time the Pro player will take to complete their turn
MIN_AMATEUR_TIME = 0.0005       # Min time the Amateur player will take to complete their turn
MAX_AMATEUR_TIME = 0.05         # Max time the Amateur player will take to complete their turn

PRO_CHANCE_OF_WINNING = 4       # Chance (over 100) the Pro will win and end the game in this turn

COMPLETED = 0                   # Counter of completed games. This helps to close the task "pro_task"

async def pro_turn(pro_queue, amateur_queues):
    while True:
        turn_info = await pro_queue.get()
        game_id, current_turn = turn_info
        await asyncio.sleep(random.uniform(MIN_PRO_TIME, MAX_PRO_TIME))
        print(f"Game n{game_id}.Turn n{current_turn}. Pro moves.")
        if (random.randrange(100) <= PRO_CHANCE_OF_WINNING):
            print(f"Game n{game_id} ended")
            global COMPLETED
            COMPLETED += 1
            if(COMPLETED == OPONENT_NUMBER):
                pro_queue.task_done()
                return
        else:
            current_turn += 1
            await amateur_queues[game_id].put((game_id, current_turn))
        pro_queue.task_done()

async def amateur_turn(id, pro_queue, amateur_queue):
    while True:
        turn_info = await amateur_queue.get()
        game_id, current_turn = turn_info
        await asyncio.sleep(random.uniform(MIN_AMATEUR_TIME, MAX_AMATEUR_TIME))
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

    await asyncio.gather(pro_task, return_exceptions=True)

    for amateur_queue in amateur_queues:
        await amateur_queue.join()
    await pro_queue.join()

    pro_task.cancel()
    for amateur in amateur_tasks:
        amateur.cancel()


asyncio.run(main())