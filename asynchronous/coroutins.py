import asyncio


async def sleepy_alarm(time):
    await asyncio.sleep(time)
    print("wake up!")


async def person_alarm(person, time):
    await asyncio.sleep(time)
    print(f"{person} -- wake up!")


async def wake_up_gang():
    tasks = [
        asyncio.create_task(person_alarm("Bob", 3), name="wake up Bob"),
        asyncio.create_task(person_alarm("Sanjeet", 4), name="wake up Sanjeet"),
        asyncio.create_task(person_alarm("Doris", 2), name="wake up Doris"),
        asyncio.create_task(person_alarm("Kim", 5), name="wake up Kim")
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(sleepy_alarm(5))

    print("Start person alarm!!!")
    asyncio.run(wake_up_gang())
