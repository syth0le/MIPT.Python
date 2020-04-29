class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1
        self.map[5][2] = -1

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


system = System()
lighter = Light()
system.get_lightening(lighter)


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


