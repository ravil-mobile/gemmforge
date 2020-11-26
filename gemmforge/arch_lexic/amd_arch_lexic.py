from .abstract_arch_lexic import AbstractArchLexic


class AmdArchLexic(AbstractArchLexic):

    def __init__(self):
        AbstractArchLexic.__init__(self)
        self.threadIdx_y = "hipThreadIdx_y"
        self.threadIdx_x = "hipThreadIdx_x"
        self.threadIdx_z = "hipThreadIdx_z"
        self.blockIdx_x = "hipBlockIdx_x"
        self.blockDim_y = "hipBlockDim_y"
        self.blockDim_z = "hipBlockDim_z"

    def get_launch_code(self, func_name, grid, block, func_params):
        return "hipLaunchKernelGGL(kernel_{}, {}, {}, 0, 0, {})".format(func_name, grid, block, func_params)
