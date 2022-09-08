import sys

# define group level master information
current_make_model = ""
count = 0


def reset():
    """Reset master info for every group"""
    global current_make_model
    global count
    current_make_model = ""
    count = 0


def flush():
    """write the output"""
    print(f"{current_make_model}\t{count}") if current_make_model else None


for line in sys.stdin:

    # parse the input from mapper and update the master info
    make_model, *data = line.strip().split("\t")

    # detect key changes
    if current_make_model != make_model:
        if current_make_model is not None:
            # write result to stdout
            flush()
        reset()

    # update more master info after the key change handling
    current_make_model = make_model
    count += 1


# do not forget to output the last group if needed
flush()
