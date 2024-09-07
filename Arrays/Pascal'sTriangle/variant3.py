def generateRow(row):
    ansRow = [1]
    ans = 1
    
    for col in range(1,row):
        ans = ans*(row-col)
        ans = ans//col
        ansRow.append(ans)

    return ansRow


def generate(n):
    pascalTriangle = []

    for row in range(1,n+1):
        pascalTriangle.append(generateRow(row))

    return(pascalTriangle)


print(generate(3))