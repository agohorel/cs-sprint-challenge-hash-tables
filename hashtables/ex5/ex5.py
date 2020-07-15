# Your code here



def finder(files, queries):
    directory = {}
    result = []

    for f in files:
        suffix = f.rsplit("/", 1)[-1]

        if suffix not in directory:
            directory[suffix] = [f]
        else:
            directory[suffix].append(f)

    for q in queries:
        try:
            for path in directory[q]:
                result.append(path)
        except:
            pass

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/bin/folder/foo',
    ]
    queries = [
        "foo",
        "qux",
        "baz",
        "foo"
    ]

    print(finder(files, queries))
