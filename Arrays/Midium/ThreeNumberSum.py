def threeNumberSum(array, targetSum):
    array.sort()
    memory = set(array)
    memory2 = set()
    output = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            three_numbers = []
            temp = targetSum - (array[i] + array[j])
            if temp in memory and array[i] != temp and array[j] != temp:
                if array[i] < array[j] < temp:
                    three_numbers.append(array[i])
                    three_numbers.append(array[j])
                    three_numbers.append(temp)
                elif array[i] < temp < array[j]:
                    three_numbers.append(array[i])
                    three_numbers.append(temp)
                    three_numbers.append(array[j])
                elif array[j] < array[i] < temp:
                    three_numbers.append(array[j])
                    three_numbers.append(array[i])
                    three_numbers.append(temp)
                elif array[j] < temp < array[i]:
                    three_numbers.append(array[j])
                    three_numbers.append(temp)
                    three_numbers.append(array[i])
                elif temp < array[i] < array[j]:
                    three_numbers.append(temp)
                    three_numbers.append(array[i])
                    three_numbers.append(array[j])
                elif temp < array[j] < array[i]:
                    three_numbers.append(temp)
                    three_numbers.append(array[i])
                    three_numbers.append(array[j])

                if (not array[i] in memory2) or (not array[j] in memory2) or (not temp in memory2):
                    output.append(three_numbers)
                    memory2.add(array[i])
                    memory2.add(array[j])
                    memory2.add(temp)

    return output


array =  [12, 3, 1, 2, -6, 5, -8, 6]
print(threeNumberSum(array,0))










