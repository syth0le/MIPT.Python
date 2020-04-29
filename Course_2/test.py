class MappingAdapter:

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        height = grid
        width = grid[0]
        work_area = (len(width), len(height))
        self.adaptee.set_dim(work_area)
        lights_massive = self.getting_cords(1, grid)
        self.adaptee.set_lights(lights_massive)
        walls_massive = self.getting_cords(-1, grid)
        self.adaptee.set_obstacles(walls_massive)
        return self.adaptee.generate_lights()

    #@staticmethod
    #def getting_cords(num, massive):
        #work_massive = []
        #for i in massive:
            #if num in i:
               # work_massive.append((i.index(num), massive.index(i)))
        #return work_massive

    @staticmethod
    def getting_cords(num, massive):
        result = []
        for i in range(len(massive)):
            for j in range(len(massive[i])):
                if massive[i][j] == num:
                    result.append((j, i))
        return result
