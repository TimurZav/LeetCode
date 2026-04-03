def unique_once(lst):
    unique_lst = {}
    for i in range(len(lst)):
        counter = 0
        if lst[i] not in unique_lst:
            unique_lst[lst[i]] = counter + 1
        else:
            unique_lst[lst[i]] += 1
    return list(dict(filter(lambda x: x[1] == 1, unique_lst.items())))

def unique_once(lst):
      count = {}
      for item in lst:
          count[item] = count.get(item, 0) + 1
      return [k for k, v in count.items() if v == 1]

print(unique_once([1, 2, 1, 1]))  # → [3, 4, 5]