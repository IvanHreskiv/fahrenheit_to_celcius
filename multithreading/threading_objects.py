import threading
import time


def time_notification(seconds):
    print(f"{seconds} seconds passed!!!")


def ten_seconds(event):
    tid = threading.get_ident()
    print(f'Waiting for ten seconds event... (thread id {tid})')
    event.wait()
    print(f'Event happend!!! (thread id {tid})')
    time_notification(10)


def ten_seconds_event(event):
    tid = threading.get_ident()
    print(f'Setting  ten seconds event... (thread id {tid})')
    event.set()


def twenty_seconds_notification(condition: threading.Condition):
    tid = threading.get_ident()
    print(f"Acquire condition!!! (thread id {tid})")
    with condition:
        print(f"Waiting for twenty second condition!!! (thread id {tid})")
        accured = condition.wait(timeout=25)
        print(f'Condition happend!!! (thread id {tid})')
        time_notification(20)
    if not accured:
        print(f'Condition had not accured!!! (thread id {tid})')


def twenty_seconds_func(condition: threading.Condition):
    tid = threading.get_ident()
    print(f"Acquire condition!!! (thread id {tid})")
    with condition:
        print(f"Counting twenty seconds... (thread id {tid})")
        time.sleep(20)
        print(f'Notify  twenty seconds condition... (thread id {tid})')
        condition.notify(n=1)


if __name__ == '__main__':

    # Event
    ten_second_event = threading.Event()
    timer = threading.Timer(10, ten_seconds_event, (ten_second_event,))
    timer.start()

    # ten_seconds_thread = threading.Thread(target=ten_seconds, args=(ten_second_event,))
    # ten_seconds_thread.start()

    # Condition
    mutex = threading.Lock()
    twenty_seconds_condition = threading.Condition(mutex)
    twenty_seconds_thread = threading.Thread(
       target=twenty_seconds_func, args=(twenty_seconds_condition,)
    )

    twenty_seconds_worker = threading.Thread(
       target=twenty_seconds_notification, args=(twenty_seconds_condition,)
    )

    twenty_seconds_second_worker = threading.Thread(
       target=twenty_seconds_notification, args=(twenty_seconds_condition,)
    )

    twenty_seconds_worker.start()
    twenty_seconds_second_worker.start()
    twenty_seconds_thread.start()

    twenty_seconds_thread.join()
    twenty_seconds_worker.join()
    twenty_seconds_second_worker.join()
