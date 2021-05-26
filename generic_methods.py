from selenium.webdriver.support.ui import Select


def drop_down(drop_down_name, drop_down_value):
    dropItem = Select(drop_down_name)
    dropItem.select_by_visible_text(drop_down_value)


def print_all_values(drop_down_name):
    items = Select(drop_down_name)
    values = items.options
    for item in values:
        print(item.text)


def stop_after_specific_value(drop_down_name, value):
    items = Select(drop_down_name)
    values = items.options
    for item in values:
        if item.text == value:
            break
