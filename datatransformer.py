


def transformer(input, return_type="html"):
    '''

    Code that a caller can use
    to transform an arbitrarily nested data structure
    into either html
    or a Javascript literal.

    '''

    # if return_type == "html":
    #     converted_string = "<ol>"
    # elif return_type == "js":
    #     converted_string = "["

    converted_string = ""

    if input is not None:

        if type(input) == list:
            # # Opening literal/tags:
            if return_type == "html":
                converted_string += "<ol>"

            elif return_type == "js":
                converted_string += "["
            # print "[list] " + str(converted_string)

            # Using recursion because the depth of the nesting is unknown:
            for element in input:
                if return_type == "html":
                    converted_string += "<li>" + transformer(element, return_type=return_type) + "</li>"
                    # converted_string += "<li>" + str(element) + "</li>"
                elif return_type == "js":
                    print element
                    converted_string += transformer(element, return_type=return_type) + ","
                    #converted_string += str(element) + ","

            # Closing literal/tags:
            if return_type == "html":
                converted_string += "</ol>"
            elif return_type == "js":
                converted_string = converted_string[:-1] + "]"

            print "[list] " + str(converted_string)

            return converted_string

        elif type(input) == dict:

            # Opening literal/tags:
            if return_type == "html":
                converted_string += "<dl>"
            elif return_type == "js":
                converted_string += "{"

            #print "[dict] " + str(converted_string)

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

            print "[dict] " + str(converted_string)

            return converted_string

        elif type(input) in [int, str, object]:
            if return_type == "js":
                converted_string += '"' + str(input) + '"'
            else:
                converted_string += str(input)
            print "[int, str, object] " + str(converted_string)
            return converted_string



if __name__ == "__main__":

    #c = ["random", 0, 1, 2, {'a': 0, 'c': 2, 'b': 1, 'd': 3}, 3, 4, "strings"]

    c = ["random", 0, 1]
    # html = <li>random</li><li>0</li><li>1</li>
    # js = random,0,1,

    d = [{1: "one"}, "random", 0]

    e = {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    # <dt>a</dt><dd>0</dd><dt>c</dt><dd>2</dd><dt>b</dt><dd>1</dd><dt>d</dt><dd>3</dd></dl>

    f = [{1: "one"}, "random", 0, {'a': {'aa':00, 'ab':01}, 'c': 2, 'b': 1, 'd': 3}]
    # js = [{"1" : "one"},"random","0",{"a" : {"aa" : "0","ab" : "1"},"c" : "2","b" : "1","d" : "3"}]

    transformer(f, return_type="js")

    print "//////////////////////////////////////////////////////////////"


'''
<ol>
 <li>
  <dl>
   <dt>1</dt><dd>one</dd>
  </dl>
 </li>
 <li>random</li>
 <li>0</li>
 <li>
  <dl>
   <dt>a</dt>
   <dd>
    <dl>
     <dt>aa</dt><dd>0</dd>
     <dt>ab</dt><dd>1</dd>
    </dl>
   </dd>
   <dt>c</dt><dd>2</dd>
   <dt>b</dt><dd>1</dd>
   <dt>d</dt><dd>3</dd>
  </dl>
 </li>
</ol>

'''





























