
import matplotlib
import matplotlib.pyplot as plt
import base64

from io import BytesIO

matplotlib.use("Agg")


def sparkline(data, figsize=(1, 0.5), **kwags):
    """
    Returns a HTML image tag containing a base64 encoded sparkline style plot
    """
    data = list(data)

    fig, ax = plt.subplots(1, 1, figsize=figsize, **kwags)
    ax.plot(data, color='#35684F')
    for k, v in ax.spines.items():
        v.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.margins(0.1)
    plt.plot(len(data) - 1, data[len(data) - 1], marker='o', markerfacecolor='#35684F', markeredgecolor='#35684F', markersize=4)

    ax.fill_between(range(len(data)), data, len(data) * [min(data)], alpha=0.5, color="#D2E1D9")

    img = BytesIO()
    # plt.savefig(img, transparent=True, bbox_inches='tight')
    plt.savefig(img, format='svg') # save as svg
    img.seek(0)
    plt.close()

    svg_data = img.getvalue()  # this is svg data

    # return base64.b64encode(img.read()).decode("UTF-8") # export svg
    return svg_data.decode("UTF-8")


values = [
        [227.2, 263.62, 252.32, 289.39, 308.65],
        [156.28, 223.37, 234.36, 275.79, 291.51],
        [218.6, 229.35, 220.01, 226.43, 232.23],
        [395.34, 413.52, 404.58, 444.72, 426.89],
        [87.36, 98.24, 92.25, 102.17, 105.83],
        [255.05, 255.11, 243.63, 249.54, 239.24],
        [549.09, 568.93, 553.21, 574.36, 542.58],
        [490.06, 485.73, 464.91, 515.18, 492.62],
        [219.3, 215.19, 191.2, 208.35, 192.21],
        [88.8, 95.46, 92.66, 106.95, 108.24]
    ]


with open("sparkline.html", "w") as file:
    for value in values:
        file.write('''
        <div>{}</div>
        '''.format(sparkline(value)))
