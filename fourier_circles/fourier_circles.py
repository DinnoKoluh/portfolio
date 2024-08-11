from matplotlib import pyplot as plt, patches
import numpy as np
# https://stackoverflow.com/questions/42955608/how-can-i-remove-a-plot-with-python


def conv(X1, X2, to_plot=False):
    Y = []
    l1 = len(X1)
    l2 = len(X2)
    for i in range(0, l1 + l2 - 1):
        y = 0
        for j in range(0, l2):
            x2 = 0
            x1 = 0
            if i - j >= 0 and i - j < l2:
                x2 = X2[i - j]
            if j < l1:
                x1 = X1[j]
            y = y + x1 * x2
        Y.append(y)
    if to_plot:
        plt.subplot(1, 3, 1)
        plt.plot(X1, "ro")
        plt.grid()
        plt.subplot(1, 3, 2)
        plt.plot(X2, "bo")
        plt.grid()
        plt.subplot(1, 3, 3)
        plt.plot(Y, "go")
        plt.grid()
    return Y


def circle_animation():
    xx = np.array([])
    t = np.arange(0, 20, 0.1)
    plt.rcParams["figure.figsize"] = [16, 8]
    fig = plt.figure()
    ax = fig.add_subplot()
    r0 = 2
    cx = 5
    cy = 5
    circle0 = patches.Circle((cx, cy), radius=r0, facecolor="None", edgecolor="green")
    ax.add_patch(circle0)
    for ti in t:
        f = 0.25
        w = 2 * np.pi * f

        r = r0
        Px = r * np.cos(w * ti) + cx
        Py = r * np.sin(w * ti) + cy
        Pcircle = patches.Circle((Px, Py), radius=0.05, color="blue")
        ax.add_patch(Pcircle)

        xx = np.insert(xx, 0, ti)
        sinx = xx + cx + 1.5 * r
        siny = r * np.sin(w * np.flip(xx)) + cy
        len_to_keep = 50
        if len(sinx) > len_to_keep:
            sinx = sinx[-len_to_keep:-1]
            siny = siny[-len_to_keep:-1]
        p1 = plt.plot(sinx, siny, color="black")
        p2 = plt.plot([Px, sinx[-1]], [Py, siny[-1]], color="red")
        p3 = plt.plot([Px, cx], [Py, cy], color="black")
        # Mention x and y limits to define their range
        plt.xlim(0, 20)
        plt.ylim(0, 10)

        # removing things after one frame
        plt.pause(0.01)
        if ti != t[-1]:
            Pcircle.remove()
            for h1, h2, h3 in zip(p1, p2, p3):
                h1.remove()
                h2.remove()
                h3.remove()
    plt.show()


def shape_animation():
    xx = np.array([])
    yy = np.array([])
    t = np.arange(0, 15, 0.05)
    plt.rcParams["figure.figsize"] = [14, 7]
    fig = plt.figure()
    ax = fig.add_subplot()
    r0 = 4
    # Mention x and y limits to define their range
    plt.xlim(-20, 20)
    plt.ylim(-10, 10)
    f = 0.25
    w = 2 * np.pi * f

    for ti in t:
        circles = []  # where the circles are stored
        radii = []  # where the radii of the circles are stored
        cx = 0  # x center point of circle
        cy = 0  # y center point of circle
        for i in range(1, 8, 2):
            prevx = cx
            prevy = cy
            r = r0 * (4 / (i * np.pi))
            circles.append(
                patches.Circle(
                    (prevx, prevy), radius=r, facecolor="None", edgecolor="green"
                )
            )

            ax.add_patch(circles[-1])
            cx = cx + r * np.cos(w * i * ti)
            cy = cy + r * np.sin(w * i * ti)
            radii.append(plt.plot([prevx, cx], [prevy, cy], color="black"))

        Pcircle = patches.Circle((cx, cy), radius=0.05, color="blue")
        ax.add_patch(Pcircle)

        xx = np.insert(xx, 0, ti + 2 * r0)
        yy = np.append(yy, cy)
        keep = 100
        # if len(xx) > keep:
        #     xx = xx[-keep:-1]
        #     yy = yy[-keep:-1]
        p1 = plt.plot(xx, yy, color="black")  # plot of the shape
        p2 = plt.plot(
            [xx[-1], cx], [cy, cy], color="red"
        )  # line connecting circles with shape

        # removing things after one frame
        plt.pause(0.01)
        if ti != t[-1]:
            for h1, h2 in zip(p1, p2):
                h1.remove()
                h2.remove()
            for p in radii:
                for h in p:
                    h.remove()
            for c in circles:
                c.remove()
            Pcircle.remove()
    plt.show()


if __name__ == "__main__":
    shape_animation()
