from classes import *
import interactions
from interactions import Option, OptionType, SelectMenu, SelectOption, ActionRow, ButtonStyle, Button, Modal, TextInput

name_form = Modal(
    title="The Journey Begins",
    custom_id="character_name_form",
    components=[TextInput(
        style=interactions.TextStyleType.SHORT,
        label="You were dreaming. What's your name?",
        custom_id="character_name",
        min_length=1,
        max_length=25)
    ]
)

attribute_select = SelectMenu(custom_id="attribute_select",
                              placeholder="Choose your attributes",
                              options=[SelectOption(label=attribute.name,
                                                    value=attribute.name)
                                       for attribute in PLAYER_ATTRIBUTES],
                              min_values=2,
                              max_values=2)

race_select = SelectMenu(custom_id="race_select",
                         placeholder="Select your race",
                         options=[SelectOption(label=race.name,
                                               value=race.name)
                                  for race in PLAYER_RACES],
                         max_values=1)

specialization_row = ActionRow(
    components=[
        Button(
            style=ButtonStyle.DANGER,
            label="Combat",
            custom_id="combat_selected"
        ),
        Button(
            style=ButtonStyle.PRIMARY,
            label="Magic",
            custom_id="magic_selected"
        ),
        Button(
            style=ButtonStyle.SUCCESS,
            label="Stealth",
            custom_id="stealth_selected"
        )
    ])