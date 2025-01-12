import os

L_SIZE = max(os.get_terminal_size().columns - 39, 10)


def ft_tqdm(lst: range) -> None:
    """
Display a n bar for an iterable.
    """
    n_elem = len(lst)

    for elem in lst:
        n = int(elem / n_elem * L_SIZE)
        if (elem + 1) % 20 == 0 or elem == n_elem - 1:
            # new version
            print(
                f"{(elem / n_elem*100):>3,.0f}%|{'█' * n}"
                f"{' '* (L_SIZE-n-2)}| {min(elem+1, n_elem)}/{n_elem}",
                end="\r",
                flush=True,
            )
            # old version
            # if elem == 1:
            #     print(
            #         f"{(elem/n_elem*100):>3,.0f}%|[{'-'*n}>]"
            #         f"{' '*(L_SIZE-n-2)}| {min(elem+1,n_elem)}/{n_elem}",
            #         end="\r",
            #         flush=True,
            #     )
            # elif elem == n_elem - 1:
            #     print(
            #         f"{(elem / n_elem * 100):>3,.0f}%|[{'-' * (n-3)}>]"
            #         f"{' '*(L_SIZE-n-2)}| {min(elem+1,n_elem)}/{n_elem}",
            #         end="\r",
            #         flush=True,
            #     )
            # else:
            #     print(
            #         f"{(elem / n_elem * 100):>3,.0f}%|[{'-' * n}"
            #         f"{' '*(L_SIZE-n-2)}| {min(elem+1,n_elem)}/{n_elem}",
            #         end="\r",
            #         flush=True,
            #     )
        yield elem
