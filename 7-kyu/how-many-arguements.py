# DESCRIPTION:
# Create a function args_count, that returns the count of passed arguments

#solution
# Create a function args_count, that returns count of passed arguments
def args_count(*argss,**args):
    return len(args) +len(argss)