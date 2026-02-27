import src.pyprinty as pyt


terminal = pyt.Terminal()


@terminal.page("page 1")
def test_page_one(name):
    print(f"hay from page num 1 {name}")
    test_page_two(name)
    print(f"bye from page num 1 {name}")


@terminal.page("page 2")
def test_page_two(name):
    print(f"hay from page num 2 {name}")
    test_page_three(name)
    print(f"bye from page num 2 {name}")


@terminal.page("page 3")
def test_page_three(name):
    print(f"hay from page num 3 {name}")
    print(f"bye from page num 3 {name}")


if __name__ == "__main__":
    test_page_one(name="example_name")
