import json


with open("/home/timur/Загрузки/dicts.json") as file:
    content = file.read()
    content = content.rstrip("\n").replace("\n", ",")
    content = f'[{content}]'
    json_content = json.loads(content)
    print(len(json_content))

    json_content_unique = [dict(t) for t in {tuple(d.items()) for d in json_content}]
    print(len(json_content_unique))

    res_list = {frozenset(item.items()): item for item in json_content}.values()
    print(len(res_list))

    seen = set()
    new_l = []
    for d in json_content:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)

    print(len(new_l))
