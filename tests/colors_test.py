from src import pyprinty


print(
    pyprinty.colors.WHITE(background=True) + \
    pyprinty.colors.RED() + \
    "white background and red text!" + \
    pyprinty.colors.Initialize_background_color + \
    " not white background!" + \
    pyprinty.colors.Initialize_text_color + \
    " and not red text!"
)

print("test is done!")
