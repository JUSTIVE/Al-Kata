import re


def solve(value: str) -> str:
    def validate() -> bool:
        return re.sub(r'pi|ka|chu', r'', value) == ''

    def render(value: bool) -> str:
        return "YES" if value else "NO"

    return render(validate())


print(solve(input()))
