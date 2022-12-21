from typing import List, Any

x: List[Any]=list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
print(x)

for animal in x:
    assert isinstance(animal, object)
    print(animal)