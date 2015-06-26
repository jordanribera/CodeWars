def brain_luck(code, input):
    code = list(code)
    input_queue = [0]
    input_queue = list(input)
    input_queue.reverse()
    heap = [0]
    data_pointer = 0
    code_pointer = 0
    output = ""
    running = True
    while running:
        command = code[code_pointer]
        #print command
        if command == ">":
            #increment pointer
            data_pointer += 1
            if len(heap) <= data_pointer:
                heap.append(0)
        elif command == "<":
            #decrement pointer
            data_pointer -= 1
        elif command == "+":
            #increment value
            heap[data_pointer] = (heap[data_pointer] + 1) % 256
        elif command == "-":
            #decrement
            heap[data_pointer] = (heap[data_pointer] - 1) % 256
        elif command == ".":
            #output
            output = output + chr(heap[data_pointer])
        elif command == ",":
            #input
            heap[data_pointer] = ord(input_queue.pop())
        elif command == "[":
            #blockstart
            if heap[data_pointer] == 0:
                search_point = code_pointer
                seeking_blocks = 1
                found_blocks = 0
                while found_blocks < seeking_blocks:
                    search_point += 1
                    if code[search_point] == "[":
                        seeking_blocks += 1
                    if code[search_point] == "]":
                        found_blocks += 1
                code_pointer = search_point
        elif command == "]":
            #blockend
            if heap[data_pointer] != 0:
                search_point = code_pointer
                seeking_blocks = 1
                found_blocks = 0
                while found_blocks < seeking_blocks:
                    search_point -= 1
                    if code[search_point] == "]":
                        seeking_blocks += 1
                    if code[search_point] == "[":
                        found_blocks += 1
                code_pointer = search_point

        code_pointer += 1
        
        if code_pointer == len(code):
            running = False

    return output
