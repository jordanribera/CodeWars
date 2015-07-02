def solution(string,markers):
    lines = string.split("\n")
    for line in range(len(lines)):
        for marker in markers:
            lines[line] = lines[line].split(marker)[0].rstrip()
    return "\n".join(lines)
