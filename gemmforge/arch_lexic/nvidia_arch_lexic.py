from .abstract_arch_lexic import AbstractArchLexic


class NvidiaArchLexic(AbstractArchLexic):

    def __init__(self):
        AbstractArchLexic.__init__(self)
        self.threadIdx_y = "threadIdx.y"
        self.threadIdx_x = "threadIdx.x"
        self.threadIdx_z = "threadIdx.z"
        self.blockIdx_x = "blockIdx.x"
        self.blockDim_y = "blockDim.y"
        self.blockDim_z = "blockDim.z"

    def get_launch_code(self, func_name, grid, block, func_params):
        return "kernel_{}<<<{},{}>>>({})".format(func_name, grid, block, func_params)
