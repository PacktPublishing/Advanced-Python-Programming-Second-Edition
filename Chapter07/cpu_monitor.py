from rx import interval
from rx.operators import map, publish, buffer_with_count

import psutil
import numpy as np

import pylab as plt


cpu_data = publish()(map(lambda x: psutil.cpu_percent())(interval(0.1)))
cpu_data.connect()


def monitor_cpu(npoints):
    (lines,) = plt.plot([], [])
    plt.xlim(0, npoints)
    plt.ylim(0, 100)

    cpu_data_window = buffer_with_count(npoints, 1)(cpu_data)

    def update_plot(cpu_readings):
        lines.set_xdata(np.arange(len(cpu_readings)))
        lines.set_ydata(np.array(cpu_readings))
        plt.draw()

    alertpoints = 4
    high_cpu = map(lambda readings: all(r > 20 for r in readings))(
        buffer_with_count(alertpoints, 1)(cpu_data)
    )

    label = plt.text(1, 1, "normal")

    def update_warning(is_high):
        if is_high:
            label.set_text("high")
        else:
            label.set_text("normal")

    high_cpu.subscribe(update_warning)
    cpu_data_window.subscribe(update_plot)

    plt.show()


if __name__ == "__main__":
    monitor_cpu(10)
