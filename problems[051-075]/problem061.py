import time


def p(m, n):
    a = m - 2
    b = 4 - m
    return n * (a * n + b) // 2


def generate_series(from_, to):
    series = list()
    for m in range(from_, to):
        m_series = list()
        n = 0
        while True:
            n += 1
            result = p(m, n)
            if result < 1000:
                continue
            if result > 9999:
                break
            str_result = str(result)
            if str_result[2] == "0":
                continue
            m_series.append(str_result)
        series.append(m_series)
    return series

def generate_tree_and_all(from_, to, series):
    tree = {str(i): [] for i in range(10, 100)}
    all_ = []
    for m, m_series in zip(range(from_, to), series):
        for s in m_series:
            value = (m, s)
            all_.append(value)
            tree[s[:2]].append(value)
    return tree, all_


def main(total=6):
    def recursive(chosen):
        length = len(chosen)
        if length == 0:
            for value in all_:
                for result in recursive(chosen + [value]):
                    if result is not None:
                        yield result
            return None
        if length == total:
            if chosen[-1][1][2:] != chosen[0][1][:2]:
                return None
            yield chosen
        for value in tree[chosen[-1][1][2:]]:
            if any(value[0] == c[0] for c in chosen):
                continue
            for result in recursive(chosen + [value]):
                if result is not None:
                    yield result
    series = generate_series(3, 3 + total)
    print([len(i) for i in series])
    tree, all_ = generate_tree_and_all(3, 3 + total, series)

    for results in recursive([]):
        print(results, sum(int(i[1]) for i in results))



if __name__ == '__main__':
    initial_time = time.time()
    main()
    final_time = time.time()
    difference = round(final_time - initial_time, 3)
    print(f"It took {difference} seconds")
