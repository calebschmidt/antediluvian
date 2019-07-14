class ContextHolder:
    def __init__(self, names):
        for name, i in zip(names, range(len(names))):
            setattr(self, name, i)


names = [
    'MAIN_MENU',
    'PLAYING',
    'PAUSED'
]

contexts = ContextHolder(names)
