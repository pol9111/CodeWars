def camel_case(string):
    result_title = string.title()
    result_split = result_title.split()
    result_string = ''.join(result_split)
    print(result_string)


camel_case("camel case method")


def camel_case(string):
    return string.title().replace(" ", "")
                          #old(space), new(None)


