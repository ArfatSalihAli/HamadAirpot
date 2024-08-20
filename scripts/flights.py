import time
import random

def getFlightsData(data_queue, data_queue2, depBusiestHoursQueue, arrBusiestHoursQueue):
    """
    This function simulates fetching flight data and sending it to different queues
    to be processed and plotted in real-time.
    """
    while True:
        # Generate some dummy data for the number of departures and arrivals
        departures = [random.randint(100, 200) for _ in range(10)]
        arrivals = [random.randint(50, 150) for _ in range(10)]

        # Simulate the busiest hours data for departures and arrivals
        busiest_hours_dep = [random.randint(10, 50) for _ in range(10)]
        busiest_hours_arr = [random.randint(5, 45) for _ in range(10)]

        # Put the data into the queues
        data_queue.put(departures)
        data_queue2.put(arrivals)
        depBusiestHoursQueue.put(busiest_hours_dep)
        arrBusiestHoursQueue.put(busiest_hours_arr)

        # Wait for 10 seconds before fetching new data
        time.sleep(10)