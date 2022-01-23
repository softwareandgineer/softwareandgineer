for p in [False, True]:
    for q in [False, True]:
        for r in [False, True]:
            print(f"p={p}, \rq={q},r= {r} \tresults={(not (p and q)) or r}")

