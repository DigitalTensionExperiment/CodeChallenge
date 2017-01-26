


def transformer(input, return_type="html"):
    '''

    Code that a caller can use to transform
    an arbitrarily nested data structure
    into either html
    or a Javascript literal ;

    return_type is set to html as default ;

    '''

    converted_string = ""

    if input is not None:

        # Handling input in the form of list:
        if type(input) == list:

            # Opening literal/tags:
            if return_type == "html":
                converted_string += "<ol>"
            elif return_type == "js":
                converted_string += "["

            # Using recursion because the depth of the nesting is unknown:
            for element in input:
                if return_type == "html":
                    converted_string += "<li>" + transformer(element, return_type=return_type) + "</li>"
                elif return_type == "js":
                    converted_string += transformer(element, return_type=return_type) + ","

            # Closing literal/tags:
            if return_type == "html":
                converted_string += "</ol>"
            elif return_type == "js":
                converted_string = converted_string[:-1] + "]"

            return converted_string

        # Handling input in the form of dict:
        elif type(input) == dict:

            # Opening literal/tags:
            if return_type == "html":
                converted_string += "<dl>"
            elif return_type == "js":
                converted_string += "{"

            # Using recursion because the depth of the nesting is unknown:
            for key,value in input.items():
                if return_type == "html":
                    converted_string += "<dt>" + \
                                        str(key) + "</dt><dd>" + transformer(value, return_type=return_type) + "</dd>"
                    # converted_string += "<dt>" + str(key) + "</dt><dd>" + str(value) + "</dd>"
                elif return_type == "js":
                    converted_string += '"' + str(key) + '" : ' + transformer(value, return_type=return_type) + ","
                    # converted_string += str(key) + ":" + str(value) + ","

            # Closing literal/tags:
            if return_type == "html":
                converted_string += "</dl>"
            elif return_type == "js":
                converted_string = converted_string[:-1] + "}"


            return converted_string

        # Handling input in the form of int, str, or object:
        elif type(input) in [int, str, object]:
            if return_type == "js":
                converted_string += '"' + str(input) + '"'
            else:
                converted_string += str(input)

            return converted_string

    else:
        # If input is None: return an empty string
        return ""


if __name__ == "__main__":

    a = ["random", 0, 1]
    b = [{1: "one"}, "random", 0]
    c = {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    d = [{1: "one"}, "random", 0, {'a': {'aa':00, 'ab':01}, 'c': 2, 'b': 1, 'd': 3}]

    format = ["html", "js"]

    for data in [a,b,c,d]:
        for preference in format:
            print "format = " + str(preference) + " : data = " + str(data)
            print transformer(data, return_type=preference)

            print "= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ="

        print "//////////////////////////////////////////////////////////////"
        print "//////////////////////////////////////////////////////////////"































