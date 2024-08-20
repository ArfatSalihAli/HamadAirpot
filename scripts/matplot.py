def update_depart_plot(i, fig, ax1, data_queue):
    """
    Update the departures plot with the latest data from the queue.
    """
    ax1.clear()
    departures = data_queue.get()
    ax1.plot(departures, color='blue', label='Departures')
    ax1.set_title("Departures Today")
    ax1.set_xlabel("Time Interval")
    ax1.set_ylabel("Number of Flights")
    ax1.legend()

def update_arriv_plot(i, fig, ax2, data_queue2):
    """
    Update the arrivals plot with the latest data from the queue.
    """
    ax2.clear()
    arrivals = data_queue2.get()
    ax2.plot(arrivals, color='green', label='Arrivals')
    ax2.set_title("Arrivals Today")
    ax2.set_xlabel("Time Interval")
    ax2.set_ylabel("Number of Flights")
    ax2.legend()

def update_busiest_hours_plot(i, fig, ax3, depBusiestHoursQueue, arrBusiestHoursQueue):
    """
    Update the busiest hours plot for departures and arrivals with the latest data.
    """
    ax3.clear()
    busiest_dep = depBusiestHoursQueue.get()
    busiest_arr = arrBusiestHoursQueue.get()

    ax3.plot(busiest_dep, color='red', label='Busiest Departures')
    ax3.plot(busiest_arr, color='purple', label='Busiest Arrivals')
    ax3.set_title("Busiest Hours for Departures/Arrivals")
    ax3.set_xlabel("Hour of the Day")
    ax3.set_ylabel("Number of Flights")
    ax3.legend()