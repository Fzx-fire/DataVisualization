from random import choice

class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points=5000):
        self.num_points=num_points

        # 所有随机漫步初始于（0,0）
        self.x_valuse=[0]
        self.y_valuse=[0]

    def fill_walk(self):
        while len(self.x_valuse)<self.num_points:
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_distance*x_direction

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # 不在原地不动
            if x_step==0 and y_step==0:
                continue

            x=self.x_valuse[-1]+x_step
            y=self.y_valuse[-1]+y_step

            self.x_valuse.append(x)
            self.y_valuse.append(y)