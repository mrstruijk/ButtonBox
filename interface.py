class Interface:
    def __init__(self):
        raise NotImplementedError("Subclasses must implement initialize.")

    def step(self):
        raise NotImplementedError("Subclasses must implement step.")

    def shutdown(self):
        raise NotImplementedError("Subclasses must implement shutdown.")