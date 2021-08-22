import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:

    rw=RandomWalk(50000)
    rw.fill_walk()
    fig,ax=plt.subplots(figsize=(10,6))

    poin_number=range(rw.num_points)
    ax.scatter(rw.x_valuse,rw.y_valuse,c=poin_number,cmap=plt.cm.Blues,edgecolors='none',s=15)

    # 突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_valuse[-1],rw.y_valuse[-1],c='red',edgecolors='none',s=100)

    # 隐藏坐标轴
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

    run=input("keep running? y/n: ")
    if run=='n':
        break