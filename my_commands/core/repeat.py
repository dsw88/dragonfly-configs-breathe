from my_commands.imports import *

playback_history = PlaybackHistory(2)
playback_history.register()

last_command = None


def repeat_command(count):
    global last_command
    last_playback: Playback = playback_history[0]

    first_word = last_playback._series[0][0][0]
    if first_word != "repeat":
        last_command = last_playback

    if last_playback:
        for n in range(count):
            last_command.execute()


mapping = {
    "repeat <count>": Function(repeat_command),
}
extras = [
    IntegerRef("count", 1, 20),
]

Breathe.add_commands(
    context=None,
    mapping=mapping,
    extras=extras,
)
